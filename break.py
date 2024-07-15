for letter in 'python':
    if letter=='h':
        break
    print('current letter:',letter)
var=10
while var>0:
    print('current variable value:',var)
    var=var-1
    if var==5:
        break
print('good bye')
id=[1,2,3,4,5]
print(id)
x=int(input('enter a number:'))
for i in range(len(id)):
    if x==id[i]:
        break
if i<len(id)-1:
    print(x,'found at position:',i+1)
else:
    print(x,'not found in list')
