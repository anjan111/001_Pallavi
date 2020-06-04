### Python Program Structure

##### program file  having 2 names #
'''
===>>> outside of the program file  what name programmer given
===>>> inside of the program file the program file  __name__  <<===>> __main__
'''
def fun_name1():
    print " I am BO  Fun1 "
    print " I am EO  Fun1 "
def fun_name2():
    print " I am BO  Fun2 "
    fun_name1()
    print " I am EO  Fun2 "
def main():
    print "i am BO Main fucction"
    fun_name2()
    print " I am EO  Main Fun "
    
if __name__ == "__main__":
    main()
    print "Program Done"
