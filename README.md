# Basic-Sales-Summary-using-Python-and-SQLite

This task demonstrates how to use **SQL inside Python** to pull simple sales information (like total quantity sold and total revenue) from a SQLite database, display the results, and visualize them using a bar chart.

---

## 🎯 Objective

✅ Connect to a **SQLite database** (`sales_data.db`)  
✅ Run SQL queries to summarize sales data:  
  - Total quantity sold per product  
  - Total revenue per product  
✅ Display output using Python `print()`  
✅ Plot a simple bar chart using `matplotlib`  
✅ Save the chart as `sales_chart.png`  

---

## 🛠️ Tools & Libraries

- Python 3.x
- SQLite3 (built into Python)
- pandas
- matplotlib

---

## 📂 Project Structure

```bash
├── sales_summary.py       # Main Python script
├── sales_data.db          # SQLite database (created on first run)
├── sales_chart.png        # Bar chart image (auto-saved)
└── README.md              # Project documentation
```
1. Clone This Repository

```bash
git clone https://github.com/Kevinl-code/Basic-Sales-Summary-using-python-and-sql.git
cd Basic-Sales-Summary-using-python-and-sql
```
2. Install required Python libraries

```bash
   pip install pandas matplotlib
```

3️. Run the script
   ```bash
  python sales_summary.py
  ```

SQL Queries Used
```bash
-- Query 1: Total quantity & revenue per product
SELECT 
    product, 
    SUM(quantity) AS total_qty, 
    SUM(quantity * price) AS revenue
FROM sales
GROUP BY product;

-- Query 2: Total revenue across all products
SELECT 
    SUM(quantity * price) AS total_revenue
FROM sales;
```

📦 Deliverables

✅ `sales_summary.py` - Python script
✅ `sales_data.db` - SQLite database (auto-created)
✅ `sales_chart.png` - Bar chart image (auto-saved)
✅ `README.md` - Documentation

👨‍💻 Author

#### Kevin Lazarus
#### M.Sc. Data Science
#### Bishop Heber College
#### Trichy




