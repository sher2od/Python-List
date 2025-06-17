text = []
new_text = []
for i in range(5):
    enter_text = input("soz >> ")
    text.append(enter_text)

for k in text:
    if len(k) > 5:
        new_text.append(k)

print(new_text)
