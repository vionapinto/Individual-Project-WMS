class Item():
    """Common attributes of any Item."""
    state = None
    category = None
    date_of_stock = None

    def __init__(self, state=None, category=None, warehouse=1, date_of_stock=None):
        """Constructor.
        Saves all item attributes as object properties,
        except the warehouse.
        """
        # We don't need the warehouse property any more,
        # because the item will be stored inside the warehouse,
        # so we only save the other data as properties of the object.
        self.state = state
        self.category = category
        self.date_of_stock = date_of_stock

    def __repr__(self):
        """Return a string representing the object."""
        if not self.state:
            return self.category
        return f"{self.state} {self.category.lower()}"

class Warehouse():

    id = None
    stock = None

    def __init__(self, warehouse_id:int=None):
        self.id = warehouse_id
        self.stock = []  # its a property with default value given as []
        
    def occupancy(self) -> int:
        return len(self.stock)

    def add_item(self, item_object):
        self.stock.append(item_object)

    def remove_item(self):
        pass

    def search(self, item_name) -> list:
        """Search an item."""
        results = []
        for item in self.stock:
            if str(item).lower() == item_name.lower():
                results.append(item)
        return {str(self.id): results}

class User():
    _name = 'Anonymous' # it is anonymous if username is blank
    is_authenticated = False # since these two are properties we don't include it in init. Default values are given to us.

    def __init__(self, *args, **kwargs):
        """Constructor."""
        if "user_name" in kwargs and kwargs["user_name"].strip():
            self._name = kwargs["user_name"]

    def authenticate(self, password=None):
        """Return False."""
        self.is_authenticated = False
        return self.is_authenticated
    
    def is_named(self, name):
        """Return True if name equals self._name."""
        return self._name == name

    def greet(self) -> None:
        """Return a greeting for the guest user."""
        print(f"Hello, {self._name}!\nWelcome to our Warehouse Database.\nIf you don't find what you are looking for,please ask one of our staff members to assist you.")

    def bye(self, actions:list) -> None:
        """Finish the session."""
        print("Thank you for your visit", self._name)

class Employee(User):

    __password = None
    head_of = None

    def __init__(self, *args, **kwargs):
        """Constructor."""
        if "user_name" not in kwargs:
            print("An employee can not be anonymous.")
            return
        if "password" not in kwargs:
            print("An employee requires a password.")
            return
        super().__init__(*args, **kwargs)
        self.__password = kwargs["password"]
        self.head_of = []
        if "head_of" in kwargs:
            self.head_of = [Employee(**employee)
                            for employee in kwargs["head_of"]]  # head_of is list of dicts

    def authenticate(self, password):
        """Authenticate the user."""
        self.is_authenticated = self.__password == password
        return self.is_authenticated

    def order(self, item, amount:int) -> int:
        """Order an item from the stock."""
        print(f"Name of the item: {item}\nAmount ordered:{amount}")

    def greet(self) -> None:
        print(f"Hello, {self._name}!\nIf you experience a problem with the system, please contact technical support.")

    def bye(self, actions):
        """Finish the session."""
        super().bye()
        print("In this session you have:")
        for num, action in enumerate(actions):
            print(f"\t{num+1}. {action}")

