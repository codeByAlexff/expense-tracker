# Expense Tracker CLI

A command-line expense tracking application that allows you to easily manage your finances. Add, delete, list, and summarize your expenses with a simple and intuitive CLI interface.

This project was made following roadmap.sh:
https://roadmap.sh/projects/expense-tracker

## Features

- **Add Expenses** — Record new expenses with description and amount
- **Delete Expenses** — Remove expenses by ID
- **List Expenses** — View all expenses in a formatted table
- **Calculate Totals** — Get a summary of all your expenses
- **Auto ID Generation** — Automatic unique ID assignment for each expense
- **Date Tracking** — Automatically records the date of each expense
- **CSV Storage** — Data stored in a simple CSV file for easy export

## Requirements

- Python 3.7+
- pandas
- No external APIs or databases needed

## Usage

### Add an Expense

```bash
python3 expense-tracker.py add --description "Groceries" --amount 50.00
```

**Output:**
```
Expense added successfully (ID: 1)
```

### Delete an Expense

```bash
python3 expense-tracker.py delete --id 1
```

**Output:**
```
Expense deleted successfully
```

### List All Expenses

```bash
python3 expense-tracker.py list
```

**Output:**
```
   ID        Date        Description  Amount
0   1  2024-04-21          Groceries    50.0
1   2  2024-04-21               Gas    45.5
2   3  2024-04-22  Electric Bill    120.0
```

### Get Summary (Total Expenses)

```bash
python3 expense-tracker.py summary
```

**Output:**
```
   ID        Date        Description  Amount
0   1  2024-04-21          Groceries    50.0
1   2  2024-04-21               Gas    45.5
2   3  2024-04-22  Electric Bill    120.0
Total expenses: $215.5
```

## Commands

### `add` — Add a new expense

```bash
python3 expense-tracker.py add --description "DESCRIPTION" --amount AMOUNT
```

**Required arguments:**
- `--description` — Description of the expense
- `--amount` — Amount spent (as a number)

**Example:**
```bash
python3 expense-tracker.py add --description "Coffee" --amount 5.50
python3 expense-tracker.py add --description "Netflix subscription" --amount 15.99
```

### `delete` — Delete an expense by ID

```bash
python3 expense-tracker.py delete --id ID
```

**Required arguments:**
- `--id` — ID of the expense to delete

**Example:**
```bash
python3 expense-tracker.py delete --id 2
```

### `list` — Display all expenses

```bash
python3 expense-tracker.py list
```

Shows a formatted table of all expenses with ID, Date, Description, and Amount.

### `summary` — Calculate total expenses

```bash
python3 expense-tracker.py summary
```

Shows all expenses and displays the total amount spent.

## Data Storage

Expenses are stored in `expenses.csv` with the following columns:

```
ID,Date,Description,Amount
1,2024-04-21,Groceries,50.0
2,2024-04-21,Gas,45.5
3,2024-04-22,Electric Bill,120.0
```

The CSV file is automatically created on first use.

## How It Works

1. **Add Expense** — Records the expense with auto-generated ID and current date
2. **Generate ID** — Automatically finds the next available ID based on existing data
3. **Store in CSV** — Data is saved to `expenses.csv` using pandas and CSV modules
4. **Delete by ID** — Filters out the specified expense and rewrites the CSV
5. **List/Summary** — Reads the CSV and displays the data using pandas

## File Structure

```
expense-tracker/
├── expense-tracker.py    # Main application
├── expenses.csv          # Data file (auto-created)
└── README.md            # This file
```

## Future Improvements

- Category filtering (food, transport, utilities, etc.)
- Date range filtering
- Export to PDF or Excel
- Monthly/yearly reports
- Budget alerts
- Recurring expenses
- Web interface with Flask
- Database integration (SQLite, PostgreSQL)

## Troubleshooting

### `ModuleNotFoundError: No module named 'pandas'`
Install pandas:
```bash
pip install pandas
```

### `FileNotFoundError: expenses.csv`
Run the `add` command to create the file:
```bash
python3 expense-tracker.py add --description "Test" --amount 10
```

### Invalid ID when deleting
Make sure you're using a valid ID from your expense list:
```bash
python3 expense-tracker.py list  # Check valid IDs first
python3 expense-tracker.py delete --id 1
```

## License

This project is open source and available under the MIT License.

## Author

[codeByAlexff](https://github.com/codeByAlexff)
