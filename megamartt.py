# megamartt.py
import numpy as np

# ==========================================================
# STEP 2 : READ THE CSV FILE
# ==========================================================

sales = np.genfromtxt(

    "MegaMartSales.csv",

    delimiter=",",

    names=True,

    dtype=None,

    encoding="utf-8",

    autostrip=True

)

print("="*70)
print("DATASET LOADED SUCCESSFULLY")
print("="*70)

print("\nShape")
print(sales.shape)

print("\nColumn Names")
print(sales.dtype.names)

print("\nFirst Record")
print(sales[0])

print("\nLast Record")
print(sales[-1])

print("\nStore IDs")
print(sales["StoreID"][:10])

print("\nCategories")
print(sales["Category"][:10])

print("\nPrices")
print(sales["Price"][:10])

# ==========================================================
# STEP 3 : CALCULATE REVENUE
# ==========================================================

revenue = (
    sales["Quantity"] *
    sales["Price"] *
    (1 - sales["Discount"] / 100)
)

print("=" * 70)
print("REVENUE GENERATED SUCCESSFULLY")
print("=" * 70)

print("\nFirst 10 Revenue Values")
print(revenue[:10])

print("\nRevenue Shape")
print(revenue.shape)

print("\nRevenue Data Type")
print(revenue.dtype)


# ==========================================================
# STEP 4 : BUSINESS KPI DASHBOARD
# ==========================================================

total_transactions = len(sales)

total_revenue = np.sum(revenue)

average_revenue = np.mean(revenue)

highest_sale = np.max(revenue)

lowest_sale = np.min(revenue)

total_quantity = np.sum(sales["Quantity"])

average_quantity = np.mean(sales["Quantity"])

average_rating = np.mean(sales["Rating"])

highest_rating = np.max(sales["Rating"])

lowest_rating = np.min(sales["Rating"])

average_discount = np.mean(sales["Discount"])

print("\n")
print("="*70)
print("            MEGAMART BUSINESS DASHBOARD")
print("="*70)

print(f"Total Transactions    : {total_transactions}")

print(f"Total Revenue         : ₹{total_revenue:.2f}")

print(f"Average Revenue       : ₹{average_revenue:.2f}")

print(f"Highest Sale          : ₹{highest_sale:.2f}")

print(f"Lowest Sale           : ₹{lowest_sale:.2f}")

print(f"Total Quantity Sold   : {total_quantity}")

print(f"Average Quantity      : {average_quantity:.2f}")

print(f"Average Rating        : {average_rating:.2f}")

print(f"Highest Rating        : {highest_rating}")

print(f"Lowest Rating         : {lowest_rating}")

print(f"Average Discount      : {average_discount:.2f}%")



# ==========================================================
# STEP 5 : REVENUE ANALYSIS
# ==========================================================

revenue_std = np.std(revenue)

revenue_variance = np.var(revenue)

median_revenue = np.median(revenue)

percentile25 = np.percentile(revenue,25)

percentile75 = np.percentile(revenue,75)

percentile90 = np.percentile(revenue,90)

print("\n")
print("="*70)
print("             REVENUE ANALYSIS")
print("="*70)

print(f"Total Revenue           : ₹{np.sum(revenue):,.2f}")

print(f"Average Revenue         : ₹{np.mean(revenue):,.2f}")

print(f"Highest Revenue         : ₹{np.max(revenue):,.2f}")

print(f"Lowest Revenue          : ₹{np.min(revenue):,.2f}")

print(f"Standard Deviation      : ₹{revenue_std:,.2f}")

print(f"Variance                : ₹{revenue_variance:,.2f}")

print(f"Median Revenue          : ₹{median_revenue:,.2f}")

print(f"25th Percentile         : ₹{percentile25:,.2f}")

print(f"75th Percentile         : ₹{percentile75:,.2f}")

print(f"90th Percentile         : ₹{percentile90:,.2f}")

# ==========================================================
# MODULE 2 : DISCOUNT ANALYSIS
# ==========================================================

highest_discount = np.max(sales["Discount"])

lowest_discount = np.min(sales["Discount"])

average_discount = np.mean(sales["Discount"])

highest_discount_products = sales[sales["Discount"] == highest_discount]

high_discount_products = sales[sales["Discount"] > 20]

discount_values, discount_counts = np.unique(
    sales["Discount"],
    return_counts=True
)

print("\n")
print("=" * 70)
print("                DISCOUNT ANALYSIS")
print("=" * 70)

