"""
Day - 6

Sets
"""

#* creating an empty set
empty_set = set()

#* creating a set with elements
fruits = {"apple", "banana", "cherry"}

# print(fruits)

# exit()














#* sets do not allow duplicates
fruits = {"apple", "banana", "cherry", "apple"}
# print(fruits)

# exit()














#* adding an element to a set
fruits.add("orange")
# print(fruits)

# exit()














#* adding multiple elements using update()
fruits.update(["mango", "grape"])
# print(fruits)

# exit()














#* removing an element using remove()
fruits.remove("banana")
# print(fruits)

# exit()














#* removing an element using discard() (no error if element doesn't exist)
fruits.discard("something")
# print(fruits)

# exit()














#* using pop() to remove and return a random element
removed_fruit = fruits.pop()
# print(fruits)
# print(f"Removed fruit: {removed_fruit}")

# exit()














#* clear() method to remove all elements
fruits.clear()
# print(fruits)

# exit()














#* union of two sets (all unique elements from both sets)
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1.union(set2)
# print(union_set)

# exit()














#* intersection of two sets (common elements)
intersection_set = set1.intersection(set2)
# print(intersection_set)

# exit()














#* difference of two sets (elements in set1 but not in set2)
difference_set = set2.difference(set1)
# print(difference_set)

# exit()














#* checking if a set is a subset of another set
is_subset = {1, 2}.issubset(set1) # set1 = {1, 2, 3}
# print(is_subset)

# exit()














#* checking if a set is a superset of another set
is_superset = set1.issuperset({1, 2})
# print(is_superset)

# exit()














#* iterating through a set
# for fruit in {"apple", "mango", "cherry"}:
#     print(fruit)

# exit()




