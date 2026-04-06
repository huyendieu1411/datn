import pandas as pd
import matplotlib.pyplot as plt

no_noise = pd.read_csv("wifi_log.csv")
with_noise = pd.read_csv("wifi_communication_log.csv")

avg1 = no_noise["PacketLoss(%)"].mean()
avg2 = with_noise["PacketLoss(%)"].mean()

plt.figure(figsize=(6, 6))
plt.bar(["Không nhiễu", "Có nhiễu"], [avg1, avg2], color=["green", "red"])
plt.ylabel("Mất gói trung bình (%)")
plt.title("So sánh mức mất gói trung bình")
plt.tight_layout()
plt.savefig("packet_loss_comparison.png")
plt.show()
