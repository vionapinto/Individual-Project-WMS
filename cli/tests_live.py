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
        # classes.bla
    except AttributeError as err:
        assert False, "Wrong class naming: --> {}".format(err)
    else:
        assert True   

def test_inheritance():
    global User, Employee, Item
    employee = Employee()
    assert isinstance(employee, User)

def test_user():
    global User
    # test Anonymous user
    user = User()
    assert user._name == "Anonymous"
    user.authenticate('1234')
    assert user.is_authenticated == False
    #test user name
    user = User(user_name = 'Test')
    assert user._name == 'Test'
    # test user with password
    user = User(user_name = 'Test')
    user.authenticate('1234')
    assert user._name == 'Test'
    assert user.is_authenticated == False

def test_employee():
    global Employee
    # test employee without name and password
    employee = Employee()
    assert employee.is_authenticated == False
    assert employee.head_of is None
    # test named employee with a password
    employee = Employee(user_name='Test', password='1234')
    employee.authenticate('1234')
    assert employee.is_authenticated
    assert not employee.head_of 
    # assert employee.head_of == []
    # assert len(employee.head_of) == 0
    employee = Employee(user_name='Test', password='1234', head_of=[{'user_name': 'test2', 'password': '4321'}])
    for other in employee.head_of:
        assert isinstance(other, Employee)


def test_warehouse():
    global Warehouse, Item
    warehouse = Warehouse()
    assert warehouse.id == None
    # assert not warehouse.id
    warehouse = Warehouse(warehouse_id = 1)
    assert warehouse.id == 1
    assert type(warehouse.stock )== list
    assert warehouse.stock == []
    assert warehouse.occupancy() == 0
    assert warehouse.occupancy() == len(warehouse.stock)
    item = Item(state='New', category="Tablet")
    warehouse.add_item(item)
    assert warehouse.occupancy() == 1
    assert warehouse.occupancy() == len(warehouse.stock)
    assert warehouse.stock != []
    item = Item(state='Old', category="Tablet")
    warehouse.add_item(item)
    warehouse.add_item(item)
    result = warehouse.search('old tablet')
    assert len(result['1']) == 2

def test_item():
    global Item
    # test item with state, category and date_of_stock
    item = Item(state='New', category='Tablet', date_of_stock='2020-01-01')
    assert item.state == 'New'
    assert item.category == 'Tablet'
    assert item.date_of_stock == '2020-01-01'
    assert str(item) == f"{item.state} {item.category.lower()}"

class mock_input:
    def __init__(self, mocked_input) -> None:
        self.mocked_input = mocked_input
        print(__builtins__["input"])
        self.original_input = __builtins__["input"] #function object

    def __enter__(self):
        __builtins__['input'] = lambda a: self.mocked_input # replace builtin input func
        print(__builtins__["input"])
        

    def __exit__(self, exc_type, exc_value, traceback):
        __builtins__['input'] = self.original_input

class mock_output:
    def __init__(self, output) -> None:
        self.original_print = __builtins__["print"]
        self.output = output

    def __enter__(self):
        __builtins__['print'] = lambda *values: [self.output.append(val) for val in values] 

    def __exit__(self, exc_type, exc_value, traceback):
        __builtins__['print'] = self.original_print

from query import get_person_entity

def test_get_person_entity():
    global User, Employee
    # User not in the employee list
    with mock_input('Testname'):
        user = get_person_entity()
        assert user._name == 'Testname'
        assert isinstance(user, User)
        assert not isinstance(user, Employee)

    with mock_input('Jeremy'):
        employee = get_person_entity()
        assert employee._name == 'Jeremy'
        assert isinstance(employee, User)
        assert isinstance(employee, Employee)

from query import selection

def test_selection():
    with mock_input(1):
        output = []
        with mock_output(output):
            assert selection() == 1
            assert output == ['1: List all items', '2: Search and place order', '3: Browse by category', '4: Quit']

from query import list_items_by_warehouse

def test_list_items_by_warehouse():
    output = []
    with mock_output(output):
        total = list_items_by_warehouse()
        assert total == "Listed 5000 items"
        assert output.pop() == 1223
        assert output.pop() == "Total items in warehouse 4:"
        assert output.pop() == 1173
        assert output.pop() == "Total items in warehouse 3:"
        assert output.pop() == 1258
        assert output.pop() == "Total items in warehouse 2:"
        assert output.pop() == 1346
        assert output.pop() == "Total items in warehouse 1:"

from query import search_and_order_item
def test_search_and_order_item():
    with mock_input('Cheap tablet'):
        assert search_and_order_item() == "Searched for Cheap tablet"


from query import STATE, place_order
def test_employees_only():
    with mock_input("Jeremy"):
        STATE['USER'] = get_person_entity()
        STATE['USER'].authenticate('coppers')
    with mock_input('1'):
        output = []
        with mock_output(output):
            result = place_order('cheap tablet', 99)
    assert output.pop() == 'Order placed for 1 cheap tablet'
    assert 'placed order for 1 cheap tablet' == result

    with mock_input("Test"):
        STATE['USER'] = get_person_entity()
        STATE['USER'].authenticate('coppers')
    with mock_input('1'):
        output = []
        with mock_output(output):
            result = place_order('cheap tablet', 99)
    assert output.pop() == 'wrong password'
    assert 'Authentication failed' == result

