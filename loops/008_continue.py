# continue
'''
==>> we should use with in the loops
==>> to skip the current iteration and continue next iteration
'''
# print 1 to 10 except 3 and 7

i = 0
while( i < 10):
    i = i+1
    if( i == 3  or i == 7):
        continue
    print i
