import dbObjects
import database
import dbObjCreators
from mediators import DBMediator


if __name__ == '__main__':

    db = database.Database()

    creator = dbObjCreators.DbObjectsCreator()
    proxy_creator = dbObjCreators.ProxyDbObjectsCreator(creator)

    cl3 = proxy_creator.create('Client', 3, 'Иван', '+7 800 555 35 35')
    emp1 = proxy_creator.create('Employee', 1, 'Галина Николаевна', '666', 'вахтёр')

    print(emp1.current_state.name)
    emp1.change_state(dbObjects.EmpOnVacation)
    print(emp1.current_state.name)

    # cl3 = creator.create('Client', 3, 'Иван', '+7 800 555 35 35')
    # # emp1 = creator.create('Employee', 1, 'Галина Николаевна', '666', 'вахтёр')
    #
    # mediator = DBMediator(db, cl3)
    # cl3.add_to_db()
    #
    # mediator2 = DBMediator(db, emp1)
    # emp1.add_to_db()
    #
    # print(db.client_list)
    # print(db.personnel_list[0].__dict__)