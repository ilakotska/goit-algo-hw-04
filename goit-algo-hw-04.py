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
