import pandas as pd

def clean_data_rename_column (input_file, output_file, old_column_name, new_column_name):

    try:
        df = pd.read_csv(input_file)
        #remove the rows with missing values
        cleaned_df = df.dropna()
        # Check if DataFrame is empty after cleaning
        if cleaned_df.empty:
            print("Error: No valid data left after removing missing values.")
            return
        #rename one of the columns
        if old_column_name.lower() in map(str.lower, df.columns):
            cleaned_df = cleaned_df.rename(columns={old_column_name: new_column_name})
        else:
            print(f"{old_column_name} not found. Renaming skipped.")
            return
        #store the cleaned data frame as a csv
        cleaned_df.to_csv(output_file, index=False)

    except FileNotFoundError:
        print("File not found. Please recheck file path")
    except pd.errors.EmptyDataError:
        print("Error: The input file is empty.")
    except Exception as e:
        print(f"Unknown Error {e}")

input_file = input("Please enter complete file path: ").strip()
old_column_name = input("Please enter the name of the column you'd like to rename: ").strip()
new_column_name = input("Please enter the name you'd like to assign: ").strip()
output_file = input("Please enter the file path for the output file. If it does not exist, the file will be created: ").strip()

clean_data_rename_column(input_file=input_file, output_file=output_file,
                        old_column_name=old_column_name, new_column_name=new_column_name)


