import json
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Hàm đọc file JSON và trích xuất quỹ đạo
def extract_trajectory(json_file):
    try:
        with open(json_file, 'r') as f:
            data = json.load(f)
    except Exception as e:
        print(f"Lỗi khi đọc file JSON {json_file}: {e}")
        return [], None

    drone_positions = []
    target_position = None

    # Trích xuất thông tin từ phần "nodes" để lấy vị trí ban đầu
    nodes = data.get('nodes', [])
    for node in nodes:
        node_name = node.get('name', '')
        if node_name == "Target":
            pos = node.get('position', {})
            if 'x' in pos and 'y' in pos and 'z' in pos:
                target_position = (pos['x'], pos['y'], pos['z'])
            else:
                print(f"Dữ liệu vị trí không đầy đủ cho Target: {pos}")

    # Trích xuất vị trí của drone từ phần "events"
    events = data.get('events', [])
    if not events:
        print(f"Không tìm thấy 'events' trong file {json_file}")
        return [], target_position

    for event in events:
        if event.get('type') != 'node-position':
            continue

        node_id = event.get('id')
        if node_id == 0:  # Drone
            time = event.get('nanoseconds', 0) / 1e9  # Chuyển từ nanoseconds sang seconds
            x = event.get('x')
            y = event.get('y')
            z = event.get('z')
            if x is not None and y is not None and z is not None:
                drone_positions.append((time, x, y, z))
            else:
                print(f"Dữ liệu vị trí không đầy đủ cho Drone: {event}")

    if not drone_positions:
        print(f"Không tìm thấy dữ liệu vị trí cho Drone trong file {json_file}")
    if target_position is None:
        print(f"Không tìm thấy dữ liệu vị trí cho Target trong file {json_file}")

    return drone_positions, target_position

# Hàm vẽ quỹ đạo 3D
def plot_trajectory(drone_positions, target_position, title, output_file):
    if not drone_positions or target_position is None:
        print(f"Không có dữ liệu để vẽ quỹ đạo cho {title}. Kiểm tra file JSON.")
        return

    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')

    # Trích xuất x, y, z từ quỹ đạo drone
    times, xs, ys, zs = zip(*drone_positions)
    
    # Vẽ quỹ đạo drone
    ax.plot(xs, ys, zs, label='Drone trajectory', color='blue', marker='o', markersize=3)
    
    # Đánh dấu điểm bắt đầu và kết thúc của drone
    ax.scatter(xs[0], ys[0], zs[0], color='green', s=100, label='Start')
    ax.scatter(xs[-1], ys[-1], zs[-1], color='red', s=100, label='End')
    
    # Đánh dấu vị trí target
    ax.scatter(target_position[0], target_position[1], target_position[2], color='orange', s=100, label='Target')

    # Đặt nhãn cho các trục
    ax.set_xlabel('X (m)')
    ax.set_ylabel('Y (m)')
    ax.set_zlabel('Z (m)')
    ax.set_title(title)

    # Đặt giới hạn cho trục (phù hợp với không gian mô phỏng)
    ax.set_xlim(0, 100)
    ax.set_ylim(-100, 0)
    ax.set_zlim(0, 50)

    # Hiển thị chú thích
    ax.legend()

    # Lưu đồ thị vào file
    plt.savefig(output_file)
    print(f"Đồ thị đã được lưu vào {output_file}")

# Main
if __name__ == "__main__":
    # Đọc và vẽ quỹ đạo cho chiến lược random
    random_json = "sar_drone_simulation_random.json"
    random_drone_positions, random_target_position = extract_trajectory(random_json)
    plot_trajectory(random_drone_positions, random_target_position, "Drone Trajectory (Random)", "random_trajectory.png")

    # Đọc và vẽ quỹ đạo cho chiến lược rl
    rl_json = "sar_drone_simulation_rl.json"
    rl_drone_positions, rl_target_position = extract_trajectory(rl_json)
    plot_trajectory(rl_drone_positions, rl_target_position, "Drone Trajectory (RL)", "rl_trajectory.png")