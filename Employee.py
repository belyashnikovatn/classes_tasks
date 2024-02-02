class Employee:
    vacation_days = 28  # общий атрибут для всех типа умолчания

    # атрибуты, которые определяются во время создания объекта
    def __init__(self, first_name_value,
                 second_name_value, gender_value) -> None:
        self.first_name = first_name_value
        self.second_name = second_name_value
        self.gender = gender_value
        self.remaining_vacation_days = Employee.vacation_days
        #   очень важно EMPLOYEE.vacation_days то есть
        #   мы обращаемся к атрибуту КЛАССА

    def consume_vacation(self, vacation_days):
        self.remaining_vacation_days -= vacation_days

    def get_vacation_details(self):
        return (f'Остаток отпускных дней: {self.remaining_vacation_days}.')


class FullTimeEmployee(Employee):
    def get_unpaid_vacation(self, start_date, vacation_days):
        return (f'Начало неоплачиваемого отпуска: '
                f'{start_date}, '
                f'продолжительность: {vacation_days} дней.')


class PartTimeEmployee(Employee):
    vacation_days = 14

    def __init__(self, first_name_value, second_name_value,
                 gender_value) -> None:
        super().__init__(first_name_value, second_name_value, gender_value)
        self.remaining_vacation_days = PartTimeEmployee.vacation_days


# full_time_employee = FullTimeEmployee('Роберт', 'Крузо', 'м')
# print(full_time_employee.get_unpaid_vacation('2023-07-01', 5))
# part_time_employee = PartTimeEmployee('Алёна', 'Пятницкая', 'ж')
# print(part_time_employee.get_vacation_details())
# part_time_employee.consume_vacation(5)
# print(part_time_employee.get_vacation_details())


# employee1 = Employee('Роберт', 'Крузо', 'м')
# employee1.consume_vacation(7)
# print(employee1.get_vacation_details())

# employee2 = Employee('Диана', 'Витер', 'ж')
# print(f'Имя: {employee1.first_name}, '
#       f'Фамилия: {employee1.second_name}, '
#       f'Пол: {employee1.gender}, '
#       f'Отпускных дней в году: {employee1.vacation_days}.')
# print(f'Имя: {employee2.first_name}, '
#       f'Фамилия: {employee2.second_name}, '
#       f'Пол: {employee2.gender}, '
#       f'Отпускных дней в году: {employee2.vacation_days}.')