# *Task 5: Read Data into a DataFrame*

import pandas as pd
import sqlite3


# Read data into a DataFrame, as described in the lesson.  The SQL statement should retrieve the line_item_id, quantity, product_id, product_name, and price from a JOIN of the line_items table and the product table. 

with sqlite3.connect("../db/lesson.db") as conn:
    sql_statement = """SELECT line_items.line_item_id, line_items.quantity, line_items.product_id, products.product_name, products.price FROM line_items INNER JOIN products ON line_items.product_id = products.product_id;"""
    df = pd.read_sql_query(sql_statement, conn)
    #print the first 5 lines
    print("original dataframe: \n", df.head())

# Add a column to the DataFrame called "total".  This is the quantity times the price.  (This is easy: `df['total'] = df['quantity'] * df['price']`.)  Print out the first 5 lines of the DataFrame to make sure this works.
df['total'] = df['quantity'] * df['price']
print("dataframe after adding total column: \n", df.head())

# Add groupby() code to group by the product_id.  Use an agg() method that specifies 'count' for the line_item_id column, 'sum' for the total column, and 'first' for the 'product_name'.  Print out the first 5 lines of the resulting DataFrame.  Run the program to see if it is correct so far.
df_grouped = df.groupby(['product_id']).agg(
    line_item_id_count=('line_item_id', 'count'),
    total_sum=('total', 'sum'),
    product_name=('product_name', 'first')
)
print("df_grouped: \n", df_grouped.head())

# Sort the DataFrame by the product_name column.
df_sorted = df_grouped.sort_values(by='product_name')
print("df_sorted: \n", df_sorted.head())

# Add code to write this DataFrame to a file `order_summary.csv`, which should be written in the `assignment7` directory.  Verify that this file is correct.
order_summary_csv = df_sorted.to_csv('order_summary_csv', index=True)