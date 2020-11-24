numberNames = int(input("Please enter a number of names: "))
names = []
i = 0
while numberNames > i:
    acceptedName = str(input("Please enter a name: "))
    names.append(acceptedName)
    i = i + 1
i = 0
total = len(names)
while total > i:
    print (names.pop(0))
    i = i + 1