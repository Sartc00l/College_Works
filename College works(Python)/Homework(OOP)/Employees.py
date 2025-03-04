class Employee:
    def __init__(self, name, employee_id, salary):
        self.name = name  # Имя сотрудника
        self.employee_id = employee_id  # Идентификатор сотрудника
        self.salary = salary  # Зарплата

    def Work(self):
        print(f"{self.name} (ID: {self.employee_id}) выполняет свои обязанности.")

    def Take_break(self):
        print(f"{self.name} (ID: {self.employee_id}) взял перерыв.")

    def Get_salary(self):
        print(f"{self.name} (ID: {self.employee_id}) получает зарплату: {self.salary} тенге")


class Manager(Employee):
    def __init__(self, name, employee_id, salary, team_size):
        super().__init__(name, employee_id, salary)
        self.team_size = team_size  # Размер команды

    def Manage_team(self):
        print(f"{self.name} (ID: {self.employee_id}) управляет командой из {self.team_size} человек.")

    def Work(self):
        print(f"{self.name} (ID: {self.employee_id}) координирует работу команды.")


class Developer(Employee):
    def __init__(self, name, employee_id, salary, programming_language):
        super().__init__(name, employee_id, salary)
        self.programming_language = programming_language  

    def Write_code(self):
        print(f"{self.name} (ID: {self.employee_id}) пишет код на {self.programming_language}.")

    def Work(self):
        print(f"{self.name} (ID: {self.employee_id}) разрабатывает програмульки")


class Leader(Employee):
    def __init__(self, name, employee_id, salary, department):
        super().__init__(name, employee_id, salary)
        self.department = department  # Отдел

    def Make_decisions(self):
        print(f"{self.name} (ID: {self.employee_id}) принимает важные штучки для отдела {self.department}.")

    def Work(self):
        print(f"{self.name} (ID: {self.employee_id}) руководит отделом {self.department}.")


# Основная программа
if __name__ == "__main__":
    manager = Manager("Менджер Менеджеров", 101, 80000, 5)
    developer = Developer("Бедолага Бедолагин", 102, 2, "C#")
    leader = Leader("Лидер Лидеров", 103, 150000, "Разработка")

    # Демонстрация методов
    manager.Work()
    manager.Manage_team()
    manager.Take_break()
    manager.Get_salary()
    print()

    developer.Work()
    developer.Write_code()
    developer.Take_break()
    developer.Get_salary()
    print()

    leader.Work()
    leader.Make_decisions()
    leader.Take_break()
    leader.Get_salary()