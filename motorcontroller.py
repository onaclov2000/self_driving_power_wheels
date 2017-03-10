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

# Initialise the PCA9685 using the default address (0x40).
   def __init__(self, channels, min=1000, max=3000):
      self.pwm = Adafruit_PCA9685.PCA9685()
      self.channels = channels
      self.servo_min = min  # Min pulse length out of 4096
      self.servo_max = max  # Max pulse length out of 4096

      # Set frequency to 60hz, good for servos. Good for power wheel?
      self.pwm.set_pwm_freq(60)
      self.zeroize()
      self.pwm.set_pwm(self.channels["INH_1"], 0, 4095)
      self.pwm.set_pwm(self.channels["INH_2"], 0, 4095)

   def zeroize(self):
      for k in self.channels:
         self.pwm.set_pwm(self.channels[k],0,0)
         
   def forward(self, time):
      try:
         self.pwm.set_pwm(self.channels["IN_2"], 0, 0)
         while True:
            self.pwm.set_pwm(self.channels["IN_1"], 0, self.servo_max)
      except:
          self.zeroize()
   def reverse(self, time):
      try:
         self.pwm.set_pwm(self.channels["IN_1"], 0, 0)
         while True:
            self.pwm.set_pwm(self.channels["IN_2"], 0, self.servo_max)
      except:
          self.zeroize()
      
