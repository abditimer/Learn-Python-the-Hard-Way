numbers = []


def numberBreakdown(finalNum, increment):
	i=0
	for i in range(0, finalNum):
		#print "At the top i is %d" % i
		numbers.append(i)
	
		#i = i + increment
		#print "Numbers now: ", numbers
		#print "At the bottom i is %d" % i
	
	print "The numbers: "

	for num in numbers:
		print num

finalNoInput = int(raw_input("What is your final number?"))
incrementInput = int(raw_input("Tell me how much to increment by?"))
print "Let me show you some magic!\n"

numberBreakdown(finalNoInput, incrementInput)