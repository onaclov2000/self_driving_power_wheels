from motorcontroller import MotorController
import sys
right =  MotorController(channels={'INH_2' : 0, 'INH_1' : 1, 'IN_2' : 2, 'IN_1' : 3})
steer =  MotorController(channels={'INH_2' : 4, 'INH_1' : 5, 'IN_2' : 6, 'IN_1' : 7}, max=4094)
left  =  MotorController(channels={'INH_2' : 8, 'INH_1' : 9, 'IN_2' : 10, 'IN_1' : 11})

#while True:
#    print "reverse"
#    right.reverse(10)
#    #right.zeroize()
#    print "forward"
#    left.forward(10)
#    #left.zeroize()
#    print 'left'
#    steer.forward(10)
#    print 'right'
#    steer.reverse(10)
    #steer.zeroize()
right.zeroize()
left.zeroize()