import dbObjects


class Database(object):
    _instance = None

    def __new__(cls):
        """Реализация  паттерна Singleton"""
        if cls._instance is None:
            cls._instance = super(Database, cls).__new__(cls)
            cls.client_list = []
            cls.personnel_list = []
            cls.list_of_materials = []
        return cls._instance

    def set_mediator(self, med):
        """Добавление ссылки на посредник"""
        self.mediator = med

    def add_object(self, obj):
        if isinstance(obj, dbObjects.Client):
            """Добавление нового клиента в список клиентов"""
            self.client_list.append(obj)
        if isinstance(obj, dbObjects.Employee):
            """Добавление нового работника в список работников"""
            self.personnel_list.append(obj)
        if isinstance(obj, dbObjects.Material):
            """Добавление нового материала в список материалов"""
            self.list_of_materials.append(obj)

    def remove_object(self, obj):
        if isinstance(obj, dbObjects.Client):
            """Удаление клиента из списка клиентов"""
            self.client_list.remove(obj)
        if isinstance(obj, dbObjects.Employee):
            """Удаление работника из списка работников"""
            self.personnel_list.remove(obj)
        if isinstance(obj, dbObjects.Material):
            """Удаление материала из списка материалов"""
            self.list_of_materials.remove(obj)


# Паттерн стратегия
class ISort:
    '''Интерфейс для стратегий'''
    def sort_db(self):
        pass


class ClientSort(ISort):
    '''Стратегия для сортировки клиентов по имени'''
    def sort_db(self, database: Database):
        database.client_list.sort(key = lambda x: x.name)

class EmployeeSort(ISort):
    '''Стратегия для сортировки работников по имени'''
    def sort_db(self, database: Database):
        database.personnel_list.sort(key = lambda x: x.name)


class MaterialSort(ISort):
    '''Стратегия для сортировки материалов по имени'''
    def sort_db(self, database: Database):
        database.list_of_materials.sort(key = lambda x: x.name)


class ContextSort:
    '''Объект-контекст, делегирует выполнение алгоритма конкретным стратегиям'''
    def __init__(self, strategy: ISort):
        self.strategy = strategy

    def set_strategy(self, strategy: ISort):
        self.strategy = strategy

    def execute_sort_db(self, database):
        return self.strategy.sort_db(database)


