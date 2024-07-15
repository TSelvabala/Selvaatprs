try:
    x=int(input("enter number:"))
    y=int(input("enter another number:"))
    z=x/y
    print("z=",z)
except(ValueError,ZeroDivisionError,KeyboardInterrupt):
    print("error occured")
