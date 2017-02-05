# self_driving_power_wheels

# Motor Controller
This motor controller is great thus far.
http://www.digikey.com/product-detail/en/infineon-technologies/DCMOTORCONTRBTN8982TOBO1/DCMOTORCONTRBTN8982TOBO1-ND/5878319

Shipping was fast too which was nice.

Works well with Arduino, will try with raspberry pi when parts come in.
Datasheets/etc that are helpful

http://www.infineon.com/dgdl/Infineon-H-Bridge+Software_setup_Dave-UM-v01_00-EN.pdf?fileId=5546d4624cb7f111014cc2238eca3248

http://www.infineon.com/cms/en/product/productType.html?productType=5546d4624ad04ef9014b07c0c07922e0#ispnTab4



# Linear Actuator
http://amzn.to/2lcuoX5

This will handle the movement using an arduino, I'd like to move to pi soon, but we'll see how it goes.
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




