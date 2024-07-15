def changeme(mylist):
    "this change a passed list into the function"
    print(id(mylist))
    print("values inside the function before change:",mylist)
    mylist[2]=50
    print("values inside the function after change:",mylist)
    return
mylist=[10,20,20]
print(id(mylist))
changeme(mylist)
print("values outside the function:",mylist)


def changeme(mylist):
    "this change a passed list into the function"
    mylist=[1,2,3,4,5]
    print(id(mylist))
    print("values inside the function:",mylist)
    return
mylist=[10,20,30]
print(id(mylist))
changeme(mylist)
print("values outside the function:",mylist)
    
