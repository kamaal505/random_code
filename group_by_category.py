import pandas as pd

def category_mean (input_file, category, target_quantity):

    try:
        df = pd.read_csv(input_file)
        #check if the category exists
        if category.lower() not in map(str.lower, df.columns):
            print(f"Error: {category} not present in the csv")
            return
        #check if the quantity is in the file
        if target_quantity.lower() not in map(str.lower, df.columns):
            print(f"Error: {target_quantity} not present in the csv")
            return
        # Check if the target quantity column is numeric
        if not pd.api.types.is_numeric_dtype(df[target_quantity]):
            print(f"Error: Column '{target_quantity}' must contain numeric data.")
            return
        
        #time to group by the category and calculate the average for each sub_category

        df_grouped = df.groupby(category)[target_quantity].mean()
        print(df_grouped)

    except FileNotFoundError:
        print("File not found")
    except pd.errors.EmptyDataError:
        print("Input file empty")
    except Exception as e:
        print(f"Unknown error e")

input_file = input("Please enter complete file path: ").strip()
category = input("Please enter the category by which you'd like to group the data set: ")
target_quantity = input("Plase enter the quantity you'd like the average for: ")
category_mean(input_file=input_file, category=category, target_quantity=target_quantity)