#There are three ways that a parent & child class can interact
# 1. Actions on the child imply an action on the parent.
# 2. Actions on the child override the action on the parent.
# 3. Actions on the child alter the actions on the parent
def printL():
	print '-' * 10

#1. Implicit Inheritence
class Parent(object):
	def implicit(self):
		print "Parent Implicit"
	def override(self):
		print "Parent override"
	def altered(self):
		print "Parent altered"

class ChildImplicitInheritence(Parent):
	#Pass is how you tel pythong that you want an empty block.
	pass

class ChildOverrideExplicitly(Parent):
	def override(self):
		print 'Child overriiiides!'

class ChildSuper(Parent):
	def altered(self):
		print "Child before altering takes place..."
		super(ChildSuper, self).altered()
		print "Child, after altering has been done."







dad = Parent()
son1 = ChildImplicitInheritence()
son2 = ChildOverrideExplicitly()
son3 = ChildSuper()

printL()
print "Implicit Inheritence."
dad.implicit()
son1.implicit()
printL()
print "Override Explicitly"
dad.override()
son2.override()
printL()
print "Altering before and after"
dad.altered()
son3.altered()