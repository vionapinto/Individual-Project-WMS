import psycopg2

from data import personnel
from data import stock
#-----------------------------------------
# Code written with Piet:
# def get_employee_sql(employees,head_of = None):
#     for employee in employees:
#         print(f"({employee['user_name']}, {employee['password']}),")

# print("INSERT INTO Employee (user_name, password) VALUES")
# get_employee_sql(personnel)
#------------------------------------------

conn = psycopg2.connect(
    host = 'localhost',
    database = 'warehouse',
    user = 'postgres',
    password = '1234'
)

cur = conn.cursor()

cur.execute("INSERT INTO warehouse(name) VALUES ('Warehouse 1'), ('Warehouse 2'), ('Warehouse 3'), ('Warehouse 4');")

items_to_insert = []

for item in stock:
    items_to_insert.append(
        (
        item.get('state'),
        item.get('category'),
        item.get('warehouse'),
        item.get('date_of_stock')
        )
    )

cur.executemany(
    "INSERT INTO item(state, category, warehouse_id, date_of_stock) VALUES (%s, %s, %s, %s);", items_to_insert)

def transform_personnel(lst, head=None):
    flattened = []
    for el in lst:
        if "head_of" in el:
            flattened.append(
                (el['user_name'], el['password'], head)
            )
            flattened.extend(transform_personnel(el["head_of"], el['user_name']))
        else:
            flattened.append(
                (el['user_name'], el['password'], head)
            )
    return flattened

transformed_personnel = transform_personnel(personnel)

cur.executemany("INSERT INTO employee(user_name, password, lead_by) VALUES (%s, crypt(%s, gen_salt('bf')), %s)", transformed_personnel)

conn.commit()
cur.close()
conn.close()
