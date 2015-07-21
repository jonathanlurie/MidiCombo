

from pymouse import PyMouse
from pykeyboard import PyKeyboard
import time



# type a string (dont use tab!)
def typeString(s, velocity):
    #m = PyMouse()
    k = PyKeyboard()

    #print args
    #k.press_keys(args)
    k.type_string(s)



# perform a combo like cmd + a or something
# Note: the keys will be pressed at the same time.
# BEWARE : the last value of *args is velocity !
def combo(*arg):

    theCombo = arg[:-1]
    theVelocity = arg[-1] # not used

    k = PyKeyboard()
    k.press_keys(theCombo)



# perform a combo as a sequence, meaning key after key
# (as opposite as combo() )
# BEWARE : the last value of *args is velocity !
def comboSequence(*arg):
    k = PyKeyboard()

    for key in arg[:-1]:
        k.tap_key(key)


def typeCurrentDate():
    import datetime
    typeString(datetime.datetime.now().strftime("%Y_%m_%d"))
