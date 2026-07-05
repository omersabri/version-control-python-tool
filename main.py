from helper import calculate_total, generate_summary

price = 5
quantity = 3

total = calculate_total(price, quantity)

print(f"The total is £{total}")
print(generate_summary(total))