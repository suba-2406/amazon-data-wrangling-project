import pandas as pd

# Load dataset
df = pd.read_csv("data/raw/amazon.csv")

# ====================================
# HANDLE MISSING VALUES
# ====================================

# Fill missing rating_count with 0
df['rating_count'] = df['rating_count'].fillna('0')

# ====================================
# CLEAN PRICE COLUMNS
# ====================================

# Remove ₹ and commas
df['discounted_price'] = df['discounted_price'].str.replace('₹', '')
df['discounted_price'] = df['discounted_price'].str.replace(',', '')

df['actual_price'] = df['actual_price'].str.replace('₹', '')
df['actual_price'] = df['actual_price'].str.replace(',', '')

# Convert to float
df['discounted_price'] = df['discounted_price'].astype(float)
df['actual_price'] = df['actual_price'].astype(float)

# ====================================
# CLEAN DISCOUNT PERCENTAGE
# ====================================

# Remove %
df['discount_percentage'] = df['discount_percentage'].str.replace('%', '')

# Convert to float
df['discount_percentage'] = df['discount_percentage'].astype(float)

# ====================================
# CLEAN RATING COLUMN
# ====================================

df['rating'] = pd.to_numeric(df['rating'], errors='coerce')

# ====================================
# CLEAN RATING COUNT
# ====================================

# Remove commas
df['rating_count'] = df['rating_count'].str.replace(',', '')

# Convert to integer
df['rating_count'] = df['rating_count'].astype(int)

# ====================================
# SIMPLIFY CATEGORY COLUMN
# ====================================

# Take only main category
df['main_category'] = df['category'].apply(lambda x: x.split('|')[0])

# ====================================
# FEATURE ENGINEERING
# ====================================

# Calculate savings amount
df['savings_amount'] = df['actual_price'] - df['discounted_price']

# ====================================
# FINAL DATA INFO
# ====================================

print("\nCLEANED DATA TYPES:")
print(df.dtypes)

print("\nMISSING VALUES AFTER CLEANING:")
print(df.isnull().sum())

print("\nFIRST 5 ROWS:")
print(df.head())

# ====================================
# SAVE CLEANED DATASET
# ====================================

df.to_csv("data/cleaned/cleaned_amazon_data.csv", index=False)

print("\nDataset cleaned successfully!")
print("Cleaned file saved in data/cleaned/")

# ====================================
# VALIDATION CHECKS
# ====================================

print("\n==============================")
print("VALIDATION CHECKS")
print("==============================")

# Check datatypes
print("\nFINAL DATA TYPES:")
print(df.dtypes)

# Check missing values
print("\nFINAL MISSING VALUES:")
print(df.isnull().sum())

# Check dataset shape
print("\nFINAL DATASET SHAPE:")
print(df.shape)

# Statistical summary
print("\nNUMERICAL SUMMARY:")
print(df.describe())

# Check new columns
print("\nNEW COLUMNS CREATED:")
print(df[['main_category', 'savings_amount']].head())

print("\nDATASET IS NOW ANALYSIS READY!")