import random
print("random number from range(100):",random.choice(range(100)))
list=[1,2,3,5,9]
print("random element from list:",random.choice(list))
str="Hello World"
print("random character from string:",random.choice(str))
print("random():",random.random())
print("random():",random.random())
random.seed(10)
print("random number with int seed",random.random())
list=[20,16,10,5]
random.shuffle(list)
print("Reshuffled list:",list)
print("Random Float Uniform(5,10):",random.uniform(5,10))
print("Random Float Uniform(7,14):",random.uniform(7,14))
      
