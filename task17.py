names = []

while True:
    name = input("ism kiritganizdan stop deb yozing : ")
    if name.lower() == 'stop':
        break
    names.append(name)

print("Ismlar soni:", len(names))
