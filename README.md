# Billing Engine Challenge

Build a Python script which runs billing based on the input files attached.

We’ve got an issue here, we’ve started providing services for a handful of clients but have not
yet built the tools to calculate the final bill. We need your help figuring out a simple pythonic
solution for this !

## As input

This script will have to leverage 3 different input csv files and produce a single
csv file as its final output:

- The first of the inputs, `clients.csv`, contains client information, a basic numerical ID(Client ID), a
  name(Client Name), the currency name the final bill has to be issued on(Bill Currency), and the
  markup we keep as revenue(Service Rate)(based on bill currency).

- The second input, `platform_spend.csv`, is the report from the marketing platform we run ads for
  our clients on, first we have the client id and client name (which matches with clients.csv),
  campaign id and campaign name(we usually run multiple campaigns per client), the advertising
  cost for the campaign, and the currency spent.

- And third, `fx_rates.csv`, this is a double entry table containing the different exchange rates we
  will need, each row is the origin currency for the rate and the column is the destination currency
  of the rate, for example on row CHA, under column TOK, we have the value 0.25 which means
  1 CHA equals 0.25 TOK.

## As output

As for the output we just need `client id`, `client name`, `bill currency` and `total amount for the bill`,
one row per client will suffice. Client id, name and bill currency are the ones found on
clients.csv.

Total amount has to be calculated as the sum of the platform spend plus the service
rate markup, for example a client with a total spend of 300CHA and a rate of 0.01CHA would be
billed 303CHA. An important detail to keep in mind is client’s can spend on multiple currencies
different from the currency we have to bill them on, so a client can spend on CHA and TAZ but
be billed on TOK.

## Usage

- `requirements.txt`: Dependencies for this project are listed on this file.

- `venv`: For running a venv, open the console and type `BillingEngine/Scripts/activate.bat` for running venv activation file.

- `Functions`:

```python
import pandas as pd
from helpers import get_total_amount
from logs_handler import MediaMonksLogger
```

- `pandas` for dataframe handling.
- `helpers` for retrieving final dataframe.
- `logs_handler` for code status acknowledgment for developers. (`Loggers` could perfectly be omitted and/or replaced for `prints` statements, since loggers could be very resource consuming for large applications.)

- `main.py`: The main script. Here csv input files are uploaded using `read_csv` function. Make sure `files extensions are csv` before uploading and running the code.

- `helpers.py`: Functions `get_total_amount()`, `merge_dataframe()` and `calculate_total()` are defined in this script. Types of parameters and outputs are specified in each function.

```python
def get_total_amount(clients:pd.DataFrame, platform_spend:pd.DataFrame, fx_rates:pd.DataFrame) -> pd.DataFrame:

def merge_dataframes(df1:pd.DataFrame, df2:pd.DataFrame) -> pd.DataFrame:

def calculate_total(df1:pd.DataFrame, df2:pd.DataFrame) -> float:
```

- `logs_hanlder.py`: Loggers configuration is set in this script. A file called `logfile.log` containing timestamp and code acknowledge information is created in the project folder.

## Output

`final_spent.csv` is retrieved as the final output file, sorted by `Client ID`, `Client Name`, `Bill Currency`, `Service Rate` and `Total`.

## License

I [unlicense](https://unlicense.org/) everything in this repository.
