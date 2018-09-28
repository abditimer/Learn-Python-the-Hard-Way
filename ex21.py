def add(a, b):
	print "Adding %d + %d" % (a,b)
	return a + b

def subtract(a,b):
	print "%d - %d" % (a,b)
	return a-b

def multiple(a,b):
	print "%d * %d" % (a,b)
	return a*b

def divide(a,b):
	print "%d / %d" % (a,b)
	return a/b

print " Lets do some fun maths!"

age = add(30,5)
height = subtract(78,4)
weight = multiple(90,2)
iq = divide(100,2)

print "Age: %d, height: %d, weight: %d, iq: %d" % (age, height, weight,iq)

print "Here is a puzzle"

what = add(age, subtract(height, multiple(weight, divide(iq,2))))

print "That becomes: ", what, "Can you do it by hand?"