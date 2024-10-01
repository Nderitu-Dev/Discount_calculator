def calculate_discount(price, discount_percentage):
    if discount_percentage >= 20:
        discount_amount = price * (discount_percentage / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price
#user input prompt
    original_price = float(input("Enter original item price"))
    discount_percentage = float(input("Enter discount percentage"))

    final_price = calculate_discount(original_price, discount_percentage)

    if final_price < original_price:
        print(f"Final price after the discount is: ${final_price:.2f}")
    else:
        price(f"No discount applied. Te original price is: ${original_price:.2f}")