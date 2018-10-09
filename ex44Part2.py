class Other(object):

	def override(self):
		print "Other override1..."

	def implicit(self):
		print "other override2.."

	def altered(self):
		print "Other altered.."

class Child(object):
	def __init__(self):
		self.other = Other()

	def implicit(self):
		self.other.implicit()

	def override(self):
		print "child overrides!"

	def altered(self):
		print "Child, before other is altered"
		self.other.altered()
		print "child, after other is altered."

son = Child()

son.implicit()
son.override()
son.altered()