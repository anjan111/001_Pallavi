'''

If we list all the natural numbers below 10
that are multiples of 3 or 5, we get 3, 5, 6 and 9.
The sum of these multiples is 23.
'''
N = input("enter N  :")
list = range(1,N)
sum =0
for e in list:
    if( e % 3 == 0  or e % 5 == 0):
        print e
        sum = sum +e
print "sum : ", sum
    
