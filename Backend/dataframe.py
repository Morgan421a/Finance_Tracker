import pandas as pd
import datetime
import locale

dataframe = pd.read_csv("../ExpenseData.csv")

locale.setlocale(locale.LC_TIME, "")

def_date = datetime.datetime.now().strftime("%x")

dataframe[" Date"].fillna(def_date, inplace = True)

dataframe.fillna("N/A", inplace = True)

print(dataframe)

