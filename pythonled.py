#written for python 2.7


import RPi.GPIO as GPIO
import time
import socket

HOST, PORT = '', 8888

listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
listen_socket.bind((HOST, PORT))
listen_socket.listen(1)
print 'Serving HTTP on port %s ...' % PORT
while True:
    client_connection, client_address = listen_socket.accept()
    request = client_connection.recv(1024)
    print request

    http_response = "hello people"

    count = 0    

    #makes blue LED on GPIO pin 18 flash

    while (count < 9):
        print "hello blue"
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(18,GPIO.OUT)
        print "LED on"
        GPIO.output(18,GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(18,GPIO.LOW)
        print "LED off"
        GPIO.output(18,GPIO.LOW)
        count = count + 1


    
    #makes red and yellow LED on GPIO pin 23 flash

    print "hello program"
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(23,GPIO.OUT)
    print "LED on"
    GPIO.output(23,GPIO.HIGH)
    time.sleep(1)
    print "LED off"
    GPIO.output(23,GPIO.LOW)


    #makes green LED on GPIO pin 24 flash

    print "hello program"
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(24,GPIO.OUT)
    print "LED on"
    GPIO.output(24,GPIO.HIGH)
    time.sleep(1)
    print "LED off"
    GPIO.output(24,GPIO.LOW)


    client_connection.sendall(http_response)
    client_connection.close()