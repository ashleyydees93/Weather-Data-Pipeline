
import pandas as pd
import matplotlib.pyplot as plt

# Read the weather data we collected
df = pd.read_csv("data/weather_data.csv")

# Display the data
print(df)

# Create a temperature comparison chart
plt.figure(figsize=(9, 5))

plt.bar(df["city"], df["temperature_f"])

plt.title("Temperature Comparison Across NC Cities")
plt.xlabel("City")
plt.ylabel("Temperature (°F)")

plt.tight_layout()

# Save the chart
plt.savefig("figures/temperature_comparison.png")

print("\nChart saved to figures/temperature_comparison.png")
