import pandas as pd
import sqlite3

#Task 1
with  sqlite3.connect("../db/lesson.db") as conn:
    conn.execute("PRAGMA foreign_keys = 1")
    cursor = conn.cursor()

    sql_statement = """ SELECT orders.order_id, SUM (line_items.quantity * products.price) AS total_price  
    FROM line_items 
    JOIN orders ON line_items.order_id = orders.order_id 
    JOIN products ON line_items.product_id = products.product_id 
    GROUP BY orders.order_id 
    ORDER BY orders.order_id
    LIMIT 5;
    """
    orders_total = pd.read_sql_query(sql_statement, conn)
    print("orders_total: \n", orders_total)


#Task 2

    sql_statement = """SELECT customers.customer_id, AVG(order_totals.total_price) AS average_order_price 
    FROM Customers 
    LEFT JOIN 
        (SELECT customers.customer_id AS customer_id_b, SUM(line_items.quantity * products.price) AS total_price 
        FROM Customers
        JOIN orders ON orders.customer_id = customers.customer_id 
        JOIN line_items ON line_items.order_id = orders.order_id
        JOIN products ON line_items.product_id = products.product_id 
        GROUP BY orders.order_id
    ) AS order_totals 
    ON customers.customer_id = order_totals.customer_id_b 
    GROUP BY customers.customer_id
    ORDER BY customers.customer_id;
    """
    customers_average = pd.read_sql_query(sql_statement, conn)
    print("customers_average: \n: ", customers_average)


#Task 3

    sql_statement = """SELECT customers.customer_id FROM customers WHERE customer_name = 'Perez and Sons'"""
    cursor.execute(sql_statement)
    results = cursor.fetchone()
    customer_id = results[0]
    print("customer_id: ", customer_id)

    sql_statement = """SELECT employees.employee_id FROM employees WHERE first_name = 'Miranda' AND last_name = 'Harris'"""
    cursor.execute(sql_statement)
    results = cursor.fetchone()
    employee_id = results[0]
    print("employee_id: ", employee_id)

    sql_statement = """SELECT product_id FROM products
        ORDER BY price 
        LIMIT 5"""
    cursor.execute(sql_statement)
    results = cursor.fetchall()
    product_ids = [id[0] for id in results]
    print("product_ids: ", product_ids)

    #insert information into tables inside a transaction
    try:
        #insert into orders table    
        cursor.execute(f"""INSERT INTO orders (customer_id, employee_id, date) 
            VALUES ({customer_id}, {employee_id}, CURRENT_DATE)
            RETURNING order_id""")
        results = cursor.fetchone()
        order_id = results[0]
        print("order_id: ", order_id)

        #insert into line_items table
        values = [(order_id, p_id, 10) for p_id in product_ids]
        sql_statement = """INSERT INTO line_items (order_id, product_id, quantity) VALUES (?, ?, ?)"""
        cursor.executemany(sql_statement,  values)
        conn.commit()

    except Exception as e:
        conn.rollback()
        print("Error: ", e)

    #print list of line_item_ids, quantity, and product name for the order
    sql_statement = (f"""SELECT line_items.line_item_id, products.product_name, line_items.quantity 
    FROM line_items
    JOIN products ON line_items.product_id = products.product_id
    WHERE order_id = {order_id}
    """)
    new_order_info = pd.read_sql_query(sql_statement, conn)
    print("new_order_info: \n", new_order_info)



#Task 4
with sqlite3.connect("../db/lesson.db") as conn:
    sql_statement = """SELECT employees.first_name, employees.last_name, COUNT(orders.order_id) AS total_orders 
    FROM employees 
    RIGHT JOIN orders ON orders.employee_id = employees.employee_id 
    GROUP BY employees.employee_id 
    HAVING (total_orders > 5)
    ORDER BY total_orders DESC;
    """
    top_employees = pd.read_sql_query(sql_statement, conn)
    print("top_employees: \n", top_employees)