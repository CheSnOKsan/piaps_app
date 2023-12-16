
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
    def __init__(self, id, name, contact_information, position, worked_hours):
        self.id = id
        self.name = name
        self.contact_information = contact_information
        # ссылка на объект, хранящий информацию о должности
        self.position = position
        self.current_state = EmpAtWork()
        self.worked_hours = worked_hours

    def change_state(self, state):
        """Изменяет состояние объекта"""
        self.current_state.switch_state(state)

    def get_salary(self):
        '''Считает итоговую зарплату'''
        return self.position.count_salary(self.worked_hours)



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


#Паттерн Легковес (Приспособленец)

class Position():
    '''Класс - легковес, хранит информацию о должностях в салоне (внутреннее состояние)'''
    def __init__(self, name, rate, description):
        self.name = name
        self.rate = rate
        self.description = description

    def count_salary(self, worked_hours):
        '''Считает итоговую зарплату'''
        return self.rate * worked_hours

class PositionFactory():
    ''' Фабрика легковесов - решает, когда нужно создать новый легковес, а когда можно обойтись существующим.'''
    positions = {}
    def get_Position(self, name, rate, description):
        if name in self.positions.keys():
            # Если такая должность уже существует, веернуть её
            print(f'Возвращена существующая должность {name}')
            return self.positions[name]
        else:
            # Если такой должности нет, создать и запомнить
            position = Position(name, rate, description)
            self.positions[name] = position
            print(f'Создана должность {name}')
            return self.positions[name]



if __name__ == '__main__':

    import database
    import dbObjCreators

    db = database.Database()

    creator = dbObjCreators.DbObjectsCreator()
    proxy_creator = dbObjCreators.ProxyDbObjectsCreator(creator)

    pos_factory = PositionFactory()

    watchman = pos_factory.get_Position('вахтёр', 200, 'наблюдает за входом в салон')
    hairdresser = pos_factory.get_Position('парикмахер', 400, 'стрижёт людей')
    watchman = pos_factory.get_Position('вахтёр', 200, 'наблюдает за входом в салон')

    emp1 = proxy_creator.create('Employee', 1, 'Галина Николаевна', '666', watchman, 10)
    emp2 = proxy_creator.create('Employee', 1, 'Галина Николаевна', '666', watchman, 5)
    emp33 = proxy_creator.create('Employee', 1, 'Зинаида Г.', '88005556666', hairdresser, 10)

    print(emp1.get_salary())
    print(emp2.get_salary())
    print(emp33.get_salary())


