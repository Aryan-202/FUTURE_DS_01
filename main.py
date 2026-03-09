import os
import pandas as pd

def clean_data(input_path: str, output_path: str):
    """
    Reads a raw CSV file, cleans the data, and saves it to a processed folder.
    """
    print(f"Loading data from {input_path}...")
    # Superstore dataset often uses windows-1252 encoding
    try:
        df = pd.read_csv(input_path, encoding='windows-1252')
    except UnicodeDecodeError:
        df = pd.read_csv(input_path, encoding='utf-8')

    print(f"Original shape: {df.shape}")

    # 1. Drop completely empty rows and columns
    df = df.dropna(how='all')
    df = df.dropna(axis=1, how='all')
    
    # 2. Drop duplicate rows
    initial_rows = len(df)
    df = df.drop_duplicates()
    if len(df) < initial_rows:
        print(f"Dropped {initial_rows - len(df)} duplicate rows.")

    # 3. Strip leading/trailing whitespaces from column names
    df.columns = df.columns.str.strip()

    # 4. Standardize string columns (strip whitespaces)
    for col in df.select_dtypes(include=['object']):
        df[col] = df[col].astype(str).str.strip()

    # 5. Convert date columns if they exist
    date_columns = ['Order Date', 'Ship Date']
    for col in date_columns:
        if col in df.columns:
            # Using mixed format for robustness 
            df[col] = pd.to_datetime(df[col], format='mixed', dayfirst=False, errors='coerce')
            print(f"Converted '{col}' to datetime.")
            
    # Ensure processed directory exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # Save cleaned data
    print(f"Saving cleaned data to {output_path}...")
    df.to_csv(output_path, index=False)
    print(f"Cleaned shape: {df.shape}")
    print("Data cleaning completed successfully.")


def main():
    raw_file = os.path.join('data', 'raw', 'Superstore.csv')
    processed_file = os.path.join('data', 'processed', 'Superstore.csv')
    
    if not os.path.exists(raw_file):
        print(f"Error: {raw_file} not found.")
        return

    clean_data(raw_file, processed_file)


if __name__ == "__main__":
    main()
