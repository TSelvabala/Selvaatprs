a=60
b=13
print('a=',a,':',bin(a),'b=',':',bin(b))
c=0
c=a & b;
print("result of AND is",c,':',bin(c))
c=a | b;
print("result of OR is",c,':',bin(c))
c=a ^ b;
print("result of EXOR is",c,':',bin(c))
c=~a;
print("result of COMPLEMENT is",c,':',bin(c))
c=a << 2;
print("result of LEFT SHIFT is",c,':',bin(c))
c=a >> 2;
print("result of RIGHT SHIFT is",c,':',bin(c))

