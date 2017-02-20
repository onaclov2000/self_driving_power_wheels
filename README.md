# self_driving_power_wheels

# Motor Controller
This motor controller is great thus far.
http://www.digikey.com/product-detail/en/infineon-technologies/DCMOTORCONTRBTN8982TOBO1/DCMOTORCONTRBTN8982TOBO1-ND/5878319

Shipping was fast too which was nice.

Works well with Arduino, raspberry pi worked as well. Worked using logic level converters, however I think I'm going to run out of some space, plus I need to be able to do PWM and it's not clear the PI will do it directly, bought a PWM board from adafruit to help with that, now PI needs just I2C I think.

## PWM 12 Bit Board
May need more boards, we'll see, I think really we need 2 PWM signals per board, everything else is just high or low, and really the linear actuator just needs voltage, so may not even care about PWM. Now that I think about it.

https://github.com/adafruit/Adafruit_Python_PCA9685/blob/master/examples/simpletest.py

https://learn.adafruit.com/16-channel-pwm-servo-driver/downloads

Datasheets/etc that are helpful

http://www.infineon.com/dgdl/Infineon-H-Bridge+Software_setup_Dave-UM-v01_00-EN.pdf?fileId=5546d4624cb7f111014cc2238eca3248

http://www.infineon.com/cms/en/product/productType.html?productType=5546d4624ad04ef9014b07c0c07922e0#ispnTab4

# Opencv install on PI
http://www.pyimagesearch.com/2015/10/26/how-to-install-opencv-3-on-raspbian-jessie/


# Linear Actuator
http://amzn.to/2lcuoX5

This will handle the movement using an arduino,Pi Works, working on PWM board now.
https://github.com/onaclov2000/self_driving_power_wheels/blob/master/lin_act.ino

## Lin Act INO
This file drives the linear actuator the full left and right that it needs.
It doesn't work with lower voltages, so needs 12V. So all we do is set the full voltage for a period of time.
271 * 50 is the limit to limit time required at 12V
moving left or right subsets of that amount would require a division.

## Wiring
MOTOR CONTROLLER is setup in H-Bridge state
This means:
  Black wire to OUT1
  Red wire to OUT2

BATT to 12v and GND to well... GND

IN_2 drives backwards (or in)
IN_1 drives forwards (or out) 
* This means that if I swap wiring it'll go opposite directions from stated.

Used #8-32 .5 inch screws with a lock washer and nut. Found at Home Depot for pretty good deal (like a buck and a half for 8, so I needed 2 packs, and the washers were a 20 pack and about the same price)

## Driving Directions
http://stackoverflow.com/questions/36035439/get-google-maps-walking-directions-json-instead-of-driving
