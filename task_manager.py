# Менеджер задач
# Задача: Создай класс Task, который позволяет управлять задачами (делами).
# У задачи должны быть атрибуты: описание задачи, срок выполнения и статус (выполнено/не выполнено).
# Реализуй функцию для добавления задач, отметки выполненных задач и вывода списка текущих (не выполненных) задач.


class Task:
    def __init__(self, description, deadline, completed=False):
        self.description = description
        self.deadline = deadline
        self.completed = completed

    def mark_as_done(self):
        self.completed = True


task_list = []


def active_tasks():
    for index, task in enumerate(task_list):
        if task.completed == False:
            print("------------------------------")
            print("Список невыполненных задач:")
            print(f"Задача No {index}:")
            print(f"Описание задачи: {task.description}")
            print(f"Срок выполнения: {task.deadline}")
            print(f"Выполнено: {task.completed}")
            print("------------------------------")


print("Управление задачами. Выберите действие")
print("1. Добавить задачу")
print("2. Отметить задачу как выполненную")
print("3. Вывести список невыполненных задач")
print("4. Выход")

while True:
    input_value = input("Введите номер действия: ")
    if input_value == "1":
        description = input("Введите описание задачи: ")
        deadline = input("Введите срок выполнения задачи: ")
        task = Task(description, deadline)
        task_list.append(task)
    elif input_value == "2":
        active_tasks()
        input_value = input("Введите номер задачи: ")
        for index, task in enumerate(task_list):
            if index == int(input_value):
                task.mark_as_done()
    elif input_value == "3":
        active_tasks()
    elif input_value == "4":
        break
    else:
        print("Неверное действие")
