# OOP Concepts

## Topics covered

Classes, objects, properties and methods, encapsulation and inheritance.

## Goal achieved

By the end of the exercise you will have upgraded your query command line tool to use a more complex data set and perform additional operations.

More specifically, you will add the following features:

-

## Data

This time, the data that you will use to write your query tool will be a list of objects instead of a list of dictionaries.

The exercise includes a small module to transform the original dictionaries in the `data.py` file into objects that are stored in memory.

Besides the type conversion, the data will also be structured slightly different. The `stock` will be a list of warehouses instead of items. Each warehouse will be an object with a property `stock` that is a list of item objects.

Copy the file [sample/loader.py](sample/loader.py) into `cli/loader.py` in your project.

## Description

As usual, you will start with the traditional refactoring, this time into classes and the new stock data structure. This process can be a little more complex than the one you did with functions. It involves various steps:

1. Analyze and decide which classes are required.
1. Implement the classes in Python.
1. Transform the original dictionary-based data set into the new class-based data set.
1. Refactor the original `query.py` file to accommodate the new class-based data structure.

An experienced developer will require some time to do all of this, and you may chose to do so as well, but the exercise provides you with a solution for the first and third steps that will help you concentrate on the most important parts of the topics covered.

### 1. Classes

You will define classes for the two main data domains of the tool: stock and personnel.

You should certainly consider a class `Item`, but you can also consider a class `Warehouse`. This class can be useful, as it will allow to add methods such as `add_item`, `remove_item` or `search` and properties such as `stock`, `capacity` or `location`. Not all will be implemented now, but this will give you more flexibility in the future.

For the users, you should also consider a class `Employee`, but since the tool can also be used by guests, you may need to define a more general `User` class. They have quite a few differences, but **an employee is a type of user**.

You can use any approach you like, but if you are uncertain on how to do it you may want to read the following guidelines:

#### Stock

##### Warehouse

| Property   | Type | Default |
|------------|------|---------|
| id         | int  | None    |
| stock      | list | []      |

Both properties need to be properties of the object, not just the class. Otherwise, the stock would be shared among all warehouses and the desired solution this time is to have each Warehouse manage its own stock (after all, an item cannot be in two warehouses at the same time).

| Method     | Input                    | Output |
|------------|--------------------------|--------|
| \_\_init__ | **warehouse_id**: int    | None   |
| occupancy  | None                     | int    |
| add_item   | **item**: \<Item>        | None   |
| search     | **search_term**: str     | list   |

The constructor method will have an input argument that will be the id of the warehouse as an integer, and it will store this value in the object's `id` property. It does not require a `stock` argument because the stock will be managed with the `add_item` method. Instead, it must simply initialize the `stock` attribute as an empty list.

The `occupancy` method will not take any argument and will return an integer representing the number of items in stock.

The `add_item` method will take an instance of `Item` as an argument. This method should simply add the given object to the `stock` property.

The `search` method will search the items in the current warehouse and will return the list of matching items according to the `search_term` passed.

Once this class is done, you should write the `Item` class, which is being used by the `Warehouse` class you just wrote.

##### Item

| Property      | Type         | Default |
|---------------|--------------|---------|
| state         | str          | None    |
| category      | str          | None    |
| date_of_stock | datetime     | None    |

Each one of these properties will be supplied to the constructor method below at the moment of instantiating the objects.

In the original data, each item has an attribute `warehouse` as well. This attribute will be received as an argument of the constructor method below, but you will not store it as a property of the object.

The items will be stored in the `stock` property of each `Warehouse` object, so the item does not need this information for now.

| Method     | Input                                                                                    | Output |
|------------|------------------------------------------------------------------------------------------|--------|
| \_\_init__ | **state**: str, **category**: str, **warehouse**: int, **date_of_stock**: datetime | None   |
| \_\_str__  | None                                                                                     | str    |

The constructor method will receive all those arguments, and should store them all as object properties, except the warehouse.

The `__str__` method is used to return a string representation of the object. This method is called automatically when we use the object as a string (ex: `print(item)` or `print(f"Item: {item}")`).

This method must return the concatenation of the properties `state` and `category`.

#### Personnel

##### User

| Property         | Type | Default     |
|------------------|------|-------------|
| _name            | str  | "Anonymous" |
| is_authenticated | bool | False       |

The `_name` property will be a protected property (thus, the underscore). If the user provides an empty string as their name, their name should be "Anonymous".

The `is_authenticated` property will be set to `False` and it will not change for the standard users, but it will still be defined as a property to make the main code simpler (here, you will check `is_authenticated` without having to check first if it is an employee or a guest).

| Method       | Input              | Output |
|--------------|--------------------|--------|
| \_\_init__   | **user_name**: str | None   |
| authenticate | **password**: str  | False  |
| is_named     | **name**: str      | bool   |
| greet        | None               | None   |
| bye          | **actions**: list  | None   |

The constructor method takes an argument named `user_name` and it will store this value in the `_name` object property.

The `authenticate` method will always return `False`. Like `is_authenticated`, this method is just a placeholder for the feature and to allow us to have a simpler code in `query.py`. The `Employee` class will override this method.

The `is_named` method will return `True` if the name passed to the method equals the `self._name` property. Since `_name` is protected we will need a way to check if the user is the one we want.

