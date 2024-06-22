import pandas as pd

def check_constituencies(file_path):
    # Load the CSV file into a DataFrame
    df = pd.read_csv(file_path)
    
    # Check the number of entries in the DataFrame
    entry_count = len(df)
    
    if entry_count == 650:
        print("The CSV file contains exactly 650 entries.")
    else:
        print(f"The CSV file contains {entry_count} entries, which is not the expected 650 entries.")

def main():
    file_path = 'UK_Constituencies_2024.csv'  # Adjust the file path as needed
    check_constituencies(file_path)

if __name__ == "__main__":
    main()
