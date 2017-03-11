from motorcontroller import MotorController
import sys
right = MotorController(channels={'IN_1' : 0, 'IN_2' : 1, 'INH_1' : 2, 'INH_2' : 3})
left =  MotorController(channels={'IN_1' : 4, 'IN_2' : 5, 'INH_1' : 7, 'INH_2' : 6})
right.reverse(10)
#right.reverse(10)
right.zeroize()
left.forward(10)
left.zeroize()
#while True:
#   try:
#      pass
#   except:
#      left.zeroize()
#      right.zeroize()
#      break
      
