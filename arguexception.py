def square(var):
    try:
        print(int(var)**2)
        return
    except ValueError as argument:
        print("the argument does not contain numbers\n",argumrnt)
square("10")
square('abc')
