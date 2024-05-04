import pandas as pd

# Problem 01: Read a CSV file and display the first 5 rows
def read_csv_file(file_path):
    df = pd.read_csv(file_path)
    print(df.head(5))

# Main function
if __name__ == "__main__":
    file_path = "../data/data_01.csv"  # Update the file path accordingly
    read_csv_file(file_path)