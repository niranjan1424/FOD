item_prices = [2.5, 1.99, 3.25, 4.5]
item_quantities = [3, 2, 1, 4]
discount_rate = 10
tax_rate = 8
subtotal = sum(item_price * item_quantity for item_price, item_quantity in zip(item_prices, item_quantities))
discount_amount = (discount_rate / 100) * subtotal
total_after_discount = subtotal - discount_amount
tax_amount = (tax_rate / 100) * total_after_discount
final_total_cost = total_after_discount + tax_amount

print("Final Total Cost:", final_total_cost)
