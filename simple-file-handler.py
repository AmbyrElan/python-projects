stored = {}

def menu():
    option = 0
    while (option != 5):
        print("Menu\n")
        print("--------------------------------\n")
        print("1. Look up an email address\n")
        print("2. Add a new name and email address\n")
        print("3. change an existing email address\n")
        print("4. Delete a name and email address\n")
        print("5. Quit the program\n")

        option = int(input("Enter your choice: "))

        if option == 1:
            stored = lookUp()
        elif option == 2:
            stored = add()
        elif option == 3:
            stored = change()
        elif option == 4:
            stored = delete()
        elif option == 5:
            print("Information saved.")
        
    

def lookUp():
    
    n = input("Enter a name: ")

    if n in stored:
        print("Name: ", n,"\n")
        print("Email: ", stored[n],"\n")
    else:
        print("The specified name was not found.\n")

def add():
    n = input("Enter a name: ")
    e = input("Enter an email address: ")

    if n in stored:
        print("That name already exists\n")
    else:
        stored[n] = e
        print("Name and email address have been added\n")
        

def change():
    n = input("Enter a name: ")
    if n in stored:
        e = input("Enter new email address: ")
        del stored[n]
        stored[n] = e
        print("Information updated\n")
    else:
        print("The specified name was not found\n")
    
def delete():

    n = input("Enter a name: ")
    if n in stored:
        del stored[n]
        print("Information deleted\n")
    else:
        print("The specified name was not found\n")

def main():
    menu()

main()
