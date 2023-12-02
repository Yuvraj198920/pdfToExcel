import re

def parse_statement(text):
    transactions = []
    lines = text.split('\n')
    print(lines)
    for line in lines:
        if re.match(r'\d{2}/\d{2}/\d{4}', line):
            parts = line.split(' ')
            date = parts[0]
            amount = parts[-1]
            description = ' '.join(parts[1:-1])
            transactions.append((date, description, amount))
    return transactions
