list1 = [1, 2, "hung"]*4
list2 = list(range(1,10))

print(list1)
print(list2)

list2.reverse()
list2.pop(1)
number_of_1 = list2.count(1)
print(list2)
print("The number of 1 in list is %r" % number_of_1)

print("example of using object of primitive data type in Python\n")
result = (100).__add__(20)
print(result)