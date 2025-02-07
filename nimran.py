import serial
import time
import csv

SERIAL_PORT = 'COM10'  # Change based on your system
BAUD_RATE = 9600

# Open serial connection
ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
time.sleep(2)  # Allow time for the connection to establish

# CSV file setup
csv_filename = "nimran.csv"

with open(csv_filename, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Timestamp", "SensorData"])  # Write header

    try:
        while True:
            if ser.in_waiting:
                sensor_data = ser.readline().decode('utf-8').strip()
                timestamp = time.strftime("%Y-%m-%d %H:%M:%S")  # More readable timestamp
                writer.writerow([timestamp, sensor_data])
                print(f"{timestamp}, {sensor_data}")
                time.sleep(1)  # Delay for readability

    except KeyboardInterrupt:
        print("Data collection stopped.")
        ser.close()