The `greet` method will print a welcoming message to the user. The message for this user object will be:

```
Hello, {name of the user}!
Welcome to our Warehouse Database.
If you don't find what you are looking for,
please ask one of our staff members to assist you.
```

The `bye` method will print a *thank you* message. To minimize speculations on how the system handles the log data, it has been decided that the guest user will not be shown the summary of its actions.

##### Employee

The `Employee` class will extend the `User` class, so it will have its same properties and methods, plus the following ones:

| Property   | Type              | Default |
|------------|-------------------|---------|
| __password | str               | None    |
| head_of    | list(\<Employee>) | []      |

The `__password` property is private and should not be used anywhere other that this class' methods.

The `head_of` property stores a list of `Employee` objects, by default it is an empty list.

| Method       | Input                                                               | Output |
|--------------|---------------------------------------------------------------------|--------|
| \_\_init__   | **user_name**: str, **password**: str, **head_of**: list (optional) | None   |
| authenticate | **password**: str                                                   | bool   |
| order        | **item**: \<Item>, **amount**: int                                  | None   |
| greet        | None                                                                | None   |
| bye          | **actions**: list                                                   | None   |

The constructor method will need to be overwritten. This time, you should make sure that the object is instantiated with both a `user_name` and `password` arguments. These arguments are compulsory.

The argument `head_of` is a list of dictionaries and is optional. If there is such argument, the constructor should save it in the `head_of` property as a list of `Employee` objects and not a dictionary.

The `authenticate` method will also be overwritten, because in this case we need to check if the password is valid. The method will return `True` if the argument `password` matches the property `__password` of the object.

The `order` method will print the name of the item and amount ordered by the user when they place an order.

The `greet` method will also print a message, but the message to employees will be different:

```
Hello, {name of the user}!
If you experience a problem with the system,
please contact technical support.
```

The `bye` method will also print a *thank you* message but, additionally, it will print the summary of actions taken during the session. This method should call the parent method to print the message defined there and then print the list of actions. It should not redefine the `Thank you for your visit, {name}!` message.

### 2. Implementing the classes

Create a file named `classes.py` to define your classes. If you are following these guidelines and you want to use the [Loader class supplied](sample/loader.py), name the classes and methods as indicated on section [1. Classes](#1-classes).

From now on, we recommend you to split the task in two. It may be easier to finish the job if you concentrate first on implementing and refactoring all the classes and features related to the stock, for instance, rather than implementing everything, then changing all the data and then refactoring the main script.

You should start implementing the classes related to the stock: `Warehouse` and `Item`. Before you try them on your query tool, you may want to use the Python console to do explicit tests of your classes with hard-coded data. For instance:

```
(env) $ python3
>>> from classes import Warehouse
>>> one = Warehouse(1)
>>> two = Warehouse(2)
>>> one.add_item("anything goes")
>>> print(one.occupancy())
1
>>> print(two.occupancy())
0
```

Once you have done that, try [loading the data](#3-loading-the-data) and then [refactor your main script](#4-refactoring) to use this new data set.

When the stock related features work as they are expected, then come back here and implement the classes `User` and `Employee` and follow the same steps.

### 3. Loading the data

The import instruction you used so far to load the data:

```
from data import personnel, stock
```

Will be equivalent to:

```
from loader import Loader


personnel = Loader(model="personnel")
stock = Loader(model="stock")
```

If you are working on the stock first, leave the initial import as it was and only use the loader for the model `"stock"`. This way, the `personnel` list will still be the original one and it will be easier to focus on the task at hand.

```
from data import personnel
from loader import Loader


stock = Loader(model="stock")
```

The variable names `personnel` and `stock` will be class instances, instead of lists, but they are iterable objects and you can treat them as lists to, for instance, iterate the contents:

```
for employee in personnel:
    print(employee)
```

Or print the amount of warehouses:

```
print(len(list(stock)))
```

### 4. Refactoring

The first step is to load the new data sets using the [Loader class](sample/loader.py) that you should have copied into your `cli` directory.

If you are only doing the stock first, load only the stock as indicated previously:

```
from data import personnel
from loader import Loader


stock = Loader(model="stock")
```

It is best if, before executing the script to see which error appears, you give first a look at your code and try to identify which changes you need to apply. Some general things we know before-hand are:

- The stock is now a list of warehouses. You will have to iterate first each warehouse and then their respective `stock` list to perform operations such as listing or searching items.

- The warehouses have the methods `occupancy()` and `search()`, use them when you can.

- Dictionaries use the square-bracket notation while objects use the dot notation. Since the data we use now are objects you will have to change all the references to the properties of the items and employees.

    > You will see this will make some parts of the code more readable as you transform notations like `categories[item["category"]]` into `categories[item.category]`.

- The users will receive a different greeting depending on whether they are guest users or employees. This means that, once the user enters the name, the program should search into the personnel tree to find if there is such a user. If not, then it should create a new instance of the User class with the given name.

    > It may be more effective to store the user object in the global scope rather than the `user_name` and `is_authenticated` properties separately.

- The properties `_name` and `__password` of the user object should not be used in your main script. Use `is_authenticated`, `authenticate()` and `is_named()` instead.
