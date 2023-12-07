class Administrator(object):

    def __init__(self, login,  password, name):
        self.login = login
        self.password = password
        self.name = name

    def log_in(self, log, pas):
        """Метод, реализущий авторизацию администратора"""
        if log == self.login and pas == self.password:
            return f'Авторизация прошла успешно, добро пожаловать, {self.name}'
        elif log == self.login and pas != self.password:
            return f'Неверный пароль, {self.name}'
        elif log != self.login:
            return f'Проверьте введённые данные'

