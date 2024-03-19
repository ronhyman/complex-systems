import numpy as np
import matplotlib.pyplot as plt

# Parameters
delta_t = 0.01
T_H0 = 400
T_C0 = 300

# Function to calculate the heat flow
def calculate_heat_flow(T_H, T_C):
    return T_H - T_C

# Function to calculate the useful work
def calculate_useful_work(T_H, T_C):
    return calculate_heat_flow(T_H, T_C) * (1 - T_C / T_H)

# Arrays to store results
time_steps = np.arange(0, 10, delta_t)
T_H_values = np.zeros_like(time_steps)
T_C_values = np.zeros_like(time_steps)

# Initial conditions
T_H_values[0] = T_H0
T_C_values[0] = T_C0

# Loop using Euler method to calculate temperatures
for i in range(1, len(time_steps)):
    Q = calculate_heat_flow(T_H_values[i-1], T_C_values[i-1])
    W = calculate_useful_work(T_H_values[i-1], T_C_values[i-1])
    
    T_H_values[i] = T_H_values[i-1] - Q * delta_t
    T_C_values[i] = T_C_values[i-1] + (Q - W) * delta_t

# Calculate work and heat flow over the simulation
total_work = np.trapz(calculate_useful_work(T_H_values, T_C_values), dx=delta_t)
total_heat_flow = np.trapz(calculate_heat_flow(T_H_values, T_C_values), dx=delta_t)

# Calculate actual efficiency
actual_efficiency = total_work / total_heat_flow

print(f"Actual Efficiency: {actual_efficiency:.2f}")

# Plot results
plt.plot(time_steps, T_H_values, label="T_H")
plt.plot(time_steps, T_C_values, label="T_C")
plt.xlabel("Time (s)")
plt.ylabel("Temperature (K)")
plt.legend()
plt.show()