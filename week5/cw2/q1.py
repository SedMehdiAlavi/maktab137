contacts = {}

while True:
    command = input("add: 1 | remove: 2 | show all: 3 | exit: 4 ")
    if command == "1":
        name = input("Enter name: ")

        if name not in contacts:
            number = input("Enter number: ")
            contacts.update({name: number})
            print("New contact added.")
        else:
            print("Contact already exists.")

    elif command == "2":
        name = input("Enter name: ")
        if name in contacts:
            del contacts[name]
            print("Contact removed.")
        else:
            print("No such contact")

    elif command == "3":
        sorted_contacts = sorted(contacts.items())
        print(sorted_contacts)

    elif command == "4":

        break