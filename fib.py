def fibo(n):
    result=[]
    a,b=0,1
    while b<n:
        result.append(b)
        a,b=b,a+b
    return result
def hello():
    print("hello")
    return
