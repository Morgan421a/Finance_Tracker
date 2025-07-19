import csv
import os
from pathlib import Path


headers = ["Name", " Merchant", " Amount", " Category", " Description", " Date"]

base_dir = Path(__file__).resolve().parent.parent
csv_file_path = base_dir / "ExpenseData.csv"

def file_creation():
    try:
        with open(csv_file_path, "x", newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(headers)
    except FileExistsError:
        pass

def filewriter(name, expense):
    with open(csv_file_path, "a") as csvfile: 
        writer = csv.writer(csvfile)
        writer.writerow([name, expense.merchant, expense.amount, expense.category, expense.description, expense.date])     



    

