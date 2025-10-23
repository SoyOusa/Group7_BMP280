# main.py — TB Cloud MQTT (1883) publish BMP280 data
import network, time, json
from umqtt.simple import MQTTClient
from machine import I2C, Pin
from bmp280 import BMP280

# Wi-Fi credentials
SSID = "Robotic WIFI"
PASS = "rbtWIFI@2025"

# ThingsBoard settings
TB_HOST = "mqtt.thingsboard.cloud"
TB_PORT = 1883
TB_TOKEN = b"TbXzoVXG4xrb7WSZkUvv"
TOPIC = b"v1/devices/me/telemetry"

# Initialize I2C for BMP280 (adjust pins for your board)
# Common ESP32 pins: SCL=22, SDA=21
i2c = I2C(0, scl=Pin(22), sda=Pin(21), freq=400000)
bmp = BMP280(i2c)

# Wi-Fi connection
w = network.WLAN(network.STA_IF)
w.active(True)
if not w.isconnected():
    print("Connecting to Wi-Fi...")
    w.connect(SSID, PASS)
    t = time.ticks_ms()
    while not w.isconnected():
        if time.ticks_diff(time.ticks_ms(), t) > 15000:
            raise RuntimeError("Wi-Fi timeout")
        time.sleep(0.2)
print("Wi-Fi:", w.ifconfig())

# MQTT connection (username = token, password empty)
c = MQTTClient(b"esp32-tb", TB_HOST, port=TB_PORT, user=TB_TOKEN, password=b"", keepalive=30, ssl=False)
c.connect()
print("Connected to", TB_HOST, ":", TB_PORT)

# Main loop - read and publish sensor data
while True:
    try:
        # Read BMP280 sensor data
        temp = round(bmp.temperature, 2)  # °C
        pressure = round(bmp.pressure, 2)  # hPa
        altitude = round(bmp.altitude, 2)  # meters
        
        # Create JSON payload
        data = {
            "temperature": temp,
            "pressure": pressure,
            "altitude": altitude
        }
        msg = json.dumps(data).encode("utf-8")
        
        # Publish to ThingsBoard
        print(f"Publishing: T={temp}°C, P={pressure}hPa, Alt={altitude}m")
        c.publish(TOPIC, msg)
        
    except Exception as e:
        print("Error reading sensor or publishing:", e)
    
    time.sleep(5)  # Publish every 5 seconds