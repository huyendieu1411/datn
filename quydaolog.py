import re
import matplotlib
# Sử dụng backend Agg để lưu file ảnh mà không cần giao diện đồ họa
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import os

# Đọc file simulation.log
def read_trajectory_from_log(log_file):
    # Kiểm tra xem file log có tồn tại không
    if not os.path.exists(log_file):
        print(f"Lỗi: File {log_file} không tồn tại!")
        return []
    
    positions = []
    with open(log_file, 'r') as file:
        for line in file:
            if "Finished RLMove, new position" in line:
                match = re.search(r"new position: \(([^,]+),\s*([^,]+),\s*([^\)]+)\)", line)
                if match:
                    try:
                        x = float(match.group(1))
                        y = float(match.group(2))
                        z = float(match.group(3))
                        positions.append((x, y, z))
                    except ValueError as e:
                        print(f"Lỗi khi phân tích dòng: {line.strip()}. Chi tiết lỗi: {e}")
                        continue
    
    # Loại bỏ các vị trí trùng lặp liên tiếp
    unique_positions = []
    last_pos = None
    for pos in positions:
        if pos != last_pos:
            unique_positions.append(pos)
            last_pos = pos
    
    return unique_positions

# Vẽ quỹ đạo 3D và lưu thành file ảnh
def plot_trajectory(positions, output_file="drone_trajectory.png"):
    if not positions:
        print("Không có dữ liệu vị trí để vẽ đồ thị!")
        return

    # Kiểm tra quyền ghi file
    output_dir = os.path.dirname(os.path.abspath(output_file))
    if not os.access(output_dir, os.W_OK):
        print(f"Lỗi: Không có quyền ghi vào thư mục {output_dir}!")
        return

    # Tách x, y, z từ danh sách positions
    x = [pos[0] for pos in positions]
    y = [pos[1] for pos in positions]
    z = [pos[2] for pos in positions]

    # Vẽ đồ thị 3D
    try:
        fig = plt.figure(figsize=(10, 8))
        ax = fig.add_subplot(111, projection='3d')

        # Vẽ quỹ đạo drone
        ax.plot(x, y, z, label='Drone Trajectory', color='red', marker='o')

        # Đánh dấu điểm bắt đầu và kết thúc
        ax.scatter(x[0], y[0], z[0], color='green', s=100, label='Start (0, 0, 10)')
        ax.scatter(x[-1], y[-1], z[-1], color='blue', s=100, label='End')
        # Đánh dấu mục tiêu (50, -50, 0)
        ax.scatter(50, -50, 0, color='black', s=100, label='Target (50, -50, 0)')

        # Đặt nhãn cho các trục
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        ax.set_title('3D Drone Trajectory')

        # Đặt giới hạn cho các trục
        ax.set_xlim([0, 100])
        ax.set_ylim([-100, 0])
        ax.set_zlim([0, 50])

        # Hiển thị chú thích
        ax.legend()

        # Lưu đồ thị thành file ảnh
        plt.savefig(output_file, dpi=300, bbox_inches='tight')
        print(f"Đã lưu đồ thị vào file: {output_file}")
    except Exception as e:
        print(f"Lỗi khi vẽ hoặc lưu đồ thị: {e}")
    finally:
        plt.close()

if __name__ == "__main__":
    # Đường dẫn đến file simulation.log
    log_file = "simulation.log"
    
    # Trích xuất dữ liệu vị trí từ file log
    positions = read_trajectory_from_log(log_file)
    
    # Kiểm tra và in danh sách vị trí
    if not positions:
        print("Không tìm thấy dữ liệu vị trí trong file log!")
    else:
        print("Các vị trí của drone (sau khi loại bỏ trùng lặp):")
        for pos in positions:
            print(pos)
        # Vẽ quỹ đạo và lưu thành file ảnh
        plot_trajectory(positions, output_file="drone_trajectory.png")