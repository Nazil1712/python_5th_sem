import RPi.GPIO as GPIO
import time
# Set the GPIO mode to BCM (Broadcom SOC channel).
GPIO.setmode(GPIO.BCM)
# Set up GPIO pin 17 as an output.
GPIO.setup(17, GPIO.OUT)
try:
 # Loop to blink the LED 5 times.
 for _ in range(5):
 # Turn the LED on.
 GPIO.output(17, GPIO.HIGH)
 # Wait for 1 second.
 time.sleep(1)
 # Turn the LED off.
 GPIO.output(17, GPIO.LOW)
 # Wait for 1 second.
 time.sleep(1)
except KeyboardInterrupt:
 # If the user interrupts the program (Ctrl+C), cleanup GPIO.
 GPIO.cleanup()
# Clean up GPIO when the program exits.
GPIO.cleanup()