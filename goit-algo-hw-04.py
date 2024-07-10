#Завдання 1

def total_salary(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            salaries = []
            for line in file:
                # Розділяємо рядок на прізвище і зарплату
                name, salary = line.strip().split(',')
                # Перетворюємо зарплату на число та додаємо до списку
                salaries.append(float(salary))

        # Обчислення загальної суми зарплат
        total = sum(salaries)
        # Обчислення середньої зарплати
        average = total / len(salaries) if salaries else 0

        return total, average

    except FileNotFoundError:
        print(f"Файл за шляхом {path} не знайдено.")
        return 0, 0
    except Exception as e:
        print(f"Сталася помилка: {e}")
        return 0, 0

# Приклад використання функції
total, average = total_salary("path/to/salary_file.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")



#Завдання 2

def get_cats_info(path):
    cats_info = []
    
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()
                if line:  
                    cat_id, name, age = line.split(',')
                    cat_info = {
                        "id": cat_id,
                        "name": name,
                        "age": age
                    }
                    cats_info.append(cat_info)
                    
    except FileNotFoundError:
        print(f"Файл за шляхом {path} не знайдено.")
    except Exception as e:
        print(f"Сталася помилка: {e}")

    return cats_info

# Приклад використання функції
cats_info = get_cats_info("path/to/cats_file.txt")
print(cats_info)



# Завдання 4

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args

def add_contact(args, contacts):
    if len(args) < 2:
        return "Invalid command format. Usage: add [name] [phone]"
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def change_contact(args, contacts):
    if len(args) < 2:
        return "Invalid command format. Usage: change [name] [new_phone]"
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    else:
        return "Contact not found."

def show_phone(args, contacts):
    if len(args) < 1:
        return "Invalid command format. Usage: phone [name]"
    name = args[0]
    if name in contacts:
        return contacts[name]
    else:
        return "Contact not found."

def show_all(contacts):
    if contacts:
        return "\n".join(f"{name}: {phone}" for name, phone in contacts.items())
    else:
        return "No contacts found."

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
