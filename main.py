import pandas as pd
from helpers import get_total_amount
from logs_handler import MediaMonksLogger

if __name__ == "__main__":
    
    # Init logger
    mmLogger = MediaMonksLogger(loggername="MediaMonksLogger", stream_logs=True).logger
    
    # Import csv files
    mmLogger.info("1) Uploading csv files...")
    clients = pd.read_csv("clients.csv")
    fx_rates = pd.read_csv("fx_rates.csv")
    platform_spend = pd.read_csv("platform_spend.csv")
    mmLogger.info("2) Csv files already uploaded.")

    # Create dataframes and variables for each client
    mmLogger.info("3) Calculating total amounts...")
    total_amount = get_total_amount(clients, platform_spend, fx_rates)
    mmLogger.info("4) Total amounts calculated.")
    
    # Create csv final file
    mmLogger.info("5) Creating final csv file...")
    total_amount.to_csv("final_spent.csv", index=False)
    mmLogger.info("6) Done! Final csv file was created.")
