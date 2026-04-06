import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt
import numpy as np

# Hàm đọc file XML và trích xuất vị trí
def read_animation_xml(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()

    positions = {}
    # Khởi tạo danh sách vị trí cho các node
    for node in root.findall('.//node'):
        node_id = int(node.get('id'))
        positions[node_id] = {'x': [], 'y': [], 'z': [], 'time': []}

    # Đọc các cập nhật vị trí
    for update in root.findall('.//updateNodePosition'):
        node_id = int(update.get('node'))
        time = float(update.get('time')) / 1000.0  # Chuyển từ ms sang giây
        x = float(update.get('x'))
        y = float(update.get('y'))
        z = float(update.get('z'))

        positions[node_id]['time'].append(time)
        positions[node_id]['x'].append(x)
        positions[node_id]['y'].append(y)
        positions[node_id]['z'].append(z)

    return positions

# Đọc file XML
xml_file = "sar-animation.xml"
positions = read_animation_xml(xml_file)

# In thông tin để kiểm tra node_id
print("Các node có trong file XML:", list(positions.keys()))
for node_id, data in positions.items():
    print(f"Node {node_id} có {len(data['x'])} cập nhật vị trí")

# Giả định node_id của drone, target, base station
drone_id = 0
target_id = 1
base_id = 2

# Vẽ quỹ đạo
plt.figure(figsize=(10, 8))

# Vẽ quỹ đạo drone
if drone_id in positions and len(positions[drone_id]['x']) > 0:
    drone_data = positions[drone_id]
    plt.plot(drone_data['x'], drone_data['y'], label='Drone Trajectory', marker='o')
    plt.plot(drone_data['x'][0], drone_data['y'][0], 'go', label='Start')
    plt.plot(drone_data['x'][-1], drone_data['y'][-1], 'ro', label='End')
else:
    print(f"Không có dữ liệu vị trí cho drone (node_id = {drone_id})")

# Vẽ vị trí target
if target_id in positions and len(positions[target_id]['x']) > 0:
    target_data = positions[target_id]
    plt.plot(target_data['x'][0], target_data['y'][0], 'b*', markersize=15, label='Target')
else:
    print(f"Không có dữ liệu vị trí cho target (node_id = {target_id})")

# Vẽ vị trí base station
if base_id in positions and len(positions[base_id]['x']) > 0:
    base_data = positions[base_id]
    plt.plot(base_data['x'][0], base_data['y'][0], 'ko', markersize=10, label='Base Station')
else:
    print(f"Không có dữ liệu vị trí cho base station (node_id = {base_id})")

# Nếu không có dữ liệu để vẽ, thoát
if not (drone_id in positions and len(positions[drone_id]['x']) > 0) and \
   not (target_id in positions and len(positions[target_id]['x']) > 0) and \
   not (base_id in positions and len(positions[base_id]['x']) > 0):
    print("Không có dữ liệu vị trí để vẽ. Kiểm tra file sar-animation.xml và mô phỏng.")
    exit(1)

plt.title('Drone Trajectory')
plt.xlabel('X (m)')
plt.ylabel('Y (m)')
plt.legend()
plt.grid(True)
plt.axis('equal')  # Giữ tỷ lệ trục x và y
plt.savefig('drone_trajectory.png')
plt.close()