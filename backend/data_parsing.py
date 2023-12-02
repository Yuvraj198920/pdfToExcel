# data_parsing.py
import re

def convert_amount_to_number(amount_str):
    # Remove any commas and convert to float
    amount_str = amount_str.replace(',', '')
    try:
        return float(amount_str)
    except ValueError:
        # Handle the case where the conversion fails
        print(f"Error converting amount: {amount_str}")
        return 0.0
    
def parse_transactions(ocr_text):
    transactions = []
    lines = ocr_text.split('\n')
    for line in lines:
        # Adjust the regex pattern based on the actual OCR output format
        match = re.match(r'(\d{2} \w{3}) (.*?) ([\d,]+\.\d{2})', line)
        if match:
            date, description, amount_str = match.groups()
            # Convert amount to a number
            amount = convert_amount_to_number(amount_str)
            transactions.append((date, description, amount))
    return transactions
