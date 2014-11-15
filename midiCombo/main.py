# used for reading args
import sys

# used for checking file existance
import os

# data container
from collections import Counter


# project imports
from KeyMapReader import *
from MidiDeviceReader import *
from CommandInterpreter import *

VERSION_NUMBER = "0.1"


def printInfo():
    print("\nMidiCombo " + VERSION_NUMBER + " needs at least the name of a mapping file (mandatory)")
    print("You can also specify the name of a MIDI controller (optional).")
    print("\t-mapping <file>\t(mandatory)")
    print("\t-device <name>\t(optional)")


def findArgValue(argName, mandatory=True):
    argValue = None

    try:
        argNameIndex = sys.argv.index(argName)
        argValue = sys.argv[argNameIndex + 1]

    except ValueError, e:
        if(mandatory):
            print(e)
            printInfo()
            exit()

    except IndexError, e:

        #print(e)
        print("ERROR: a value for the argument " + str(argName) + " was not found.")
        printInfo()
        exit()

    return argValue





if __name__ == '__main__':
    print("________________________________________________________________________________")
    print("                                MidiCombo " + VERSION_NUMBER)


    # handles the args

    # finding the mapping file (mandatory)
    mappingFile = findArgValue("-mapping")
    if(not os.path.isfile(mappingFile)):
        print("ERROR: this mapping file does not exist.")
        printInfo()
        exit()

    # finding the MIDI device name (optional)
    deviceName = findArgValue("-device", False)






    try:
        # creating the key map reader, in charge of reading the
        # instruction from the .setting file
        kmr = KeyMapReader()
        kmr.setMapFileName(mappingFile)
        kmr.processMapFile()

        # creating the command interpreter
        ci = CommandInterpreter()
        # giving the key-argument map to the command interpreter:
        ci.setKeyArgumentMap(  kmr.getKeyArgumentMap() )



        mdr = MidiDeviceReader(deviceName)
        mdr.setCommandInterpreter(ci)
        mdr.readFlow()

    except KeyboardInterrupt:
        mdr.close()
        exit()
