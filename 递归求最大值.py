def my_max(a) :
    if len(a)>2 :
        return my_max(a[1:len(a)])
    if len(a) == 2 :
        if a[0]>a[1] :
            return a[0]
        else :
            return a[1]

print(my_max([1,3,2,6,4,10,7]))