from openpyxl import Workbook

def create_excel(transactions, filename="transactions.xlsx"):
    wb= Workbook()
    ws = wb.active
    ws.title = "Transactions"

    # Add headers
    ws.append(["Date", "Description", "Amount"])

    #Add transaction data
    for transaction in transactions:
        ws.append(transaction)

    wb.save(filename)