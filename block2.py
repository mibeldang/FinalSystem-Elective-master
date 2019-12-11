# BLOCK TWO
import RPi.GPIO as GPIO
import time
import paho.mqtt.client as mqtt
client = mqtt.Client()
client.connect("test.mosquitto.org", 1883, 60)

# ----------------Laser Start-----------------------
LedPin = 11
count = 0

def setup():
    GPIO.setmode(GPIO.BOARD) 
    GPIO.setup(LedPin, GPIO.OUT)
    GPIO.output(LedPin, GPIO.HIGH)

def emergency():
    global count
    while(count <= 20):
        print 'Laser = on'
        GPIO.output(LedPin, GPIO.LOW) # led on
        time.sleep(1)
        count += 1
        if(count == 21):
            GPIO.output(LedPin, GPIO.HIGH) # led off
        

def eatingTime():
    global count
    while(count <= 5):
        print 'Laser=on'
        GPIO.output(LedPin, GPIO.LOW) # led on
        time.sleep(5)
        print 'Laser=off'
        GPIO.output(LedPin, GPIO.HIGH) # led off
        time.sleep(1)
        count += 1

def GoingToUSC():
    global count
    while(count <= 10):
        print 'Laser=on'
        GPIO.output(LedPin, GPIO.LOW) # led on
        time.sleep(3)
        print 'Laser=off'
        GPIO.output(LedPin, GPIO.HIGH) # led off
        time.sleep(2)
        count += 1

def PagingB2():
    global count
    while(count <= 10):
        print('Laser=on')
        GPIO.output(LedPin, GPIO.LOW) # led on
        time.sleep(1.5)
        print('Laser=off')
        GPIO.output(LedPin, GPIO.HIGH) # led off
        time.sleep(1)
        count += 1

# def PagingB1():
#     global count
#     while(count <= 10):
#         print('Laser=on')
#         GPIO.output(LedPin, GPIO.LOW) # led on
#         time.sleep(1)
#         print('Laser=off')
#         GPIO.output(LedPin, GPIO.HIGH) # led off
#         time.sleep(1)
#         count += 1

def destroy():
    GPIO.output(LedPin, GPIO.LOW)
    GPIO.cleanup()

def on_message(client, userdata, msg):
    global count
    if str(msg.payload) == "Emergency":
        print("\nEMERGENCY\n")
        emergency()
        print("\nDone\n")
        count = 0
    if str(msg.payload.decode("utf-8"))=="EatingTime":
        print("\nEATING TIME\n")
        eatingTime()
        print("\nDone\n")
        count = 0
    if str(msg.payload.decode("utf-8"))=="GoingToUSC":
        print("\nGOING TO USC\n")
        GoingToUSC()
        print("\nDone\n")
        count = 0
    if str(msg.payload.decode("utf-8"))=="PagingB2":
        print("\nPAGING BLOCK 2\n")
        PagingB2()
        print("\nDone\n")
        count = 0
    # if str(msg.payload.decode("utf-8"))=="PagingB1":
    #     print("\nPAGING BLOCK 1\n")
    #     PagingB1()
    #     print("\nDone\n")
    #     count = 0
    elif str(msg.payload.decode("utf-8"))=="off":
        destroy()
        print("\nDone\n")



client.on_message = on_message
client.on_connect = client.subscribe("Project")
setup()
client.loop_forever()
