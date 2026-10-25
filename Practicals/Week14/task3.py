import RPi.GPIO as GPIO
import time
# Define constants
LED_PIN = 17
BLINK_COUNT = 5
BLINK_DELAY = 1
def setup_gpio():
 # Set the GPIO mode to BCM (Broadcom SOC channel).
 GPIO.setmode(GPIO.BCM)
 # Set up the LED GPIO pin as an output.
 GPIO.setup(LED_PIN, GPIO.OUT)
def blink_led():
 try:
 # Loop to blink the LED for a specified number of times.
 for _ in range(BLINK_COUNT):
 # Turn the LED on.
 GPIO.output(LED_PIN, GPIO.HIGH)
 print("LED ON")
 # Wait for a specified duration.
 time.sleep(BLINK_DELAY)
 # Turn the LED off.
 GPIO.output(LED_PIN, GPIO.LOW)
 print("LED OFF")
 # Wait for the same duration.
 time.sleep(BLINK_DELAY)
 except KeyboardInterrupt:
 # If the user interrupts the program (Ctrl+C), clean up GPIO.
 GPIO.cleanup()
if __name__ == "__main__":
 try:
 setup_gpio()
 blink_led()
 finally:
 # Clean up GPIO when the program exits.
 GPIO.cleanup()