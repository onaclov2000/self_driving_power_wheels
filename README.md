# self_driving_power_wheels

# Motor Controller
digikey [TBD]
Works well with Arduino, will try with raspberry pi when parts come in.

# Linear Actuator
http://amzn.to/2lcuoX5


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




