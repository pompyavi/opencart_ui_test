import pandas as pd
from pathlib import Path

# Read the Excel file into a DataFrame
root = Path.cwd()
test_data_path = root / 'testdata/test_data.xlsx'


def get_test_data(sheet_name):
    df = pd.read_excel(test_data_path, sheet_name=sheet_name)

    # Get the number of columns
    num_columns = df.shape[1]
    data = []
    for index in range(len(df)):
        row = df.iloc[index]
        # Print each column dynamically
        row_list = []
        for col_index in range(num_columns):
            row_list.append(str(row.iloc[col_index]))
        data.append(tuple(row_list))

    return data




