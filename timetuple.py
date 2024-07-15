import time
print("time tuple")
localtime=time.localtime(time.time())
print("local current time:",localtime)
print()
localtime=time.asctime(time.localtime(time.time()))
print("formatted current time:",localtime)
