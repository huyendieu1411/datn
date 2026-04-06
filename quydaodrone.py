import matplotlib.pyplot as plt
import pandas as pd
from mpl_toolkits.mplot3d import Axes3D

# Đọc dữ liệu từ file CSV
df = pd.read_csv('wifi_communication_log.csv')

# Trích xuất dữ liệu
time = df['Time(S)']
x = df['X']
y = df['Y']
z = df['Z']

# Tạo biểu đồ 3D
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Vẽ quỹ đạo drone
ax.plot(x, y, z, label='Drone Trajectory', color='blue', marker='o')

# Đánh dấu điểm bắt đầu và kết thúc
ax.plot([x.iloc[0]], [y.iloc[0]], [z.iloc[0]], 'go', label='Start', markersize=10)
ax.plot([x.iloc[-1]], [y.iloc[-1]], [z.iloc[-1]], 'ro', label='End', markersize=10)

# Đặt nhãn và tiêu đề
ax.set_xlabel('X (m)')
ax.set_ylabel('Y (m)')
ax.set_zlabel('Z (m)')
ax.set_title('Drone Trajectory in 3D Space')
ax.legend()

# Đặt giới hạn trục (dựa trên dữ liệu)
ax.set_xlim(min(x) - 5, max(x) + 5)
ax.set_ylim(min(y) - 5, max(y) + 5)
ax.set_zlim(min(z) - 2, max(z) + 2)

# Thêm lưới để dễ quan sát
ax.grid(True)

# Lưu và hiển thị biểu đồ
plt.savefig('drone_trajectory_3d.png')
plt.show()
plt.close()

print("Biểu đồ quỹ đạo drone đã được lưu dưới dạng: drone_trajectory_3d.png")