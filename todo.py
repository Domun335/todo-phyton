user_select = -1
tasks = []


def show_tasks():
    task_index = 0

    for task in tasks:
        print(task + ' [' + str(task_index) + ']')
        task_index += 1


def add_task():
    tasks.append(input("Wpisz zadanie: "))
    print("Dodano zadanie!")


def delete_task():
    task_index = int(input("Podaj index zadania do usuniecia: "))

    if task_index < 0 or task_index > len(tasks) - 1:
        print("Zadanie o tym indexie nie istnieje")
        return
    tasks.pop(task_index)
    print("Usunieto zadanie!")


def save_tasks_to_file_and_exit():
    file = open("tasks.txt", "w")

    for task in tasks:
        file.write(task + "\n")
    file.close()


def load_tasks_form_file():
    try:
        file = open("tasks.txt")

        for line in file.readlines():
            tasks.append(line.strip())
        file.close()
    except FileNotFoundError:
        return


load_tasks_form_file()
while user_select != 5:
    if user_select == 1:
        show_tasks()
    if user_select == 2:
        add_task()
    if user_select == 3:
        delete_task()
    if user_select == 4:
        save_tasks_to_file_and_exit()
        break

    print()
    print('1. Pokaż zadania')
    print('2. Dodaj zadanie')
    print('3. Usuń zadanie')
    print('4. Zapisz i wyjdź')
    print('5. Wyjdź')

    try:
        user_select = int(input('Podaj wybór: '))
    except ValueError:
        print()
        print("Podaj liczbę!")

    print()
