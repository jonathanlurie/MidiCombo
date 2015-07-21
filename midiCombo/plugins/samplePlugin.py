

# shows the simplest plugin possible
def helloWorld(*args):
	print(">> From the Sample plugin:  Hello world!")


# shows a simple plugin that takes arguments.
# just performs a sum and display it.
def methodWithArguments(number1, number2, *args):
	result = int(number1) + int(number2)
	print(">> what about that: " + str(number1) +  " + " + str(number2) + " = " + str(result))


# A simple plugin that uses the key-pressed velocity.
# The velocity is accessible in the last index of the *args array
def methodWithVelocity(number1, number2, *args):
	print("Velocity : " + str(args[-1]))
