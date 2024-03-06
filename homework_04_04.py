def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contacts(args,contacts):
    name,phone = args
    contacts[name] = phone
    return "Contact added."

def change_contact(args, contacts):
    if args[0] in contacts.keys():
        add_contacts(args, contacts)
    else:
        return "No such name in the base"

def show_phone(args,contacts):
    return contacts[args[0]]


def show_all(args,contacts):
    list=''
    for key in contacts:
        list+=(f"{key:10} : {contacts[key]}\n")
    return list

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)
        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contacts(args,contacts))  
        elif command == "change":
            print(change_contact(args,contacts)) 
        elif command == "phone":
            print(f"His phone number is: {show_phone(args,contacts)}")
        elif command == "all":
            print(show_all(args,contacts))
        else:
            print("Invalid command.")
    
if __name__ == "__main__":
    main()