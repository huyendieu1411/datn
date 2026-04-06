import matplotlib.pyplot as plt
import pandas as pd

# Đọc dữ liệu từ hai file CSV
with_noise = pd.read_csv('wifi_communication_log.csv')
no_noise = pd.read_csv('wifi_log.csv')

# Thời gian làm trục X (dùng chung cho cả ba biểu đồ)
time = with_noise['Time(S)']

# 1. Biểu đồ RSSI(dBm) theo thời gian
plt.figure(figsize=(10, 6))
plt.plot(time, with_noise['RSSI(dBm)'], label='With Noise', color='#FF6384', marker='o')
plt.plot(time, no_noise['RSSI(dBm)'], label='No Noise', color='#36A2EB', marker='o')
plt.title('RSSI vs Time')
plt.xlabel('Time (s)')
plt.ylabel('RSSI (dBm)')
plt.legend()
plt.grid(True)
plt.savefig('rssi_plot.png')
plt.close()

# 2. Biểu đồ AverageDelay(ms) theo thời gian
plt.figure(figsize=(10, 6))
plt.plot(time, with_noise['AverageDelay(ms)'], label='With Noise', color='#FF6384', marker='o')
plt.plot(time, no_noise['AverageDelay(ms)'], label='No Noise', color='#36A2EB', marker='o')
plt.title('Average Delay vs Time')
plt.xlabel('Time (s)')
plt.ylabel('Average Delay (ms)')
plt.legend()
plt.grid(True)
plt.savefig('average_delay_plot.png')
plt.close()

# 3. Biểu đồ UDPSuccessRate(%) theo thời gian
plt.figure(figsize=(10, 6))
plt.plot(time, with_noise['UDPSuccessRate(%)'], label='With Noise', color='#FF6384', marker='o')
plt.plot(time, no_noise['UDPSuccessRate(%)'], label='No Noise', color='#36A2EB', marker='o')
plt.title('UDP Success Rate vs Time')
plt.xlabel('Time (s)')
plt.ylabel('UDP Success Rate (%)')
plt.legend()
plt.grid(True)
plt.ylim(0, 100)  # Đặt giới hạn trục Y từ 0 đến 100 để rõ ràng
plt.savefig('udp_success_rate_plot.png')
plt.close()

print("Biểu đồ đã được lưu dưới dạng: rssi_plot.png, average_delay_plot.png, udp_success_rate_plot.png")