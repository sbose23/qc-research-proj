import matplotlib.pyplot as plt
import json 

with open('./brute_force_classical/Results/runtime_data.json', 'r') as f:
    runtime_data = json.load(f)

with open('./brute_force_classical/Results/runtime_increase_data.json', 'r') as f:
    runtime_increase_trend = json.load(f)

x1 = list(map(int, runtime_data.keys()))
y = list(runtime_data.values())

x2 = list(map(int, runtime_increase_trend.keys()))
z = list(runtime_increase_trend.values())

fig, ax1 = plt.subplots()

ax1.plot(x1, y, 'bo-', label='Runtime (s)')
ax1.set_xlabel('Bitstring length')
ax1.set_ylabel('Runtime (s)', color='b')
ax1.tick_params(axis='y', labelcolor='b')

ax2 = ax1.twinx()
ax2.plot(x2, z, 'r^-', label='Percentage increase (%)')
ax2.set_ylabel('Percentage increase (%)', color='r')
ax2.tick_params(axis='y', labelcolor='r')

plt.title("Runtime & Runtime Increase Trend of Brute Force AES Key Search")
fig.tight_layout()
plt.show()
