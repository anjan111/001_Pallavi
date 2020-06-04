#arguments
'''
===>>> to send  the data from  function call to function defination
'''
# default arguments
def  fun_name(arg1 = None , arg2 =  None , arg3 =None):# formal argument
    print "arg1 : ",arg1
    print "arg2 : ",arg2
    print "arg3 : ",arg3
fun_name(10,20,30) # actual argument
a = 45
b = 30
fun_name(10,a,a*b+12)
fun_name()

