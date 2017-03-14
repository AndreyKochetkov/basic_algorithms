
x = 1L
u = 0
while 1:
   for y in xrange(1, x):
       for z in xrange(1, y):

           if x*x == y*y + 12752041*z*z:
               print "Found it"
   x = x + 1