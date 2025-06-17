nums = []

# 6 ta son kiritamiz
for i in range(6):
    enter_nums = int(input(f"{i + 1} - sonni kiriting: "))
    nums.append(enter_nums)

print("Kiritilgan sonlar:", nums)

# Juftliklarni tekshiramiz
print("Yig'indisi 10 ga teng bo‘lgan juftliklar:")
for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] + nums[j] == 10:
            print(f"{nums[i]} + {nums[j]} = 10")
