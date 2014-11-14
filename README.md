MidiCombo
=========

## Introduction
MidiCombo is a Python tool for triggering actions from a MIDI controller (like a music MIDI keyboard or pad) by pressing and/or releasing a key. The performed actions can be of various kinds because MidiCombo uses a plugin architecture. A plugin is a Python package or even just a Python function that manages its own dependencies. Hence, you plugin more or less what you want, as long as it is coded in Python.

To make the link between an action (aka, a plugin) and a key pressed/released on your MIDI controller, a mapping file needs to be created.

At the origin, MidiCombo was created to simulate complex keyboard shortcuts in Adobe Photoshop Lightroom (or other fancy softwares full of ninja shortcuts) in order to go faster with repetitive tasks that cannot be totally automated.


## The mapping file
The mapping file makes the links between a behaviour on the MIDI controller (like a key pressed or released) and a plugin (software action). It looks like a CSV text file with tabulation separators (real tabs, not spaces).
As an example, it is composed of lines like this one:

```
# Types the string abc
1	P	plugin|keyboard|typeString|abc
```

As shown on the example, you can use # at the begining of the line to add a comment.
Then:
* '__1__' means the first key of your MIDI device. MIDI keys are index and you can know more about how is indexed this or that key by reading the section [Side Tools](https://github.com/jonathanlurie/MidiCombo/blob/master/README.md#side-tools) section.
* '__P__' means we are about to map a _key-Pressing_ behaviour. We could have used the letter 'R' to map a _key-Releasing_ behaviour.
* '__plugin|keyboard|typeString|abc__' means several things, note we are splitting them with the Pipe ('|') character:
  1. '__plugin__' mean we are about to call a plugin. Such an expression will always start by the word 'plugin'.
  2. '__keyboard__' is the name of the plugin we are calling, meaning __keyboard.py__ located in the __plugins__ subdirectory.
  3. '__typeString__' is a function from the file __keyboard.py__
  4. '__abc__' is a parameter needed by the function _typeString_. A function may need several parameters, if so, you must use pipes ('|') separators.

## Available plugins
TODO

## Side tools
TODO

## How to install MidiCombo
TODO

## How to launch
TODO

## A note about threads
TODO

## Depedencies
TODO : complete that

- [PyUserInputGen](https://github.com/jonathanlurie/PyUserInputGen) for keyboard emulation (examples availables in Plugins)
- [PyGame](http://www.pygame.org/download.shtml) for reading MIDI controller inputs.
