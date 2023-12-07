from dbObjects import Client, Employee, Material


#Реализация абстрактной фабрики

class Creator:
    """Интерфейс для фабричных методов"""
    def create_obj(self): pass


class ClientCreator(Creator):
    """Фабричныый метод для класса Client"""
    obj = None

    def create_obj(self, *args):
        self.obj = Client(*args)
        return self.obj


class EmployeeCreator(Creator):
    """Фабричныый метод для класса Employee"""
    obj = None

    def create_obj(self, *args):
        self.obj = Employee(*args)
        return self.obj


class MaterialCreator(Creator):
    """Фабричныый метод для класса Material"""
    obj = None

    def create_obj(self, *args):
        self.obj = Material(*args)
        return self.obj


# Реализация Прокси

class ICreator:
    """Интерфейс для DbObjectsCreator и его заместителя"""
    def create(self, obj_type, *args):
        pass


class DbObjectsCreator(ICreator):
    """Делегирует создание объектов соответствующиим фабрикам"""
    creators = None

    def __init__(self):
        """Словарь, ключи - типы создаваемых объектов, значения - классы (фабрики), используемые для их создания"""
        self.creators = {
            "Client": ClientCreator,
            "Employee": EmployeeCreator,
            "Material": MaterialCreator
        }

    def create(self, obj_type, *args):
        """Возвращает метод создания объекта определённого класса в зависимости от obj_type"""
        return self.creators[obj_type]().create_obj(*args)


class ProxyDbObjectsCreator(ICreator):
    """Заместитель DbObjectsCreator"""
    creators = None

    def __init__(self, real_creator):
        self.creators = ["Client", "Employee", "Material" ] #список допустимых типов объектов
        self.real_creator = real_creator #создание экземпляра реального класса

    def create(self, obj_type, *args):
        """Возвращает метод создания объекта настоящего класса DbObjectsCreator"""
        if obj_type in self.creators:
            self.logging(obj_type)
            return self.real_creator.create(obj_type, *args)
        else:
            print("Указан неверный тип создаваемого объекта")

    def logging(self, obj_type):
        """Записывает логи создания объектов"""
        print(f"Создан объект класса {obj_type}")
