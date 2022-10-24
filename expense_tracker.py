'''Creates an expenses CSV file in the format of:
Date    Category    Cost'''
import csv

def read_expenses():
    try:
        with open("expenses.csv", "r") as f:
            csv_reader = csv.reader(f, delimiter=",")
            expenses = []
            for row in csv_reader:
                expenses.append(row)
        # expenses come in the columns of date (0), category (1), price (2)
        for line in expenses:
            print(f"On {line[0]}, {line[2]} was spent on {line[1]}")
    except:
        print("No Expense Tracker File Exists Yet")

def write_expenses():
    reporting = True
    f = open("expenses.csv", "a")
    expense_writer = csv.writer(f, delimiter=",")
    while reporting:
        date = input("What date was the expense incurred? ")
        category = input("What category is the expense for? ")
        cost = input("How much money did you spend? ")
        expense_writer.writerow([date, category, cost])
        end = input("If you are done inputting expenses, type \"end\" ")
        if end == "end":
            reporting = False

    f.close()

print("Current state of expense report: ")
read_expenses()
report = input("Would you like to report expenses?(y/n) ")
if report == "y":
    write_expenses()
