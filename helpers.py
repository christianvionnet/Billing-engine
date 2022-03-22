import pandas as pd
import logging

# Encharges of getting total amount for each client
def get_total_amount(clients:pd.DataFrame, platform_spend:pd.DataFrame, fx_rates:pd.DataFrame) -> None:

    try:
        # Merge dataframes
        client = merge_dataframes(clients, platform_spend)

        # Create dinamically a dictionary with each client's name as key
        names = client["Client Name"].unique()
        client_list = {}
        for name in names:
            client_list[name] = client[client["Client Name"] == name]
        
        # Apply calculate_total() to each client dataframe
        for client in client_list:
            client_list[client]["Total"] = client_list[client].apply(lambda row: calculate_total(row,fx_rates), axis=1)
        
        # Create final column with all total amounts
        total = {}
        for client in client_list:
            print(client_list[client]["Total"].sum() * (1+client_list[client]["Service Rate"]))
            total[client] = client_list[client]["Total"].sum() * (1+client_list[client]["Service Rate"])
            
        return total
    
    except Exception as e:
        print(f"An error has ocurred while executing the program: {e}")
        
# Encharges of merging datafremes into only one
def merge_dataframes(df1:pd.DataFrame, df2:pd.DataFrame) -> pd.DataFrame:
    
    return pd.merge(left=df1, right=df2, how='left') 

# Encharges of calculating each client total
def calculate_total(df1:pd.DataFrame, df2:pd.DataFrame) -> float:
    
    logging.info("Entering calculate_total()...")
    
    df2.index = df2["Origin Currency"]
    
    currencies = df2["Origin Currency"].unique()
    
    total = 0

    for currency in currencies:
        
        if(df1.loc["Currency"] == currency):
            total = total + df1.loc["Advertising Cost"] / df2.loc[df1.loc["Bill Currency"],currency]

    logging.info("Exiting calculate_total()")            
    return total