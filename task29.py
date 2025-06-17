
nums = [1, 2, 2, 3, 4, 1, 5, 6, 3, 7]

unique_nums = []
for num in nums:
    if nums.count(num) == 1:
        unique_nums.append(num)

print(unique_nums)


# TODO user tomonidan kiritish

# nums = []

# for i in range(10):
#     element = int(input(f"{i + 1} - element "))
#     nums.append(element)


# unique_nums = []
# for num in nums:
#     if nums.count(num) == 1:
#         unique_nums.append(num)

# print(unique_nums)


