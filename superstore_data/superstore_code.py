import pandas as pd

# 1. Load the dataset.
file_path = "Superstore.csv"
df = pd.read_csv(file_path, encoding='latin1')

print("DATA LOADED SUCCESFULLY")
print(f"Total Rows before cleaning: {len(df)}")


# 2. Check Duplicates
# Check for exact duplicate rows across all columns.
duplicate_count = df.duplicated().sum()
if duplicate_count > 0:
    print(f"Found {duplicate_count} exact duplicate rows.")
else:
    print("No exact duplicate rows found.")


# 3.Convert Order Date to the correct datetime format
df['Order Date'] = pd.to_datetime(df['Order Date'], format='%d-%m-%Y')



# 4. Drop Unnecessary Columns (Select only required columns)
# The analysis requires: Order Date, Region, Category, Sales, Profit column.
required_cols = ['Order ID','Order Date','Region', 'Category', 'Sales', 'Profit']

# Keep only the columns needed for the task
df = df[required_cols].copy()

print(df.head())


# 5. Save Cleaned Data
cleaned_file_path = "Superstore_Sales_Cleaned.csv"
df.to_csv(cleaned_file_path, index=False)

print("\n--- Final Status ---")
print(f"Total Rows after cleaning: {len(df)}")
print(f"Columns in Final File: {list(df.columns)}")
print(f"Cleaned file '{cleaned_file_path}' is ready for Tableau.")

