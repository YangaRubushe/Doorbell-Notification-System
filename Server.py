import socket
import RPi.GPIO as GPIO
import time

# Setting the GPIO mode
GPIO.setmode(GPIO.BCM)
button_pin = 4  
GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def handle_button_press():

    GPIO.setup(button_pin, GPIO.IN)
    GPIO.setup(button_pin, GPIO.OUT)
    GPIO.output(button_pin, GPIO.HIGH)
    GPIO.output(button_pin, GPIO.LOW)

# Created a TCP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bound the socket to the IP address oand port 5000
server_address = ("Your IP address here", 5000)
print('starting up on %s port %s' % server_address)
sock.bind(server_address)

# Listening for incoming connections
sock.listen(1)
print("Waiting for a connection ")
connection, client_address = sock.accept()

try:
    print("Connection established from ", client_address)

    while True:
        # Checks if the button is pressed
        if GPIO.input(button_pin) == GPIO.LOW:
            handle_button_press()
            # Wait for button release
            while GPIO.input(button_pin) == GPIO.LOW:
                time.sleep(0.1)
            print("The button has been Pressed")
                        
            try:
                # Sends a message to the client
                connection.send(bytes("There is someone at the door. Please check. ", "utf-8")) 
            except ConnectionResetError:
                print("Client closed the connection")
                break

except KeyboardInterrupt:
    print("Closing socket ")
    sock.close()