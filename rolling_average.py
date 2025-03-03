import pandas as pd
from typing import Optional

def resample_and_rolling_average(input_file: str, date_column_name: str, target_quantity: str, time_period: int) -> Optional[pd.Series]:
    """
    Calculate the rolling average of a target quantity over a specified time period.

    Parameters:
    input_file (str): Path to the input CSV file.
    date_column_name (str): Name of the column containing date/time data.
    target_quantity (str): Name of the column to calculate the rolling average for.
    time_period (int): The window size for the rolling average.

    Returns:
    pd.Series: The rolling average of the target quantity.
    """
    try:
        # Read the CSV file
        df = pd.read_csv(input_file)

        # Convert the date column to datetime and set it as the index
        df[date_column_name] = pd.to_datetime(df[date_column_name])
        df.set_index(date_column_name, inplace=True)

        # Calculate the rolling average
        moving_average = df[target_quantity].rolling(window=time_period).mean()

        # Print the results
        print(f"Rolling average of '{target_quantity}' over a {time_period}-period window:")
        print(moving_average.dropna())  # Drop NaN values for cleaner output

        return moving_average

    except FileNotFoundError:
        print("Error: The input file could not be found.")
    except pd.errors.EmptyDataError:
        print("Error: The input file is empty.")
    except KeyError:
        print(f"Error: Column '{date_column_name}' or '{target_quantity}' not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def get_input_parameters():
    """
    Collect user input and call the resample_and_rolling_average function.
    """
    file_path = input("Please enter the file path: ").strip()
    date_column_name = input("Please enter the column name that corresponds to 'Date': ").strip()
    target_quantity = input("Please enter the quantity for which you'd like moving averages: ").strip()
    time_period = int(input("And the time period for moving averages? ").strip())

    resample_and_rolling_average(input_file=file_path, date_column_name=date_column_name,
                                 target_quantity=target_quantity, time_period=time_period)

# Main program
get_input_parameters()