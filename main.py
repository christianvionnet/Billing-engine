# -*- coding: utf-8 -*-

import logging
import pandas as pd
from helpers import get_total_amount


if __name__ == "__main__":
    
    # Import csv files
    logging.info("Uploading csv files...")
    clients = pd.read_csv("clients.csv")
    fx_rates = pd.read_csv("fx_rates.csv")
    platform_spend = pd.read_csv("platform_spend.csv")

    # Create dataframes and variables for each client
    logging.info("Calculating total amounts...")
    total_amount = get_total_amount(clients, platform_spend, fx_rates)
    logging.info("Total amounts calculated.")
    
    # Create csv final file
    logging.info("Creating final csv file...")
    total_amount_df = pd.DataFrame(total_amount)
    total_amount_df.to_csv("final_spent.csv", index=False)
    logging.info("Done! Final csv file was created.")
