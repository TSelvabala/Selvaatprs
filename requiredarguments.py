#required
def printme(str):
    print(str)
    return
printme(str)
#keyword
def printme(name,age):
    print("name:",name)
    print("age:",age)
    return
printme("abc",19)
printme(age=30,name="selva")
#default
def printme(name="bala",age=20):
    print("name:",name)
    print("age:",age)
    return
printme("abc")
printme(age=30)
#variable length
def printme(arg1,*var):
    print("Output is:")
    print(arg1)
    for var in var:
        print(var)
    return
printme(10)
printme(20,40,60)
