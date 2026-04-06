import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from math import sqrt

# Load data from CSV files
no_noise_data = pd.read_csv('wifi_log.csv')
with_noise_data = pd.read_csv('wifi_communication_log.csv')

# Debug: Print first few rows to verify data
print("No Noise Data Sample:", no_noise_data.head())
print("With Noise Data Sample:", with_noise_data.head())

# Calculate distance from drone to base station (0, 0, 0) - only for reference, not used in plot
def calculate_distance(row):
    return sqrt(row['X']**2 + row['Y']**2 + row['Z']**2)

no_noise_data['Distance'] = no_noise_data.apply(calculate_distance, axis=1)
with_noise_data['Distance'] = with_noise_data.apply(calculate_distance, axis=1)

# Set up the plot style
plt.style.use('ggplot')  # Use ggplot style (available by default)
plt.rcParams['font.size'] = 12

# Figure 1: RSSI over Time
plt.figure(1, figsize=(10, 6))
plt.plot(no_noise_data['Time(S)'], no_noise_data['RSSI(dBm)'], label='No Noise RSSI', color='blue', linewidth=2)  # Nét liền
plt.plot(with_noise_data['Time(S)'], with_noise_data['RSSI(dBm)'], label='With Noise RSSI', color='green', linewidth=2, linestyle='--')  # Nét đứt

plt.xlabel('Time (s)')
plt.ylabel('RSSI (dBm)')
plt.title('RSSI over Time')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.7)

# Adjust layout and save
plt.tight_layout()
plt.savefig('rssi_over_time.png', dpi=300)  # Save as high-resolution image
plt.show()

# Figure 2: Packet Loss over Time
plt.figure(2, figsize=(10, 6))
plt.plot(no_noise_data['Time(S)'], no_noise_data['PacketLoss(%)'], label='No Noise Packet Loss', color='orange', linewidth=2)  # Nét liền
plt.plot(with_noise_data['Time(S)'], with_noise_data['PacketLoss(%)'], label='With Noise Packet Loss', color='red', linewidth=2)  # Nét liền

plt.xlabel('Time (s)')
plt.ylabel('Packet Loss (%)')
plt.title('Packet Loss over Time')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.7)
plt.ylim(-5, 20)  # Adjust y-axis for packet loss

# Adjust layout and save
plt.tight_layout()
plt.savefig('packet_loss_over_time.png', dpi=300)  # Save as high-resolution image
plt.show()

# Print statistical analysis
print("Statistical Analysis:")
print(f"No Noise - Average RSSI: {no_noise_data['RSSI(dBm)'].mean():.2f} dBm")
print(f"With Noise - Average RSSI: {with_noise_data['RSSI(dBm)'].mean():.2f} dBm")
print(f"With Noise - Average Packet Loss: {with_noise_data['PacketLoss(%)'].mean():.2f}%")
print(f"With Noise - Packet Loss Std Dev: {with_noise_data['PacketLoss(%)'].std():.2f}%")