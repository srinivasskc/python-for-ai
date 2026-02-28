# calculate the total for single item
def calculate_total(quantity,price):
    return quantity*price

def format_currency(amount):
    # Format number as currency
    return f"${amount:,.2f}"
