import unittest
from administrator import Administrator

class TestAdministratorLogin(unittest.TestCase):

    # создание экземпляра класса
    def setUp(self):
        self.admin1 = Administrator(login='admin', password='1Qwerty_2', name='администратор Иван')

    # проверка случая введения верных данных
    def test_successful_login(self):
        self.assertEqual(self.admin1.log_in('admin', '1Qwerty_2'),
                         'Авторизация прошла успешно, добро пожаловать, администратор Иван')

    # проверка случая введения неверного пароля при верном логине
    def test_invalid_password(self):
        self.assertEqual(self.admin1.log_in('admin', 'wrong_password'), 'Неверный пароль, администратор Иван')

    # проверка случая введения неверных данных
    def test_invalid_username(self):
        self.assertEqual(self.admin1.log_in('user',  5),
                         'Проверьте введённые данные')


# if __name__ == '__main__':
#     unittest.main()