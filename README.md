🌤️ **IoT Atmospheric Sensor Using BMP280 and ESP32**
📘 **Overview**

This project uses an ESP32 and BMP280 sensor to measure temperature, pressure, and altitude, then sends the data to the cloud for live monitoring.
It helps you learn how sensors communicate using the I²C protocol and how to send IoT data through MQTT to ThingsBoard Cloud.

🎯 **Objectives**

_Connect the BMP280 to the ESP32 using MicroPython

_Read and calculate temperature, pressure, and altitude

_Use I²C for communication

_Send data to the cloud using MQTT

_View live data on ThingsBoard dashboard

🧰 **Components**

1. ESP32 board (with MicroPython)

2. BMP280 sensor

3. Jumper wires

4. USB cable

5. Laptop with Thonny IDE

6. Wi-Fi connection
⚙️ **Circuit Connections**
ESP32	  BMP280	 Description
3V3	     VCC	    Power
GND      GND	   Ground
GPIO22	 SCL	   I²C clock
GPIO21	 SDA	   I²C data

🧩 **Setup Steps**

1. Flash MicroPython on the ESP32.

2. Open Thonny IDE and connect the board.

3. Upload the bmp280.py file.

4. Create main.py and update your Wi-Fi and MQTT details:
**WIFI_SSID = 'Your_WiFi_Name'
WIFI_PASSWORD = 'Your_WiFi_Password'
MQTT_BROKER = "test.mosquitto.org"
MQTT_PORT = 1883
CLIENT_ID = b"ESP32_Client"
TOPIC = b"sensor/data"**

# BMP280
Video Link:
https://youtube.com/shorts/cBZ0ciHF3sU?feature=share
Screen Recorded Video:
https://youtu.be/xfs7KF0wnbA
**Wire:**<img width="960" height="1280" alt="image" src="https://github.com/user-attachments/assets/c2692952-c76a-4db4-a281-2bbb914f8e79" />
