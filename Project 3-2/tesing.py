import numpy as np

# Example matrices (replace these with your actual matrices)
od_flow = np.random.randint(size = [5, 5], high = 200, low = 100, )  # 5x5 matrix
sir_percent = np.random.rand(3, 5) # 3x5 matrix

# Get the second row from the SIR matrix (index 1 since Python is zero-indexed)
second_row_SIR = sir_percent[1, :]

# Multiply each row of od by the corresponding value from the second row of SIR

print(od_flow)
print()
print(sir_percent)
print()

second_row_SIR = sir_percent[1, :]
od_infected = od_flow * second_row_SIR[:, np.newaxis]  # Broadcasting across rows

print(od_infected)