print(f"Highest Discount          : {highest_discount}%")

print(f"Lowest Discount           : {lowest_discount}%")

print(f"Average Discount          : {average_discount:.2f}%")

print(f"Products With Max Discount: {len(highest_discount_products)}")

print(f"Products >20% Discount    : {len(high_discount_products)}")

print("\nDiscount Distribution")

for value, count in zip(discount_values, discount_counts):
    print(f"{value:>2}% Discount  --->  {count} Transactions")




# ==========================================================
# MODULE 3 : CUSTOMER RATING ANALYSIS
# ==========================================================

average_rating = np.mean(sales["Rating"])

highest_rating = np.max(sales["Rating"])

lowest_rating = np.min(sales["Rating"])

highest_rated_products = sales[
    sales["Rating"] == highest_rating
]

lowest_rated_products = sales[
    sales["Rating"] == lowest_rating
]

good_products = sales[
    sales["Rating"] > 4
]

rating_values, rating_counts = np.unique(
    sales["Rating"],
    return_counts=True
)

most_common_rating = rating_values[np.argmax(rating_counts)]

least_common_rating = rating_values[np.argmin(rating_counts)]

happy_customers = np.count_nonzero(
    sales["Rating"] >= 4
)

satisfaction = (
    happy_customers /
    len(sales)
) * 100

print("\n")
print("="*70)
print("          CUSTOMER RATING ANALYSIS")
print("="*70)

print(f"Average Rating             : {average_rating:.2f}")

print(f"Highest Rating             : {highest_rating}")

print(f"Lowest Rating              : {lowest_rating}")

print(f"Highest Rated Products     : {len(highest_rated_products)}")

print(f"Lowest Rated Products      : {len(lowest_rated_products)}")

print(f"Products Rating >4         : {len(good_products)}")

print(f"Happy Customers            : {happy_customers}")

print(f"Satisfaction Percentage    : {satisfaction:.2f}%")

print(f"Most Common Rating         : {most_common_rating}")

print(f"Least Common Rating        : {least_common_rating}")

print("\nRating Distribution")

for rating, count in zip(rating_values, rating_counts):
    print(f"{rating} Star ---> {count} Customers")


# ==========================================================
# MODULE 4 : STORE ANALYSIS
# ==========================================================

store_ids = np.unique(sales["StoreID"])

store_revenue = []

for store in store_ids:

    current_revenue = np.sum(
        revenue[sales["StoreID"] == store]
    )

    store_revenue.append(current_revenue)

store_revenue = np.array(store_revenue)

highest_store = store_ids[np.argmax(store_revenue)]

lowest_store = store_ids[np.argmin(store_revenue)]

average_store_revenue = np.mean(store_revenue)

top10 = np.argsort(store_revenue)[-10:]

bottom10 = np.argsort(store_revenue)[:10]

print("\n")
print("="*70)
print("               STORE ANALYSIS")
print("="*70)

print(f"Highest Revenue Store : {highest_store}")

print(f"Lowest Revenue Store  : {lowest_store}")

print(f"Average Store Revenue : ₹{average_store_revenue:,.2f}")

print("\nTop 10 Stores")

for index in top10[::-1]:
    print(f"Store {store_ids[index]} ---> ₹{store_revenue[index]:,.2f}")

print("\nBottom 10 Stores")

for index in bottom10:
    print(f"Store {store_ids[index]} ---> ₹{store_revenue[index]:,.2f}")



# ==========================================================
# MODULE 5 : CATEGORY ANALYSIS
# ==========================================================

categories = np.unique(sales["Category"])

category_revenue = []

category_quantity = []

category_average = []

for category in categories:

    current_revenue = np.sum(
        revenue[
            sales["Category"] == category
        ]
    )

    current_quantity = np.sum(
        sales["Quantity"][
            sales["Category"] == category
        ]
    )

    average = np.mean(
        revenue[
            sales["Category"] == category
        ]
    )

    category_revenue.append(current_revenue)

    category_quantity.append(current_quantity)

    category_average.append(average)

category_revenue = np.array(category_revenue)

category_quantity = np.array(category_quantity)

category_average = np.array(category_average)

highest_category = categories[
    np.argmax(category_revenue)
]

lowest_category = categories[
    np.argmin(category_revenue)
]

print("\n")
print("="*70)
print("              CATEGORY ANALYSIS")
print("="*70)

