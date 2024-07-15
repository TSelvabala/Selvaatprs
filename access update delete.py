list1=['tamil','english',2004,1998]
list2=[1,2,3,4,5]
print("list1[0]",list1[0])
print("list2[1:5]",list2[1:5])
print("value available at index 3:",list1[3])
list1[3]=1995
print("new value available at index 3:",list1[3])
print(list1)
del list1[0]
print("after deleting value at index 0:",list1)
print(list2)
del list2[1]
print("after deleting value at index 1:",list2)


