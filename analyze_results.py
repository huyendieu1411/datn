import pandas as pd
import numpy as np

num_runs = 10
completion_times = []
min_distances = []

for i in range(1, num_runs + 1):
    df = pd.read_csv(f'trajectory_{i}.csv')
    # Thời gian hoàn thành
    completion_time = df['time'].iloc[-1]
    completion_times.append(completion_time)
    # Khoảng cách tối thiểu
    df['distance'] = np.sqrt((df['drone_x'] - df['target_x'])**2 +
                             (df['drone_y'] - df['target_y'])**2 +
                             (df['drone_z'] - df['target_z'])**2)
    min_distance = df['distance'].min()
    min_distances.append(min_distance)

print(f"Average completion time: {np.mean(completion_times):.2f} seconds")
print(f"Average minimum distance: {np.mean(min_distances):.2f} meters")