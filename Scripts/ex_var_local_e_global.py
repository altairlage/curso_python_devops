#!/user/bin/env python

hacker = "me"
def local_variable_example():
	hacker = "you"
	print ("the local variable is " + hacker)

local_variable_example()
print ("the global variable is " + hacker)