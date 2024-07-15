pwd="ss"
while(True):
    x=input("password:")
    if x!=pwd:
        print("enter again:")
        continue
    print("password entered correctly")
    break

for letter in 'python':
    if letter=='h':
        continue
    print('current letter:',letter)

var=10
while var>0:
    var=var-1
    if var==5:
        continue
    print('current variable value:',var)
