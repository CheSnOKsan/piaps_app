
class DbObject(object):
    """Класс объектов, хранящихся в БД"""

    def set_mediator(self, med):
        """Добавление ссылки на посредник"""
        self.mediator = med

    def add_to_db(self):
        """Добавление объекта в БД"""
        self.mediator.notify(self, 'Добавить')

    def remove_from_db(self):
        """Удаление объекта из БД"""
        self.mediator.notify(self, 'Удалить')


class Client(DbObject):
    """Класс для хранения информации о клиенте"""
    def __init__(self, id, name, contact_information):
        self.id = id
        self.name = name
        self.contact_information = contact_information


class Employee(DbObject):
    """Класс для хранения информации о сотруднике"""
    def __init__(self, id, name, contact_information, position):
        self.id = id
        self.name = name
        self.contact_information = contact_information
        self.position = position
        self.current_state = EmpAtWork()

    def change_state(self, state):
        """Изменяет состояние объекта"""
        self.current_state.switch_state(state)



class Material(DbObject):
    """Класс для хранения информации о материале/товаре"""
    def __init__(self, id, name, supplier_information, price, quantity):
        self.id = id
        self.name = name
        self.supplier_information = supplier_information
        self.price = price
        self.quantity = quantity


# Паттерн состояние
class EmpState:
    """Состояние работника"""

    name = 'some_state' #название текущего состояния
    allowed = []#состояния, в которые возможен переход

    def get_state(self, employee):
        pass

    def switch_state(self, state):
        """Изменяет состояние (класс) объекта"""
        if state.name in self.allowed:
            print(f"Класс объекта изменён с {self.name} на {state.name}")
            self.__class__ = state
        else:
            print(f"Изменить класс {self.name} на {state.name} невозможно")


class EmpAtWork(EmpState):
    """Работник может выйти на работу"""

    name = 'at_work'
    allowed = ['on_vacation', 'dismissed']


class EmpOnVacation(EmpState):
    """Работник в отпуске"""

    name = 'on_vacation'
    allowed = ['at_work', 'dismissed']


class EmpDismissed(EmpState):
    """Работник уволен"""

    name = 'dismissed'
    allowed = ['at_work']