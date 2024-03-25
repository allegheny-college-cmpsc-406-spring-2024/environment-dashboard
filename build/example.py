from machine import Pin, I2C
import bme280
from time import sleep
# from picozero import pico_temp_sensor, pico_led
# from umqtt.simple import MQTTClient
import network
import asyncio
from mqtt_as import MQTTClient, config
# https://github.com/peterhinch/micropython-mqtt/blob/master/mqtt_as/mqtt_as.py <- save to lib

ssid = "wifi_name"
password = "wifi_password"

i2c=I2C(0,sda=Pin(0), scl=Pin(1), freq=400000)
sleep(5)

MQTTClient.DEBUG = True  # Optional: print diagnostic messages

def connectMQTT(config):
    broker = "xx.s1.eu.hivemq.cloud"
    config['user'] = "himvemq_username"
    config['password'] = "havemq_password"
    config['ssid'] = ssid
    config['wifi_pw'] = password
    config['port'] = 8883
    config['keepalive'] = 60
    config['server'] = broker
    config['ssl'] = True
    config['ssl_params'] = {"server_hostname": broker}
    return MQTTClient(config)

client = connectMQTT(config)

async def main(client):
    await client.connect()
    while True:
        await asyncio.sleep(5)
        sensor_reading = bme280.BME280(i2c=i2c)
        t1 = sensor_reading.values[0]
        #t2 = pico_temp_sensor.temp
        pressure = sensor_reading.values[1]
        humidity = sensor_reading.values[2]
        print(t1, pressure, humidity)
        # If WiFi is down the following will pause for the duration.
        await client.publish('temp', '{}'.format(t1), qos = 1)

MQTTClient.DEBUG = True  # Optional: print diagnostic messages
client = MQTTClient(config)
try:
    asyncio.run(main(client))
finally:
    client.close()  # Prevent LmacRxBlk:1 errors

