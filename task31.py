nums = []

for i in range(10):
    enter_num = int(input(f"{i+1}-sonni kiriting: "))
    nums.append(enter_num)

# Eng ko‘p takrorlangan elementni topish
max_soni = 0
eng_kop_son = None

for num in nums:
    takror_soni = nums.count(num)
    if takror_soni > max_soni:
        max_soni = takror_soni
        eng_kop_son = num

print("Eng kop takrorlangan son:", eng_kop_son)
