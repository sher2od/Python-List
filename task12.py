my_list = ["olma", "anor", "banan", "uzum", "shaftoli", "anjir"]

open_list = []

for i in range(len(my_list)):
    if i % 2 == 0:  
        open_list.append(my_list[i])

print(open_list)
