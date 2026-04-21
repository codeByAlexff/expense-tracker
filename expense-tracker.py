import argparse
import csv
import os
from datetime import datetime
import pandas as pd


filename = "expenses.csv"
header_data = ['ID', 'Date', 'Description', 'Amount']

def add_expense(args):
    file_exists = os.path.isfile(filename)

    with open(filename, 'a', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=header_data)
    
        if not file_exists:
            writer.writeheader()
    
        writer.writerow({
            'ID': generate_id(filename),
            'Date': datetime.now().strftime('%Y-%m-%d'),
            'Description': args.description,
            'Amount': args.amount
        })

        print(f"Expense added successfully (ID: {generate_id})")

def generate_id(filename):
    if not os.path.isfile(filename):
        return 1

    df = pd.read_csv(filename)
    if df.empty:
        return 1
    
    return int(df['ID'].max()) + 1
    

def delete_expense(args):
    df = pd.read_csv(filename)
    df = df[df['ID'] != int(args.id)]

    df.to_csv(filename, index=False)

    print(f"Expense deleted successfully")

def summary_expense(args):
    df = pd.read_csv(filename)
    total = df['Amount'].sum()
    print(f"Total expenses: ${total}")


def list_expense(args):
    df = pd.read_csv(filename)
    print(df)
                

#Main Parses
parser = argparse.ArgumentParser(description="CLI Expense Tracker")
parser.add_argument("--month", help="Month of expense")
parser.add_argument("--year", help="Year of expense")
parser.add_argument("--day", help="Day of expense")
parser.add_argument("--id", help="ID of expense")

subparsers = parser.add_subparsers(dest='command', help='Available commands', required=True)

#Command 1: Add
add_parser = subparsers.add_parser('add', help="Add expense")
add_parser.add_argument("--description", help="Describe the expense", required=True)
add_parser.add_argument("--amount", help="Amount of the expense", type=float, required=True)
add_parser.set_defaults(func=add_expense)

#Command 2: Delete
delete_parser = subparsers.add_parser("delete", help="Delete expense")
delete_parser.add_argument("--id", help="ID of expense")
delete_parser.set_defaults(func=delete_expense)


#Command 3: List
list_parser = subparsers.add_parser("list", help="List all expenses")
list_parser.set_defaults(func=list_expense)

#Command 4: Summary
summary_parser = subparsers.add_parser("summary", help="Calculate total expenses")
summary_parser.set_defaults(func=summary_expense)

#Parse Arguments
args = parser.parse_args()


if hasattr(args, 'func'):
    args.func(args)
    