for i in range(len(categories)):

    print(f"\nCategory : {categories[i]}")

    print(f"Revenue  : ₹{category_revenue[i]:,.2f}")

    print(f"Quantity : {category_quantity[i]}")

    print(f"Average Revenue : ₹{category_average[i]:,.2f}")

print("\n")

print(f"Highest Revenue Category : {highest_category}")

print(f"Lowest Revenue Category  : {lowest_category}")



# ==========================================================
# MODULE 6 : CITY ANALYSIS
# ==========================================================

cities = np.unique(sales["City"])

city_revenue = []

city_quantity = []

city_average_rating = []

city_average_revenue = []

for city in cities:

    current_revenue = np.sum(
        revenue[sales["City"] == city]
    )

    current_quantity = np.sum(
        sales["Quantity"][sales["City"] == city]
    )

    current_rating = np.mean(
        sales["Rating"][sales["City"] == city]
    )

    current_average_revenue = np.mean(
        revenue[sales["City"] == city]
    )

    city_revenue.append(current_revenue)

    city_quantity.append(current_quantity)

    city_average_rating.append(current_rating)

    city_average_revenue.append(current_average_revenue)

city_revenue = np.array(city_revenue)

city_quantity = np.array(city_quantity)

city_average_rating = np.array(city_average_rating)

city_average_revenue = np.array(city_average_revenue)

highest_city = cities[np.argmax(city_revenue)]

lowest_city = cities[np.argmin(city_revenue)]

print("\n")
print("="*70)
print("                 CITY ANALYSIS")
print("="*70)

for i in range(len(cities)):

    print(f"\nCity : {cities[i]}")

    print(f"Revenue : ₹{city_revenue[i]:,.2f}")

    print(f"Quantity Sold : {city_quantity[i]}")

    print(f"Average Rating : {city_average_rating[i]:.2f}")

    print(f"Average Revenue : ₹{city_average_revenue[i]:,.2f}")

print("\n")

print(f"Highest Revenue City : {highest_city}")

print(f"Lowest Revenue City  : {lowest_city}")


# ==========================================================
# MODULE 7 : PAYMENT MODE ANALYSIS
# ==========================================================

payment_values, payment_counts = np.unique(

    sales["PaymentMode"],

    return_counts=True

)

payment_percentage = (

    payment_counts /

    len(sales)

) * 100

payment_revenue = []

payment_average = []

for mode in payment_values:

    current_revenue = np.sum(

        revenue[
            sales["PaymentMode"] == mode
        ]

    )

    payment_revenue.append(current_revenue)

    avg = np.mean(

        revenue[
            sales["PaymentMode"] == mode
        ]

    )

    payment_average.append(avg)

payment_revenue = np.array(payment_revenue)

payment_average = np.array(payment_average)

most_preferred = payment_values[

    np.argmax(payment_counts)

]

least_preferred = payment_values[

    np.argmin(payment_counts)

]

print("\n")
print("=" * 70)
print("              PAYMENT MODE ANALYSIS")
print("=" * 70)

for i in range(len(payment_values)):

    print(f"\nPayment Mode : {payment_values[i]}")

    print(f"Transactions : {payment_counts[i]}")

    print(f"Percentage   : {payment_percentage[i]:.2f}%")

    print(f"Revenue      : ₹{payment_revenue[i]:,.2f}")

    print(f"Average Revenue : ₹{payment_average[i]:,.2f}")

print("\n")

print(f"Most Preferred Payment Mode  : {most_preferred}")

print(f"Least Preferred Payment Mode : {least_preferred}")


# ==========================================================
# MODULE 8 : BOOLEAN INDEXING
# ==========================================================

price_above5000 = sales[
    sales["Price"] > 5000
]

discount_above20 = sales[
    sales["Discount"] > 20
]

low_rating = sales[
    sales["Rating"] < 3
]

high_quantity = sales[
    sales["Quantity"] > 5
]

electronics = sales[
    sales["Category"] == "Electronics"
]

delhi_sales = sales[
    sales["City"] == "Delhi"
]

card_sales = sales[
    sales["PaymentMode"] == "Card"
]

premium_sales = sales[
    (sales["City"] == "Delhi")
    &
    (sales["Category"] == "Electronics")
    &
    (sales["Rating"] > 4)
    &
    (sales["Discount"] > 10)
]

print("\n")
print("="*70)
print("             BOOLEAN INDEXING")
print("="*70)

print(f"Price > 5000                : {len(price_above5000)}")

print(f"Discount >20%               : {len(discount_above20)}")

