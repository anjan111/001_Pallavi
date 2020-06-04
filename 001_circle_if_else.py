#wap find the area of circle when rad is float other wise find perimeter
rad = input("enter rad of circle in meters : ")
pi = 22.0 /7
if ( isinstance(rad,float) ) :
    area = pi * (rad ** 2 )
    print "area : ",area," sq m "
else:
    peri  = 2 * pi * rad
    print "perimter : ",peri," meters"
print "Task finished"
