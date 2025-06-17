
text = []

for i in range(5):
    text_enter = input(f"{i + 1} - soz > ")
    if text_enter[::-1] == text_enter:
        text.append(text_enter)
    
print(text)