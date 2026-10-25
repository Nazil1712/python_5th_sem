import RPi.GPIO as GPIO
import time
# Set the GPIO mode to BCM
GPIO.setmode(GPIO.BCM)
# Define the GPIO pin for the LED
led_pin = 18
# Set up the GPIO pin as an output
GPIO.setup(led_pin, GPIO.OUT)
try:
 while True:
 # Turn the LED ON
 GPIO.output(led_pin, GPIO.HIGH)
 print("LED ON")
 time.sleep(1) # Wait for 1 second
 # Turn the LED OFF
 GPIO.output(led_pin, GPIO.LOW)
 print("LED OFF")
 time.sleep(1) # Wait for 1 second
except KeyboardInterrupt:
 # Clean up GPIO settings on program exit
 GPIO.cleanup()