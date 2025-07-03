#Import required libraries
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# -------------------------------------------
# Step 1: Create SQLite Database & Insert Data
# -------------------------------------------
# Connect to (or create) the database
conn = sqlite3.connect("sales_data.db")
cursor = conn.cursor()

# Create the sales table
cursor.execute("""
CREATE TABLE IF NOT EXISTS sales (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product TEXT NOT NULL,
    quantity INTEGER NOT NULL,
    price REAL NOT NULL
)
""")

# Insert sample data (only if table is empty)
cursor.execute("SELECT COUNT(*) FROM sales")
if cursor.fetchone()[0] == 0:  # Insert only if table is empty
    sample_data = [
        ("Laptop", 5, 60000.00),
        ("Smartphone", 10, 30000.00),
        ("Headphones", 15, 2000.00),
        ("Tablet", 7, 25000.00),
        ("Smartwatch", 8, 8000.00),
        ("Earbuds", 12, 1500.00)
    ]
    cursor.executemany("INSERT INTO sales (product, quantity, price) VALUES (?, ?, ?)", sample_data)
    conn.commit()
    print("✅ Database created and sample data inserted.")
else:
    print("ℹ️ Database already has data. Skipping insert.")

# -------------------------------------------
# Step 2: Run SQL Queries
# -------------------------------------------

# Query 1: Total quantity and revenue per product
query1 = """
SELECT 
    product, 
    SUM(quantity) AS total_qty, 
    SUM(quantity * price) AS revenue
FROM sales
GROUP BY product
"""
df_summary = pd.read_sql_query(query1, conn)

# Query 2: Total revenue across all products
query2 = """
SELECT 
    SUM(quantity * price) AS total_revenue
FROM sales
"""
df_total_revenue = pd.read_sql_query(query2, conn)

# Close DB connection
conn.close()

# -------------------------------------------
# Step 3: Display Results
# -------------------------------------------
print("\n=== 📊 Basic Sales Summary ===")
print(df_summary)

print("\n💰 Total Revenue Across All Products:")
print(df_total_revenue)

# -------------------------------------------
# Step 4: Plot Bar Chart of Revenue
# -------------------------------------------
plt.figure(figsize=(8, 5))
df_summary.plot(kind='bar', x='product', y='revenue', color='skyblue', legend=False)
plt.title("Revenue by Product")
plt.ylabel("Revenue (₹)")
plt.xlabel("Product")
plt.xticks(rotation=45)
plt.tight_layout()

# Save chart
plt.savefig("sales_chart.png")
print("\n📈 Bar chart saved as 'sales_chart.png'.")

# Show chart
plt.show()
