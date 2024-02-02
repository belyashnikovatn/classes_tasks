class Phone:
    line_type = 'проводной'

    def __init__(self, dial_type_value) -> None:
        self.dial_type = dial_type_value
        self._serial_number = id(dial_type_value)

    def ring(self):
        print('Дзззззззинь')

    def call(self, phone_number):
        print(f'Звоню по номеру {phone_number}! Тип связи - {self.line_type}')

    def get_missed_calls(self):
        print('Запрос количества пропущенных звонков')

    def dial_type_upgrade(self, new_dial_type):
        self.dial_type = new_dial_type

    def __str__(self) -> str:
        # переопределила строковый метод
        return f'Это {self.line_type} телефон. Набор - {self.dial_type}.'


class MobilePhone(Phone):
    line_type = 'беспроводной'
    battery_type = 'Li-on'

    def __init__(self, dial_type_value, network_type) -> None:
        self.__network_type = network_type
        super().__init__(dial_type_value)

    def ring(self):
        print('Дзыньк')

    def start_game(self):
        print('Игра запущена')

    def get_info(self):
        print(f'Серийный номер = {self._serial_number}, '
              f'тип связи {self.__network_type}')


rotary_phone = Phone(dial_type_value='дисковый')
rotary_phone.ring()
rotary_phone.call('555-33-22')
rotary_phone.get_missed_calls()
rotary_phone.dial_type_upgrade('кнопочный')
print(rotary_phone.dial_type)
print(rotary_phone)

mobile_phone = MobilePhone('сенсорный', 'LTE')
mobile_phone.ring()
print(mobile_phone)
print(mobile_phone.battery_type)
# print(mobile_phone.__network_type)
mobile_phone.start_game()
mobile_phone.get_info()
# rotary_phone = Phone(dial_type_value='дисковой')
# print(f'Тип набора: {rotary_phone.line_type}')
# меняем значение атрибута объекта
# rotary_phone.dial_type = 'кнопочный'
# print(f'Тип набора: {rotary_phone.line_type}')

# print(f'Тип линии: {Phone.line_type}')
# меняем значение атрибута класса
# Phone.line_type = 'беспроводной'
# print(f'Тип линии: {Phone.line_type}')
# print('-')

# rotary_phone = Phone(dial_type_value='дисковый')
# keypad_phone = Phone(dial_type_value='кнопочный')
# print(f'Тип линии: {rotary_phone.line_type}')
# print(f'Тип линии: {keypad_phone.line_type}')
# rotary_phone.line_type = 'радио'
# print(f'Тип линии: {rotary_phone.line_type}')
# print(f'Тип линии: {keypad_phone.line_type}')
# Phone.line_type = 'спутниковый'
# Если в объекте явно задать новое значение атрибута с именем атрибута класса,
# то объект сохранит собственное значение, а не ссылку на класс.
# print(f'Тип линии: {rotary_phone.line_type}')
# Объект не хранит значение атрибута класса, а лишь ссылается на него.
# print(f'Тип линии: {keypad_phone.line_type}')

# print('----')
# rotary_phone.ring()
