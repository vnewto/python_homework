import sqlite3

try: # SQL operations can raise exceptions!
    
    # The with statement is helpful, because it ensures that the connection
    # is closed at the end, even if an exception occurs
    with sqlite3.connect("./db/lesson.db",isolation_level='IMMEDIATE') as conn:    
        cursor = conn.cursor()
        conn.execute("PRAGMA foreign_keys = 1")
        # This does a SELECT and a subquery
        stmt = """SELECT o.order_id, l.line_item_id, p.product_name FROM orders  
        o JOIN line_items l on o.order_id = l.order_id JOIN products p on 
        l.product_id = p.product_id WHERE o.order_id IN 
        (SELECT order_id from orders ORDER BY order_id limit 5);"""
        cursor.execute(stmt)
        result = cursor.fetchall()
        for row in result:
            print(row)

        # This retrieves the first 5 orders joined with the line_items and products tables, 
        # and aggregates (SUM) the quantity by the price to give the cost of each order
        stmt = """SELECT o.order_id, SUM(l.quantity * p.price) FROM orders o JOIN line_items l ON 
        o.order_id = l.order_id JOIN products p on l.product_id = p.product_id GROUP BY o.order_id 
        ORDER BY o.order_id LIMIT 5;"""
        cursor.execute(stmt)
        result = cursor.fetchall()
        for row in result:
            print(row)

        # This creates a new order with corresponding line_items.  First, we get the ids of
        # the customer, the employee, and the products.
        stmt = """SELECT customer_id FROM customers WHERE customer_name = \"Perez and Sons\";"""
        cursor.execute(stmt)
        result = cursor.fetchone()
        print(result)
        customer_id = result[0]
        stmt = """SELECT employee_id FROM employees WHERE first_name = \"Miranda\" AND last_name = \"Harris\";"""
        cursor.execute(stmt)
        result = cursor.fetchone()
        print(result)
        employee_id = result[0]
        stmt = """SELECT product_id FROM products ORDER BY price DESC LIMIT 5"""
        cursor.execute(stmt)
        result=cursor.fetchall()
        print(result)
        products = result

        # Now we add the order, saving the returned order_id.  This example uses a parameterized
        # statement.  It is not really necessary to use a parameterized statement when the
        # values come from a trusted source, because no SQL injection could occur in that case.
        stmt = f"""INSERT INTO orders (employee_id, customer_id) VALUES (?,?) RETURNING order_id"""
        cursor.execute(stmt,(employee_id, customer_id))
        result = cursor.fetchone()
        print(result)
        order_id = result[0]
        values = []
        for i in range(5):
            values.append(f"({order_id}, {products[i][0]}, 10)")
        values_string = ",".join(values)
        
        stmt = f"""INSERT INTO line_items (order_id, product_id, quantity) VALUES {values_string};"""
        print(stmt)
        cursor.execute(stmt)
        conn.commit()
        stmt=f"""SELECT l.line_item_id, l.quantity, p.product_name FROM line_items l JOIN products p ON 
        l.product_id = p.product_id WHERE l.order_id = {order_id};"""
        cursor.execute(stmt)
        result = cursor.fetchall()
        for row in result:
            print(row)
except Exception as e:
    print(f"An exception occurred: {e}")
else:
    print("All SQL operations completed.")
    