print(f"Rating <3                   : {len(low_rating)}")

print(f"Quantity >5                 : {len(high_quantity)}")

print(f"Electronics Transactions    : {len(electronics)}")

print(f"Delhi Transactions          : {len(delhi_sales)}")

print(f"Card Transactions           : {len(card_sales)}")

print(f"Premium Delhi Electronics   : {len(premium_sales)}")



# ==========================================================
# MODULE 9 : SEARCHING FUNCTIONS
# ==========================================================

highest_transaction = np.argmax(revenue)

lowest_transaction = np.argmin(revenue)

zero_discount = np.where(
    sales["Discount"] == 0
)

five_star = np.where(
    sales["Rating"] == 5
)

electronics = np.where(
    sales["Category"] == "Electronics"
)

non_zero_discount = np.nonzero(
    sales["Discount"]
)

five_star_count = np.count_nonzero(
    sales["Rating"] == 5
)

print("\n")
print("=" * 70)
print("             SEARCHING FUNCTIONS")
print("=" * 70)

print("\nHighest Revenue Transaction")
print(sales[highest_transaction])

print("\nRevenue")
print(revenue[highest_transaction])

print("\nLowest Revenue Transaction")
print(sales[lowest_transaction])

print("\nRevenue")
print(revenue[lowest_transaction])

print("\nTransactions With Discount = 0")
print(len(zero_discount[0]))

print("\nTransactions With Rating = 5")
print(five_star_count)

print("\nElectronics Transactions")
print(len(electronics[0]))

print("\nNon Zero Discount Transactions")
print(len(non_zero_discount[0]))



# ==========================================================
# MODULE 10 : SORTING
# ==========================================================

sorted_revenue = np.sort(revenue)

sorted_revenue_desc = np.sort(revenue)[::-1]

top10_sales = sales[np.argsort(revenue)[-10:]][::-1]

bottom10_sales = sales[np.argsort(revenue)[:10]]

quantity_sorted = sales[np.argsort(sales["Quantity"])]

discount_sorted = sales[np.argsort(sales["Discount"])]

rating_sorted = sales[np.argsort(sales["Rating"])]

store_sorted = sales[np.argsort(sales["StoreID"])]

product_sorted = sales[np.argsort(sales["ProductID"])]

category_sorted = sales[np.argsort(sales["Category"])]

print("\n")
print("=" * 70)
print("                SORTING ANALYSIS")
print("=" * 70)

print("\nLowest 5 Revenue")
print(sorted_revenue[:5])

print("\nHighest 5 Revenue")
print(sorted_revenue_desc[:5])

print("\nTop 10 Revenue Transactions")
print(top10_sales)

print("\nBottom 10 Revenue Transactions")
print(bottom10_sales)

print("\nFirst 5 Transactions Sorted by Quantity")
print(quantity_sorted[:5])

print("\nFirst 5 Transactions Sorted by Discount")
print(discount_sorted[:5])

print("\nFirst 5 Transactions Sorted by Rating")
print(rating_sorted[:5])

print("\nFirst 5 Transactions Sorted by StoreID")
print(store_sorted[:5])

print("\nFirst 5 Transactions Sorted by ProductID")
print(product_sorted[:5])

print("\nFirst 5 Transactions Sorted by Category")
print(category_sorted[:5])



# ==========================================================
# MODULE 11 : STATISTICAL ANALYSIS
# ==========================================================

total_revenue = np.sum(revenue)

average_revenue = np.mean(revenue)

median_revenue = np.median(revenue)

highest_revenue = np.max(revenue)

lowest_revenue = np.min(revenue)

std_revenue = np.std(revenue)

variance_revenue = np.var(revenue)

p25 = np.percentile(revenue,25)

p50 = np.percentile(revenue,50)

p75 = np.percentile(revenue,75)

p90 = np.percentile(revenue,90)

q25 = np.quantile(revenue,0.25)

q50 = np.quantile(revenue,0.50)

q75 = np.quantile(revenue,0.75)

print("\n")
print("="*70)
print("            STATISTICAL ANALYSIS")
print("="*70)

print(f"Total Revenue           : ₹{total_revenue:,.2f}")

print(f"Average Revenue         : ₹{average_revenue:,.2f}")

print(f"Median Revenue          : ₹{median_revenue:,.2f}")

print(f"Maximum Revenue         : ₹{highest_revenue:,.2f}")

print(f"Minimum Revenue         : ₹{lowest_revenue:,.2f}")

