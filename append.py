print("append()method")
list1=['C++','Java','Python']
list1.append('C#')
print("updated list:",list1)
print("count()method")
alist=[123,'xyz','zara','abc',123];
print(alist)
print("count for 123:",alist.count(123))
print("count for zara:",alist.count('zara'))
print("extend()method")
list1=['physics','chemistry','maths']
list2=list(range(5))
print(list1,list2)
list1.extend(list2)
print("extended list",list1)
print("index()method")
list1=['physics','chemistry','maths']
print(list1)
print('index of chemistry',list1.index('chemistry'))
print('index of maths:',list1.index('maths'))


#insert() method
print(list1)
list1.insert(1,"Cython")
print(list1)

#pop() method
print(list1)
list1.pop()
print(list1)

#remove()
print(list1)
list1.remove("physics")
print(list1)

#reverse()
print(list1)
list1.reverse()
print(list1)

#sort()
print(list1)
list1.sort()
print(list1)
