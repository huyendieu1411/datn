import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

target_x, target_y, target_z = 44, -56, 0

no_noise = pd.read_csv("wifi_log.csv")
with_noise = pd.read_csv("wifi_communication_log.csv")

def calc_dist(df):
    return np.sqrt((df["X"] - target_x)**2 + (df["Y"] - target_y)**2 + (df["Z"] - target_z)**2)

no_noise["Distance"] = calc_dist(no_noise)
with_noise["Distance"] = calc_dist(with_noise)

plt.figure(figsize=(10, 6))
plt.plot(no_noise["Time(S)"], no_noise["Distance"], label="Không nhiễu", color='blue')
plt.plot(with_noise["Time(S)"], with_noise["Distance"], label="Có nhiễu", color='orange', linestyle='--')
plt.xlabel("Thời gian (s)")
plt.ylabel("Khoảng cách đến mục tiêu")
plt.title("So sánh khoảng cách UAV đến mục tiêu theo thời gian")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("distance_comparison.png")
plt.show()
