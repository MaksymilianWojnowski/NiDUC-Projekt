import pandas as pd
import matplotlib.pyplot as plt

# Load the data from the CSV file
data_path = 'output.csv'
df = pd.read_csv(data_path)

# Ensure that the errors columns are treated as integers
df['Errors'] = df['Errors'].astype(int)
df['Single Errors'] = df['Single Errors'].astype(int)
df['Double Errors'] = df['Double Errors'].astype(int)
df['Group Errors'] = df['Group Errors'].astype(int)

# Calculate the total errors for each type
total_single_errors = df['Single Errors'].sum()
total_double_errors = df['Double Errors'].sum()
total_group_errors = df['Group Errors'].sum()

# Calculate percentage of each error type
total_errors = total_single_errors + total_double_errors + total_group_errors
percent_single_errors = (total_single_errors / total_errors) * 100
percent_double_errors = (total_double_errors / total_errors) * 100
percent_group_errors = (total_group_errors / total_errors) * 100

# Calculate percentage of each error type for each polynomial
polynomials = df['Polynomial'].unique()

for poly in polynomials:
    subset = df[df['Polynomial'] == poly]
    total_poly_errors = subset['Errors'].sum()
    if total_poly_errors > 0:
        percent_single = (subset['Single Errors'].sum() / total_poly_errors) * 100
        percent_double = (subset['Double Errors'].sum() / total_poly_errors) * 100
        percent_group = (subset['Group Errors'].sum() / total_poly_errors) * 100

        plt.figure(figsize=(10, 6))
        plt.bar(['Single Errors', 'Double Errors', 'Group Errors'], [percent_single, percent_double, percent_group])
        plt.xlabel('Error Type')
        plt.ylabel('Percentage')
        plt.title(f'Percentage of Error Types for Polynomial {poly}')
        plt.show()

# Plotting the overall percentage of each error type
plt.figure(figsize=(10, 6))
plt.bar(['Single Errors', 'Double Errors', 'Group Errors'], [percent_single_errors, percent_double_errors, percent_group_errors])
plt.xlabel('Error Type')
plt.ylabel('Percentage')
plt.title('Overall Percentage of Error Types')
plt.show()