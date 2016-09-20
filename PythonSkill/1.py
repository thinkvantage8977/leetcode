

#Create a dictionary
heap = [(-f, c) for c, f in collections.Counter(str).items()]

#Create multu demension array
dp = [[0 for x in range(len(nums))] for y in range(len(nums))]

#Create a dictioanry with default object
d = collections.defaultdict(object)

#Sorted with lambda
l.sort(key=lambda x: (x[0], x[1]))

# OOP
class Parent:        # define parent class
   parentAttr = 100
   def __init__(self):
      print "Calling parent constructor"

   def parentMethod(self):
      print 'Calling parent method'

   def setAttr(self, attr):
      Parent.parentAttr = attr

   def getAttr(self):
      print "Parent attribute :", Parent.parentAttr

class Child(Parent): # define child class
   def __init__(self):
      print "Calling child constructor"

   def childMethod(self):
      print 'Calling child method'

c = Child()          # instance of child
c.childMethod()      # child calls its method
c.parentMethod()     # calls parent's method
c.setAttr(200)       # again call parent's method
c.getAttr()          # again call parent's method


# Overriding
class Parent:        # define parent class
   def myMethod(self):
      print 'Calling parent method'

class Child(Parent): # define child class
   def myMethod(self):
      print 'Calling child method'

c = Child()          # instance of child
c.myMethod()         # child calls overridden method




type(o) is str

isinstance(o, str)

issubclass(type(o), str)

isinstance(o, basestring)