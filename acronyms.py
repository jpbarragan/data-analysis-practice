def find_acronym():
    user_acronym = input("Whay acronym do you want to look up?\n")

    found = False
    try:
        with open ('acronyms.txt') as file:
            for line in file:
                if user_acronym in line:
                    print(line)
                    found = True
                    break
    except FileNotFoundError as e:
        print("File not found")
        return

    if not found:
        print("Acronym not found")

def add_acronym():
    new_acronym = input("Which acronym would you like to add to the database?\n")
    definition = input("What is the definition for " + new_acronym + "?\n")

    with open ("acronyms.txt", "a") as file:
        file.write("\n" + new_acronym + " = " + definition)

def main():
    choice = input("Do you want to find (F) or add (A) an acronym?\n")
    if choice == "F":
        find_acronym()
    elif choice == "A":
        add_acronym()

main()