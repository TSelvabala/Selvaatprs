total=0
def sum(arg1,arg2):
    total=arg1+arg2
    print("inside the function local total:",total)
    return total
sum(10,20)
print("outside the function local total:",total)
