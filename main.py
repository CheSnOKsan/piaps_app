import dbObjects
import database
import dbObjCreators
from mediators import DBMediator


if __name__ == '__main__':
    db = database.Database()

    creator = dbObjCreators.DbObjectsCreator()
    proxy_creator = dbObjCreators.ProxyDbObjectsCreator(creator)

    pos_factory = dbObjects.PositionFactory()

    watchman = pos_factory.get_Position('вахтёр', 200, 'наблюдает за входом в салон')
    hairdresser = pos_factory.get_Position('парикмахер', 400, 'стрижёт людей')
    watchman = pos_factory.get_Position('вахтёр', 200, 'наблюдает за входом в салон')

    emp1 = proxy_creator.create('Employee', 1, 'Галина Николаевна', '666', watchman, 10)
    emp2 = proxy_creator.create('Employee', 1, 'Антонина Николаевна', '666', watchman, 5)
    emp33 = proxy_creator.create('Employee', 1, 'Зинаида Г.', '88005556666', hairdresser, 10)

    mediator = DBMediator(db, emp1)
    emp1.add_to_db()

    mediator = DBMediator(db, emp2)
    emp2.add_to_db()

    mediator = DBMediator(db, emp33)
    emp33.add_to_db()

    cl1 = proxy_creator.create('Client', 3, 'Иван', '+7 800 555 35 35')
    cl2 = proxy_creator.create('Client', 4, 'Антон', '+7 800 555 35 35')
    cl3 = proxy_creator.create('Client', 5, 'Валерия', '+7 800 555 35 35')

    mediator = DBMediator(db, cl1)
    cl1.add_to_db()

    mediator = DBMediator(db, cl2)
    cl2.add_to_db()

    mediator = DBMediator(db, cl3)
    cl3.add_to_db()
    print("До сортировки")
    print([i.name for i in db.client_list])
    print([i.name for i in db.personnel_list])

    context = database.ContextSort(database.ClientSort())
    context.execute_sort_db(db)

    context.set_strategy(database.EmployeeSort())
    context.execute_sort_db(db)

    print("После сортировки")
    print([i.name for i in db.client_list])
    print([i.name for i in db.personnel_list])



    #
    # mediator2 = DBMediator(db, emp1)
    # emp1.add_to_db()
    #
    # print(db.client_list)
    # print(db.personnel_list[0].__dict__)