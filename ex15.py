from sys import argv

script, filename1, filename2 = argv

txt = open(filename1)

print "Here's your file %r:" % filename1
print txt.read()

print "Here's the second file %r:" % filename2

text_again = open(filename2)

print text_again.read()