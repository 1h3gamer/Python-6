#different types of sets
#set of integers
my_set = {1,2,3}
print(my_set)

#set of mixed datatypes
my_set = {1.0,"hello",(1,2,3)}
print(my_set)

#sets cannot have duplicates
my_set = {1,2,3,4,2,3}
print(my_set)

#we can make sts from a list
my_set = set([1,2,3,2])
print(my_set)

#remove a number from a set
num_set = set([0,1,3,4,5])
print("Original set")
print(num_set)
num_set.pop()
print("Set after removing the first element")
print(num_set)