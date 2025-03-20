import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_json("drill_data.json")
plt.plot(data["time"], data["rpm"])
plt.title("Drill RPM Over Time")
plt.show()

avg_rpm = data["rpm"].mean()
if data["rpm"].iloc[-1] < avg_rpm * 0.9:  # 10% drop
    print("Drill’s slowing—maybe brushes need a look!")
