import classes
import pytest
from query import get_person_entity, selection, list_items_by_warehouse, stock, search_and_order_item


# Test the system classes

classes = __import__('classes')
User = None
Employee = None
Warehouse = None
Item = None


def test_class_naming():
    global User, Employee, Warehouse, Item
    try:
        User = classes.User
        Employee = classes.Employee
        Warehouse = classes.Warehouse
        Item = classes.Item
        # bla = classes.bla
    except AttributeError as err:
        assert False, "Wrong class naming: --> {}".format(err)
    else:
        assert True

def test_inheritance():
    global User, Employee, Warehouse, Item
    employee = Employee()
    assert isinstance(employee, User)

def test_user():
    global User
    # test Anonymous user
    user = User()
    assert user._name == "Anonymous"
    user.authenticate('1234')
    assert user.is_authenticated == False
    # test named user
    user = User(user_name='Test')
    assert user._name == "Test"
    user.authenticate('1234')
    assert user.is_authenticated == False
    # test named user with password
    user = User(user_name='Test', password='1234')
    assert user._name == "Test"
    user.authenticate('1234')
    assert user.is_authenticated == False

def test_employee():
    global Employee
    # test named employee without a password
    employee = Employee(user_name='Test', head_of=[{'user_name': 'Test2'}])
    assert employee._name == "Test"
    employee.authenticate('1234')
    assert employee.is_authenticated == False
    assert employee.head_of is None
    # test named employee with password and no head_of
    employee = Employee(user_name='Test', password='1234')
    assert employee._name == "Test"
    employee.authenticate('1234')
    assert employee.is_authenticated == True
    assert employee.head_of == []
    # test named employee with password and head_of
    employee = Employee(user_name='Test', password='1234', head_of=[{'user_name': 'Test2', 'password':'4321'}])
    assert employee._name == "Test"
    employee.authenticate('1234')
    assert employee.is_authenticated == True
    assert employee.head_of != None
    assert isinstance(employee.head_of, list)
    assert len(employee.head_of) == 1
    for other in employee.head_of:
        assert isinstance(other, Employee)

def test_warehouse():
    global Warehouse, Item
    # test warehouse without id
    warehouse = Warehouse()
    assert warehouse.id == None
    assert isinstance(warehouse.stock, list)
    assert(len(warehouse.stock) == 0)
    # test warehouse with id
    warehouse = Warehouse(warehouse_id=1)
    assert warehouse.id == 1
    assert isinstance(warehouse.stock, list)
    assert(len(warehouse.stock) == 0)
    # test add_item method
    warehouse.add_item(Item(state='New', category="Tablet"))
    assert warehouse.occupancy() == 1
    # search with with an incomplete search
    warehouse.add_item(Item(state='Old', category="Tablet"))
    assert warehouse.occupancy() == 2
    result = warehouse.search('Old')
    assert len(result['1']) == 0
    # search with a complete search
    warehouse.add_item(Item(state='Old', category="Tablet"))
    result = warehouse.search('Old Tablet')
    assert len(result['1']) == 2

def test_item():
    global Item
    # test item without warehouse
    item = Item(state='New', category="Tablet", date_of_stock='2020-01-01')
    assert item.state == 'New'
    assert item.category == 'Tablet'
    assert item.date_of_stock == '2020-01-01'
    assert str(item) == 'New tablet'



# test query script

class mock_input:
    def __init__(self, mocked_input):
        self.mock = lambda _: mocked_input
        self.original_input = __builtins__["input"]

    def __enter__(self):
        __builtins__["input"] = self.mock

    def __exit__(self, exc_type, exc_value, traceback):
        __builtins__["input"] = self.original_input



class mock_output:
    def __init__(self, print_output):
        self.mock = lambda *value: [print_output.append(val) for val in value]
        self.original_print = __builtins__["print"]

    def __enter__(self):
        __builtins__["print"] = self.mock

    def __exit__(self, exc_type, exc_value, traceback):
        __builtins__["print"] = self.original_print

    

def test_get_person_entity():
    global User, Employee
    # User not in the employer list
    with mock_input("TestName"):
        user = get_person_entity()
        assert user._name == "TestName"
        assert isinstance(user, User)

    # User in the employer list
    with mock_input("Jeremy"):
        employee = get_person_entity()
        assert employee._name == "Jeremy"
        assert isinstance(employee, User)
        assert isinstance(employee, Employee)


def test_selection():
    with mock_input("1"):
        output = []
        with mock_output(output):
            assert selection() == 1
            assert output == ['1: List all items', '2: search and place order', '3: browse by category', '4: quite']
        # print(output)
        # assert False

def test_list_items_by_warehouse():
    output = []
    with mock_output(output):
        total = list_items_by_warehouse()
        assert total == "Listed 5000 items"
        assert output.pop() == 1223 
        assert output.pop() == 'Total items in warehouse 4:'

def test_search_item():
    with mock_input("Cheap tablet"):
            total = search_and_order_item()
    assert total == "Searched for Cheap tablet"



from query import STATE, place_order
def test_employees_only():
    global Item
    with mock_input("Jeremy"):
        STATE['USER'] = get_person_entity()
        STATE['USER'].authenticate('coppers')
    item = Item(state="Cheap", category="Tablet")
    with mock_input('1'):
        output = []
        with mock_output(output):
            result = place_order(item, 99)

    print(output)
    assert False
    # assert output.pop() == 'wrong password'
    # assert result == "Authentication failed"

