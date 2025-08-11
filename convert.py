import pandas as pd

# Define the path to your input XLSX file
excel_file_path = './datasets/Heart Attack.xlsx'

# Define the path for your output CSV file
csv_file_path = './datasets/data.csv'

try:
    # Read the Excel file into a pandas DataFrame
    df = pd.read_excel(excel_file_path)

    # Convert the DataFrame to a CSV file, excluding the index
    df.to_csv(csv_file_path, index=False)

    print(f"'{excel_file_path}' successfully converted to '{csv_file_path}'.")

except FileNotFoundError:
    print(f"Error: The file '{excel_file_path}' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")