print(f"Standard Deviation      : ₹{std_revenue:,.2f}")

print(f"Variance                : ₹{variance_revenue:,.2f}")

print("\nPercentiles")

print(f"25th Percentile         : ₹{p25:,.2f}")

print(f"50th Percentile         : ₹{p50:,.2f}")

print(f"75th Percentile         : ₹{p75:,.2f}")

print(f"90th Percentile         : ₹{p90:,.2f}")

print("\nQuantiles")

print(f"0.25 Quantile           : ₹{q25:,.2f}")

print(f"0.50 Quantile           : ₹{q50:,.2f}")

print(f"0.75 Quantile           : ₹{q75:,.2f}")


# ==========================================================
# MODULE 12 : ARRAY MANIPULATION
# ==========================================================

print("\n")
print("=" * 70)
print("             ARRAY MANIPULATION")
print("=" * 70)

# Create a numeric array
sample = np.arange(12)

print("\nOriginal Array")
print(sample)

# Reshape
matrix = sample.reshape(3,4)

print("\nReshape (3x4)")
print(matrix)

# Flatten
flat = matrix.flatten()

print("\nFlatten")
print(flat)

# Ravel
ravel_array = matrix.ravel()

print("\nRavel")
print(ravel_array)

# Transpose
print("\nTranspose")
print(matrix.T)

# Swap Axes
three_d = np.arange(24).reshape(2,3,4)

print("\nOriginal 3D Shape")
print(three_d.shape)

swapped = np.swapaxes(three_d,0,1)

print("After swapaxes(0,1)")
print(swapped.shape)

# Concatenate
a = np.array([1,2,3])
b = np.array([4,5,6])

print("\nConcatenate")
print(np.concatenate((a,b)))

# Stack
print("\nStack")
print(np.stack((a,b)))

# Horizontal Stack
print("\nHorizontal Stack")
print(np.hstack((a,b)))

# Vertical Stack
print("\nVertical Stack")
print(np.vstack((a,b)))

# Split
print("\nSplit")
parts = np.split(sample,3)

for i, part in enumerate(parts, start=1):
    print(f"Part {i}")
    print(part)




# ==========================================================
# MODULE 13 : SAVE REPORTS
# ==========================================================

print("\n")
print("=" * 70)
print("               SAVING REPORTS")
print("=" * 70)

# Common Header
header = "TransactionID,StoreID,ProductID,Category,Quantity,Price,Discount,City,PaymentMode,Rating"

# ----------------------------------------------------------
# Top 10 Stores Report
# ----------------------------------------------------------

top10_store_report = np.column_stack((
    store_ids[top10],
    store_revenue[top10]
))

np.savetxt(
    "Top10Stores.csv",
    top10_store_report,
    delimiter=",",
    fmt="%s",
    header="StoreID,Revenue",
    comments=""
)

print("✓ Top10Stores.csv Saved")

# ----------------------------------------------------------
# High Discount Products
# ----------------------------------------------------------

np.savetxt(
    "HighDiscountProducts.csv",
    high_discount_products,
    delimiter=",",
    fmt="%s",
    header=header,
    comments=""
)

print("✓ HighDiscountProducts.csv Saved")

# ----------------------------------------------------------
# Best Rated Products
# ----------------------------------------------------------

np.savetxt(
    "BestRatedProducts.csv",
    highest_rated_products,
    delimiter=",",
    fmt="%s",
    header=header,
    comments=""
)

print("✓ BestRatedProducts.csv Saved")

# ----------------------------------------------------------
# Delhi Sales
# ----------------------------------------------------------

np.savetxt(
    "DelhiSales.csv",
    delhi_sales,
    delimiter=",",
    fmt="%s",
    header=header,
    comments=""
)

print("✓ DelhiSales.csv Saved")

# ----------------------------------------------------------
# Electronics Sales
# ----------------------------------------------------------

np.savetxt(
    "ElectronicsSales.csv",
    electronics,
    delimiter=",",
    fmt="%s",
    header=header,
    comments=""
)

print("✓ ElectronicsSales.csv Saved")

# ----------------------------------------------------------
# Store Revenue Report
# ----------------------------------------------------------

store_report = np.column_stack((
    store_ids,
    store_revenue
))

np.savetxt(
    "StoreRevenue.csv",
    store_report,
    delimiter=",",
    fmt="%s",
    header="StoreID,Revenue",
    comments=""
)

print("✓ StoreRevenue.csv Saved")

print("\nAll Reports Saved Successfully!")
