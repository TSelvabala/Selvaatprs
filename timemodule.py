import time
t=time.localtime()
print("asctime:",asctime(t))
t0=time.clock()
time.sleep(2.5)
print(time.clock()-t0,"seconds process time")
t0=time.time()
time.sleep(2.5)
print(time.time()-t0,"seconds wall time")
print("ctime:",time.ctime())
print("time.localtime():",time.localtime())
t=(2016,12,3,13,45,38,1,48,0)
d=time.mktime(t)
print("time.mktime(t):%f"%d)
print("asctime(localtime(secs)):%s"%time.asctime(time.localtime(d)))
print("s
