

list1 = [1,2,3,4,5]
list2 = [4,5,6,7]

result = []
for element in list1:
    if element in list2:
        result.append(element)

print(result)

