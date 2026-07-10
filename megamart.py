# megamart.py
import numpy as np

# ==========================================================
#               MEGAMART RETAIL ANALYTICS
#               STEP 1 : GENERATE DATASET
# ==========================================================

# Make random values same every time (Optional)
np.random.seed(42)

# ----------------------------------------------------------
# Number of Transactions
# ----------------------------------------------------------

num_transactions = 100000

# ----------------------------------------------------------
# Transaction ID
# Generates IDs from 100001 to 110000
# ----------------------------------------------------------

transaction_id = np.arange(100001, 100001 + num_transactions)

# ----------------------------------------------------------
# Store IDs
# 500 stores available
# Store ID : 1 - 500
# ----------------------------------------------------------

store_id = np.random.randint(1, 501, num_transactions)

# ----------------------------------------------------------
# Product IDs
# 100 products
# Product ID : 1001 - 1100
# ----------------------------------------------------------

product_id = np.random.randint(1001, 1101, num_transactions)

# ----------------------------------------------------------
# Product Category
# ----------------------------------------------------------

categories = np.array([
    "Electronics",
    "Grocery",
    "Furniture",
    "Clothing"
])

category = np.random.choice(categories, num_transactions)

# ----------------------------------------------------------
# Quantity Purchased
# Random quantity between 1 and 10
# ----------------------------------------------------------

quantity = np.random.randint(1, 11, num_transactions)

# ----------------------------------------------------------
# Price Per Item
# Random decimal values between ₹100 and ₹10000
# Rounded to 2 decimal places
# ----------------------------------------------------------

price = np.round(np.random.uniform(100, 10000, num_transactions), 2)

# ----------------------------------------------------------
# Discount Percentage
# ----------------------------------------------------------

discount_options = np.array([0, 5, 10, 15, 20, 25, 30])

discount = np.random.choice(discount_options, num_transactions)

# ----------------------------------------------------------
# City
# ----------------------------------------------------------

cities = np.array([
    "Delhi",
    "Mumbai",
    "Lucknow",
    "Chennai",
    "Bangalore"
])

city = np.random.choice(cities, num_transactions)

# ----------------------------------------------------------
# Payment Mode
# ----------------------------------------------------------

payment_modes = np.array([
    "Cash",
    "Card",
    "UPI"
])

payment_mode = np.random.choice(payment_modes, num_transactions)

# ----------------------------------------------------------
# Customer Rating
# Rating between 1 and 5
# ----------------------------------------------------------

rating = np.random.randint(1, 6, num_transactions)

# ==========================================================
# Combine All Columns
# ==========================================================

sales_data = np.column_stack((
    transaction_id,
    store_id,
    product_id,
    category,
    quantity,
    price,
    discount,
    city,
    payment_mode,
    rating
))

# ==========================================================
# Save CSV File
# ==========================================================

np.savetxt(
    "MegaMartSales.csv",
    sales_data,
    delimiter=",",
    fmt="%s",
    header="TransactionID,StoreID,ProductID,Category,Quantity,Price,Discount,City,PaymentMode,Rating",
    comments="",
    encoding="utf-8"
)

# ==========================================================
# Display Sample Data
# ==========================================================

print("=" * 70)
print("        MEGAMART DATASET GENERATED SUCCESSFULLY")
print("=" * 70)

print("\nShape of Dataset")
print(sales_data.shape)

print("\nFirst 5 Records")
print(sales_data[:5])

print("\nLast 5 Records")
print(sales_data[-5:])

print("\nCSV File Saved Successfully as 'MegaMartSales.csv'")