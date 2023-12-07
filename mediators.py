import dbObjects

class IMediator():
    """Интерфейс посредника"""
    def notify(self, obj, message):
        pass


class DBMediator(IMediator):
    """Посредник для взаимодействия с БД"""
    def __init__(self, database, obj):
        self.database = database
        self.obj = obj
        database.set_mediator(self)
        obj.set_mediator(self)

    def notify(self, obj, message):
        """Приём сообщений от компонентов системы"""

        if isinstance(obj, dbObjects.DbObject):
            if message == 'Добавить':
                self.database.add_object(obj)
            if message == 'Удалить':
                self.database.remove_object(obj)

        # if isinstance(obj, database.Database):
        #     if message == 'Удалить':
        #         print('медиатор удалить')
        #         self.database.remove_object(obj)
