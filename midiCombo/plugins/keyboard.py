

from pymouse import PyMouse
from pykeyboard import PyKeyboard
import time



# type a string (dont use tab!)
def typeString(s):
    #m = PyMouse()
    k = PyKeyboard()

    #print args
    #k.press_keys(args)
    k.type_string(s)



# perform a combo like cmd + a or something
# Note: the keys will be pressed at the same time
def combo(*arg):
    k = PyKeyboard()
    k.press_keys(arg)


# perform a combo as a sequence, meaning key after key
# (as opposite as combo() )
def comboSequence(*arg):
    k = PyKeyboard()

    for key in arg:
        k.tap_key(key)


def typeCurrentDate():
    import datetime
    typeString(datetime.datetime.now().strftime("%Y_%m_%d"))
