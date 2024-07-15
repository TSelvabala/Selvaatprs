try:
    marks=int(input("input marks"))
    if marks<0 or marks>100:
        raise Exception(marks)
    print("marks within valid range=",marks)
except Exception as e:
    print("error.invalid marks input",e)
