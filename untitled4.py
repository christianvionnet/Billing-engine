# -*- coding: utf-8 -*-
import pandas as pd

#Function encharges of calculating total amount for each client
def get_total_amount(clients:pd.DataFrame, platform_spend:pd.DataFrame, fx_rates:pd.DataFrame) -> None:

    try:
        
        # Merge dataframes
        client = merge_dataframes(clients, platform_spend)
        
        # Create dinamically each client
        nombres = client["Client Name"].unique()
        client_list = {}
        for nombre in nombres:
            client_list[nombre] = client[client["Client Name"]==nombre]
          
        # Apply calculate_total to each client dataframe
        for client in client_list:
            client_list[client].apply(lambda element: calculate_total(element,fx_rates), axis=1)
        
    except Exception as e:
        print(f"An error has ocurred while executing the program: {e}")
  

  
def merge_dataframes(df1:pd.DataFrame, df2:pd.DataFrame) -> pd.DataFrame:
    
    return pd.merge(left=df1, right=df2, how='left') 



def calculate_total(df1:pd.DataFrame, df2:pd.DataFrame) -> None:
    
    df2.index = df2["Origin Currency"]
    #df2.drop(["Origin Currency"], axis = 1, inplace=True)
        
    currencies = df2["Origin Currency"].unique()
    ##print(currencies)
    
    total = 0

    if(df1.loc["Currency"] == df1.loc["Bill Currency"]):
        total = total + df1.loc["Advertising Cost"]
        print("Total if: ",total)
        return total

    else:
        for currency in currencies:
            # TAZ
            if(df1.loc["Currency"] == currency):
                total = total + df1.loc["Advertising Cost"] / df2.loc[df1.loc["Bill Currency"],currency]
                print ("Total else: ", total)
                return total
            
            
            
            
            
                
    if(df1.loc["Currency"] == df1.loc["Bill Currency"]):
        total = total + df1.loc["Advertising Cost"]
        print("Total if: ",total)
        #return total

    else:
        for currency in currencies:
            # TAZ
            if(df1.loc["Currency"] == currency):
                total = total + df1.loc["Advertising Cost"] / df2.loc[df1.loc["Bill Currency"],currency]
                print ("Total else: ", total)
                #return total
    print("**************** Total total: ", total)            
    return total