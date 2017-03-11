# Simple demo of of the PCA9685 PWM servo/LED controller library.
# This will move channel 0 from min to max position repeatedly.
# Author: Tony DiCola, Tyson Bailey (lots of modifications, this came from simpletest in the original repo)
# License: Public Domain
from __future__ import division
import time

# Import the PCA9685 module.
import Adafruit_PCA9685
class MotorController:
# Uncomment to enable debug output.
#import logging
#logging.basicConfig(level=logging.DEBUG)
   pwm = Adafruit_PCA9685.PCA9685()
# Initialise the PCA9685 using the default address (0x40).
   def __init__(self, channels, min=1000, max=3000):
      self.channels = channels
      self.servo_min = min  # Min pulse length out of 4096
      self.servo_max = max  # Max pulse length out of 4096

      # Set frequency to 60hz, good for servos. Good for power wheel?
      pwm.set_pwm_freq(60)
      self.zeroize()
      pwm.set_pwm(self.channels["INH_1"], 0, 4095)
      pwm.set_pwm(self.channels["INH_2"], 0, 4095)

   def zeroize(self):
      for k in self.channels:
         pwm.set_pwm(self.channels[k],0,0)
         
   def forward(self, time):
      try:
         pwm.set_pwm(self.channels["IN_2"], 0, 0)
         if True:
            pwm.set_pwm(self.channels["IN_1"], 0, self.servo_max)
      except:
          self.zeroize()
   def reverse(self, time):
      try:
         pwm.set_pwm(self.channels["IN_1"], 0, 0)
         if True:
            pwm.set_pwm(self.channels["IN_2"], 0, self.servo_max)
      except:
          self.zeroize()
      
