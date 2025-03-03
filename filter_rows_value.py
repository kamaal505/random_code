import pandas as pd

def filter_csv (input_file, column_name, threshold, output_file=None):

    try:

        df = pd.read_csv(input_file) #now check if column_name is present:

        if column_name not in df.columns:
            print("Error: Column not found")

        #create the filtered data_frame

        filtered_df = df[df[column_name] > threshold]

        print("Filtered data: ")
        print(filtered_df)

        #give the user an option to save the filtered data set as an output_file

        if output_file:
            filtered_df.to_csv(output_file, index=False)
            print (f"Filtered data saved to {output_file}")

    except FileNotFoundError:
        print ("File could not be found")
    except Exception as e:
        print (f"Unexpected Error: {e}")
    except FileExistsError:
        print ("The file you specified does not exist")

file_path = input("Please enter complete file path: ")
column_name = input("Please enter the column name: ").lower()
treshold = float(input("Please specify the treshold: "))

filter_csv(file_path, column_name=column_name, threshold=treshold)