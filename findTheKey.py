def menu(list, question):
    for entry in list:
        print(1 + list.index(entry), ") " + entry)

    return int(input(question)) - 1


def inspect(choice,location):
    if choice == location:
        print("\nYou found a key!")
        return 1
    else:
        print("Nothing of interest here.")
        return 0

loop=1
items = ["plant","painting","vase","lampshade","shoe","door"]
keylocation = 2
keyfound = 0

while loop == 1:
    keyfound = inspect(menu(items,"What do you want to inspect?"), keylocation)
    if keyfound == 1:
        print("\nYou put the key in the lock of the door, and turn it. It opens!")
        loop = 0

print("Light floods into the room, as you open the door to your freedom.")
