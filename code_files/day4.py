"""
Day - 4

Lists and Tuples
"""

#* creating an empty list
empty_list = []











#* creating a list with elements
example = [1, 2, 3, 4]












#* supports multiple data types
multi = [1, 1.2, True, "example"]












#* operations on a list - append
fruits = ["apple", "mango", "banana"]
fruits.append("banana")
# print(fruits)
# exit()












#* operations on a list - insert
fruits.insert(1, "banana")
# print(fruits)

# exit()











#* operations on a list - remove
fruits.remove("banana")
# print(fruits)

# exit()











#* operations on a list - pop
fruits.pop(2)
# print(fruits)

# exit()











#* concatenation
list1 = [1, 2]
list2 = [3, 4]
combined = list1 + list2
# print(combined)

# exit()











#* repetition
repeated = [0] * 30
# print(repeated)

# exit()











#* slicing
my_list = [1, 2, 3, 4, 5]
sliced = my_list[1:3] 
# print(sliced)

# exit()











#* iterating a list using an index
# for i in range(len(my_list)):
#   print(my_list[i])

# exit()











#* iterating without an index
# for item in my_list:
#   print(item)

# print(my_list)
my_list[0] = 6
# print(my_list)

# exit()











#* creating empty tuple
empty_tuple = ()












#* creating tuple with multiple elements
example_tuple = (1, 2, 3)












#* creating single element tuple
single_tuple = (1,)
# print(type(single_tuple))

# exit()










#* access by index
fruits_tuple = ('apple', 'orange', 'banana')
# print(fruits_tuple[1])











#* slicing tuples
# print(fruits_tuple[0:2])











#* concatenation
tuple1 = (1, 2)
tuple2 = (3, 4)
result = tuple1 + tuple2
# print(result)











#* repetition
repeated = (0,) * 2 
# print(repeated)












#* packing
packed = 1, 2, "apple"
# print(packed)
# print(type(packed))












#* unpacking
a, b, c = packed
# print(a, b, c)