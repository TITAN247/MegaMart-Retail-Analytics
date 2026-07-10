# 🛒 MegaMart Retail Analytics using NumPy

A complete **Retail Analytics System** built entirely using **NumPy**. This project simulates real-world retail sales data, performs business analytics, generates reports, and exports results into CSV files.

This project was built to practice and demonstrate almost every major NumPy concept, including array manipulation, statistics, searching, sorting, Boolean indexing, CSV handling, and data analysis.

---

# 🚀 Features

- 📊 Generate a realistic retail sales dataset
- 📁 Read and process CSV files using NumPy
- 💰 Revenue Calculation
- 📈 Business KPI Dashboard
- 🎯 Revenue Analysis
- 🏷 Discount Analysis
- ⭐ Customer Rating Analysis
- 🏪 Store Performance Analysis
- 🛍 Category Analysis
- 🌆 City-wise Analysis
- 💳 Payment Mode Analysis
- 🔍 Boolean Indexing & Advanced Filtering
- 🔎 Searching Functions
- 🔃 Sorting Functions
- 📉 Statistical Analysis
- 🔧 Array Manipulation
- 💾 Automatic Report Generation (CSV)

---

# 📂 Project Structure

```
MegaMart/
│
├── megamart.py
├── MegaMartSales.csv
│
├── Top10Stores.csv
├── HighDiscountProducts.csv
├── BestRatedProducts.csv
├── DelhiSales.csv
├── ElectronicsSales.csv
├── StoreRevenue.csv
│
├── README.md
├── requirements.txt
└── .gitignore
```

---

# 📦 Dataset

The project generates a dataset containing **100,000 retail transactions**.

Each transaction contains:

| Column |
|--------|
| TransactionID |
| StoreID |
| ProductID |
| Category |
| Quantity |
| Price |
| Discount |
| City |
| PaymentMode |
| Rating |

---

# 📊 Modules Implemented

## 1. Dataset Generation

- Generate 100,000 transactions
- Random store IDs
- Product IDs
- Categories
- Cities
- Payment Modes
- Customer Ratings

---

## 2. Revenue Analysis

- Total Revenue
- Average Revenue
- Maximum Revenue
- Minimum Revenue
- Median Revenue
- Standard Deviation
- Variance
- Percentiles
- Quantiles

---

## 3. Discount Analysis

- Highest Discount
- Lowest Discount
- Average Discount
- High Discount Products
- Discount Distribution

---

## 4. Customer Rating Analysis

- Average Rating
- Highest Rated Products
- Lowest Rated Products
- Rating Distribution
- Customer Satisfaction

---

## 5. Store Analysis

- Revenue of Every Store
- Top 10 Stores
- Bottom 10 Stores
- Highest Revenue Store
- Lowest Revenue Store
- Average Revenue per Store

---

## 6. Category Analysis

- Electronics Revenue
- Furniture Revenue
- Clothing Revenue
- Grocery Revenue
- Highest Selling Category
- Lowest Selling Category

---

## 7. City Analysis

- Revenue by City
- Quantity Sold by City
- Average Rating by City
- Highest Revenue City
- Lowest Revenue City

---

## 8. Payment Analysis

- Cash %
- Card %
- UPI %
- Revenue by Payment Mode
- Most Preferred Payment Method
- Least Preferred Payment Method

---

## 9. Boolean Indexing

Examples include:

- Price > ₹5000
- Discount >20%
- Rating >4
- Quantity >5
- Electronics Products
- Delhi Sales
- Card Payments
- Multiple Combined Conditions

---

## 10. Searching Functions

Implemented:

- np.where()
- np.nonzero()
- np.argwhere()
- np.argmax()
- np.argmin()
- np.count_nonzero()

---

## 11. Sorting Functions

Implemented:

- np.sort()
- np.argsort()
- Quick Sort
- Merge Sort
- Heap Sort

Sorting performed on:

- Revenue
- Quantity
- Discount
- Rating
- StoreID
- ProductID
- Category

---

## 12. Statistical Analysis

- Mean
- Median
- Sum
- Min
- Max
- Standard Deviation
- Variance
- Percentile
- Quantile

---

## 13. Array Manipulation

Implemented:

- reshape()
- flatten()
- ravel()
- transpose()
- swapaxes()
- concatenate()
- stack()
- hstack()
- vstack()
- split()

---

## 14. Report Generation

Automatically generates:

- Top10Stores.csv
- HighDiscountProducts.csv
- BestRatedProducts.csv
- DelhiSales.csv
- ElectronicsSales.csv
- StoreRevenue.csv

---

# 🛠 Technologies Used

- Python 3
- NumPy

---

# ▶️ How to Run

Clone the repository

```bash
git clone https://github.com/TITAN247/MegaMart.git
```

Move into the project

```bash
cd MegaMart
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the project

```bash
python megamart.py
```

---

# 📚 NumPy Concepts Covered

- Array Creation
- Array Attributes
- Indexing
- Slicing
- Broadcasting
- Vectorization
- Random Module
- CSV Reading
- CSV Writing
- Boolean Indexing
- Searching
- Sorting
- Statistics
- Mathematical Functions
- Aggregation
- Structured Arrays
- Array Manipulation

---

# 🎯 Learning Outcomes

This project demonstrates practical implementation of:

- Data Analysis using NumPy
- Business Intelligence Concepts
- Retail Sales Analytics
- CSV Data Processing
- Statistical Analysis
- Report Generation
- Real-world Data Manipulation

---

# 📄 License

This project is created for learning, portfolio, and educational purposes.

---

## ⭐ If you found this project useful, don't forget to star the repository!
