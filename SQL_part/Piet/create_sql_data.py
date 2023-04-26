from data import personnel as employees, stock

#print(employees)
sql_employee_str = ''
def get_employees_sql(employees_list, lead_by = None):
    global sql_employee_str
    for employee in employees_list:
        if lead_by:
            sql_employee_str +=(f"({employee['user_name']},{employee['password']},{lead_by}),\n")
        else:
            sql_employee_str += (f"({employee['user_name']},{employee['password']},NULL),\n")
        if "head_of" in employee:
            get_employees_sql(employee['head_of'], employee['user_name'])

print("INSERT INTO employee(user_name, password, lead_by) VALUES")

get_employees_sql(employees)
sql_employee_str = sql_employee_str[:-2] + ';'
print(sql_employee_str)

warehouses = set([item['warehouse'] for item in stock])
#print(warehouses)

print()
print('INSERT INTO warehouse(id) VALUES')
sql_wh_str = ''

for wh in warehouses:
    sql_wh_str += f"({wh}),\n"

sql_wh_str = sql_wh_str[:-2] + ';'
print(sql_wh_str)

sql_item_str = ''

for item in stock:
    sql_item_str += (f"('{item['state']}', '{item['category']}',{item['warehouse']},'{item['date_of_stock']}'),\n")

print()
print('INSERT INTO item(state, category, warehouse_id, date_of_stock) VALUES')
sql_item_str = sql_item_str[:-2] + ';'
print(sql_item_str)