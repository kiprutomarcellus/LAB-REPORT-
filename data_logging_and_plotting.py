import random
import time
import matplotlib.pyplot as plt

# Lists to store the data in memory
temps = []
humidity = []

# Task 1: Initialize values for logging
num_samples = 10

try:
    # We open files once before the loop for better performance/error handling
    # Task 2: Using different file formats (CSV and TXT)
    with open("data_log.csv", "a") as csv_file, open("data_log.txt", "a") as txt_file:
        
        for t in range(num_samples):
            # Task 1: Log both temperature and humidity
            temp = round(25 + random.uniform(-1, 1), 2)
            hum = round(50 + random.uniform(-5, 5), 2)
            
            temps.append(temp)
            humidity.append(hum)
            
            # Writing to CSV format
            csv_file.write(f"{t},{temp},{hum}\n")
            # Writing to TXT format (more descriptive)
            txt_file.write(f"Time: {t}s | Temp: {temp}C | Humidity: {hum}%\n")
            
            print(f"Logged: {temp}C, {hum}%")
            time.sleep(0.5)

# Task 3: Add error handling for file operations
except IOError as e:
    print(f"File Error: Could not write to file. {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

# Visualization
plt.figure(figsize=(10, 5))
plt.plot(temps, label="Temperature (C)", color="red")
plt.plot(humidity, label="Humidity (%)", color="blue")
plt.xlabel("Time (s)")
plt.ylabel("Value")
plt.title("Environmental Data Log")
plt.legend()
plt.grid(True)
plt.show()
