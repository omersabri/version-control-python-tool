from helper import calculate_total, generate_summary


def main():
    price = 5
    quantity = 3

    total = calculate_total(price, quantity)

    print(f"The total is £{total}")
    print(generate_summary(total))


if __name__ == "__main__":
    main()