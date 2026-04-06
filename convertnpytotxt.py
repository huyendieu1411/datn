import numpy as np
q_table = np.load("q_table_exploration.npy")
np.savetxt("q_table_exploration.txt", q_table.reshape(-1, q_table.shape[-1]), fmt="%.6f")