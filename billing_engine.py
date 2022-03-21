# -*- coding: utf-8 -*-

import pandas as pd

#Import csv files
clients = pd.read_csv("clients.csv")
fx_rates = pd.read_csv("fx_rates.csv")
platform_spend = pd.read_csv("platform_spend.csv")

#Create dinamically dataframes and variables for each client
for i in range(len(clients)):
    exec ("client_%s = clients.loc[[i]]" % (i))
    exec ("total_client_%s = 0" % (i))

#Service rate factor for each client
rate_0 = client_0.loc[0,"Service Rate"] + 1
rate_1 = client_1.loc[1,"Service Rate"] + 1
rate_2 = client_2.loc[2,"Service Rate"] + 1

#Function encharges of calculating total amount for each client
def total_amount(x:object) -> None:
    
    global total_client_0
    global total_client_1
    global total_client_2
    
    #Ask for client C3P0 Ads
    if ( client_0.loc[0,"Client Name"] in x["Client Name"] ):
        
        #Ask for proper currency
        if (x.loc["Currency"] == client_0.loc[0,"Bill Currency"]):
            total_client_0 = total_client_0 + x.loc["Advertising Cost"]           
        #If not, converts to proper one
        else:
            #Ask for TAZ
            if (x.loc["Currency"] == client_1.loc[1,"Bill Currency"]):
                total_client_0 = total_client_0 + (x.loc["Advertising Cost"] * fx_rates.loc[1,client_0.loc[0,"Bill Currency"]]) 
            #Ask for TOK
            elif (x.loc["Currency"] == client_2.loc[2,"Bill Currency"]):
                total_client_0 = total_client_0 + (x.loc["Advertising Cost"] * fx_rates.loc[2,client_0.loc[0,"Bill Currency"]])
     
    #Ask for client Costa Atlantica    
    if ( client_1.loc[1,"Client Name"] in x["Client Name"] ):
        
        #Ask for proper currency
        if (x.loc["Currency"] == client_1.loc[1,"Bill Currency"]):
            total_client_1 = total_client_1 + x.loc["Advertising Cost"]
        #If not, converts to proper one
        else:
            #Ask for CHA
            if (x.loc["Currency"] == client_0.loc[0,"Bill Currency"]):
                total_client_1 = total_client_1 + (x.loc["Advertising Cost"] * fx_rates.loc[0,client_1.loc[1,"Bill Currency"]])
            #Ask for TOK
            elif (x.loc["Currency"] == client_2.loc[2,"Bill Currency"]):
                total_client_1 = total_client_1 + (x.loc["Advertising Cost"] * fx_rates.loc[2,client_1.loc[1,"Bill Currency"]])

    #Ask for Only Programmatic Marketing
    if ( client_2.loc[2,"Client Name"] in x["Client Name"] ):
        
        #Ask for proper currency
        if (x.loc["Currency"] == client_2.loc[2,"Bill Currency"]):
            total_client_2 = total_client_2 + x.loc["Advertising Cost"]
        #If not, converts to proper one
        else:
            #Ask for TAZ
            if (x.loc["Currency"] == client_1.loc[1,"Bill Currency"]):
                total_client_2 = total_client_2 + (x.loc["Advertising Cost"] * fx_rates.loc[1,client_2.loc[2,"Bill Currency"]]) 
            #Ask for CHA
            elif (x.loc["Currency"] == client_0.loc[0,"Bill Currency"]):
                total_client_2 = total_client_2 + (x.loc["Advertising Cost"] * fx_rates.loc[0,client_2.loc[2,"Bill Currency"]])
    
try:
    total = platform_spend[["Client Name","Advertising Cost","Currency"]].apply(lambda x: total_amount(x),axis=1) 
    clients["Total Spent"] = [total_client_0*rate_0, total_client_1*rate_1, total_client_2*rate_2]
    #Create final csv file with total spent for each client
    clients.to_csv("final_spent.csv")
    
except:
    print("There was an error. Please refresh the app.")