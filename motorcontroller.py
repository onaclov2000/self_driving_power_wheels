# Simple demo of of the PCA9685 PWM servo/LED controller library.
# This will move channel 0 from min to max position repeatedly.
# Author: Tony DiCola
# License: Public Domain
from __future__ import division
import time

# Import the PCA9685 module.
import Adafruit_PCA9685
class MotorController:

# Uncomment to enable debug output.
#import logging
#logging.basicConfig(level=logging.DEBUG)

# Initialise the PCA9685 using the default address (0x40).
   def __init__(self, min=1000, max=3000):
      self.pwm = Adafruit_PCA9685.PCA9685()

# Alternatively specify a different address and/or bus:
#pwm = Adafruit_PCA9685.PCA9685(address=0x41, busnum=2)

# Configure min and max servo pulse lengths
      self.servo_min = min  # Min pulse length out of 4096
      self.servo_max = max  # Max pulse length out of 4096
# Set frequency to 60hz, good for servos.
      self.pwm.set_pwm_freq(60)
print('Moving servo on channel 0, press Ctrl-C to quit...')
     pwm.set_pwm(1,0,0)
     pwm.set_pwm(5,0,0)
     pwm.set_pwm(2,0,servo_max)
     pwm.set_pwm(3,0,servo_max)
     pwm.set_pwm(6,0,servo_max)
     pwm.set_pwm(7,0,servo_max)
if  True:
  try:
    # Move servo on channel O between extremes.
    for i in range(servo_min,servo_max):
       print i
       pwm.set_pwm(0,0,i)
       pwm.set_pwm(4,0,i)
    #time.sleep(1)
    #pwm.set_pwm(0, 0, servo_max)
    #time.sleep(1)
  except:
     pass
  zeroize()
#     break
