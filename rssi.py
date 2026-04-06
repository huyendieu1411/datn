import pandas as pd
import matplotlib.pyplot as plt

no_noise = pd.read_csv("wifi_log.csv")
with_noise = pd.read_csv("wifi_communication_log.csv")

plt.figure(figsize=(10, 6))
plt.plot(no_noise["Time(S)"], no_noise["RSSI(dBm)"], label="Không nhiễu", color='green')
plt.plot(with_noise["Time(S)"], with_noise["RSSI(dBm)"], label="Có nhiễu", color='red', linestyle='--')
plt.xlabel("Thời gian (s)")
plt.ylabel("RSSI (dBm)")
plt.title("So sánh RSSI theo thời gian")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("rssi_comparison.png")
plt.show()
