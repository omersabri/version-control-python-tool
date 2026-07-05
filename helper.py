def calculate_total(price, quantity):
    return price * quantity * 10


def generate_summary(total):
    return f"Summary: the final total is £{total}"

def average_score(scores):
    return sum(scores) / len(scores)