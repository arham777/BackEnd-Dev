
#mutable
# 1 append => adds data to end of the list

fruits = ["Pineapple", "Banana", "Apple", "Melon"]
fruits.append("Kiwi")
print(fruits)

# 2 insert => add data to index

fruits.insert(0, "Orange")
print(fruits)

# 3 remove => remove data from first occurrence within the list

fruits.remove("Melon")
print(fruits)

# 4 pop = get the element at the index and remove from the list

fruits.pop(2)
print(fruits)

# remove the last value from list
fruits.pop()
print(fruits)
