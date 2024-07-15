try:
    fh=open("testfile","w")
    try:
        fh.write("this is my test file!!")
    finally:
        print("going to close the file")
        fh.close()
except IOError:
    print("error:can\'t find file or read data")
