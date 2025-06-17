text = []

text3 = []       # <= 3 harfli
text4_6 = []     # 4-6 harfli
text_gt6 = []    # > 6 harfli

for i in range(5):
    enter_text = input(f"{i + 1} - sozni kiriting: ")
    text.append(enter_text)

for k in text:
    if len(k) <= 3:
        text3.append(k)
    elif 4 <= len(k) <= 6:
        text4_6.append(k)
    else:
        text_gt6.append(k)

print("<= 3 harfli sozlar:", text3)
print("4-6 harfli sozlar:", text4_6)
print("> 6 harfli sozlar:", text_gt6)

        
    




