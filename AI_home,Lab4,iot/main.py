import sys
import time
import random
from simpleAI import *
from Adafruit_IO import MQTTClient

AIO_FEED_ID = ["bong-den", "may-bom"]
AIO_USERNAME = "Hynsandyy"
AIO_KEY = "aio_cpNt46RrKSIda287stCQUd7DjAF8"

def connected(client):
    print("Ket noi thanh cong ...")
    for topic in AIO_FEED_ID:
        client.subscribe(topic)

def subscribe(client , userdata , mid , granted_qos):
    print("Subscribe thanh cong ...")

def disconnected(client):
    print("Ngat ket noi ...")
    sys.exit (1)

def message(client , feed_id , payload):
    print("Nhan du lieu: " + payload + " , feed id: " + feed_id)

client = MQTTClient(AIO_USERNAME , AIO_KEY)
client.on_connect = connected
client.on_disconnect = disconnected
client.on_message = message
client.on_subscribe = subscribe
client.connect()
client.loop_background()

# Khai báo biến đếm thời gian
counter = 10
counter_ai = 10
while True:

    # Đếm ngược thời gian để phát sinh dữ liệu
    counter = counter - 1
    if counter <= 0:
        counter = 10
        print("\nPhát sinh dữ liệu ngẫu nhiên để publishing...")
        temp = random.randint(0,100)
        client.publish("nhiet-do", temp)

        humidity = random.randint(0,100)
        client.publish("do-am", humidity)

        bright = random.randint(0,2000)
        client.publish("anh-sang", bright)
    
    # Đếm ngược thời gian để chạy AI
    counter_ai = counter_ai - 1
    if counter_ai<=0:
        counter_ai = 5
        ai_result = Image_dectector()
        client.publish("du-doan-ai", ai_result)
    
    time.sleep(1)