import pandas as pd

def csv_merge (input_file1, input_file2, output_file):
    try:
        df1 = pd.read_csv(input_file1)
        df2 = pd.read_csv(input_file2)
        #now for the merger
        df_merged = pd.concat([df1,df2], ignore_index=True) #the TRUE makes sure we don't have duplicate indices in the data
        #save the merged data frame to the output file
        df_merged.to_csv(output_file, index=False) #The FALSE makes sure that the csv file doesn't have the index column that the df has
        print(f"Files merged and saved to {output_file}")

    except FileNotFoundError:
        print("One or both input files were not found. Please check file paths.")
    except Exception as e:
        print(f"An error occurred: {e}")

input_file1 = input("Please enter file path 1: ")
input_file2 = input("Please enter file path 2: ")
output_file = input("Please enter path for output file: ")
