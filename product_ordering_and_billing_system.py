# Products catalog
products = {
    "Product A": 20,
    "Product B": 40,
    "Product C": 50 
}

# Discount rules
discount_rules = {
    'flat_10_discount': (200, 10),
    'bulk_5_discount': (10, 5),
    'bulk_10_discount': (20, 10),
    'tiered_50_discount': (30, 50)
}

# Product quantities and gift wrap for each product
product_quantities = {}
is_gift_wrapped = {}

# Enter quantities and gift wrap option for each product
for product_item, price in products.items():
    quantity = int(input(f"Enter the quantity of {product_item}: {price} rupees\n"))
    product_quantities[product_item] = quantity
    if quantity > 0:
        gift_wrap = input(f"Add gift wrap for {product_item}? (y/n): ").lower() == 'y'
        is_gift_wrapped[product_item] = gift_wrap
    else:
        is_gift_wrapped[product_item] = False
        
# Calculate subtotal
subtotal = sum(products[product_item] * quantity for product_item, quantity in product_quantities.items())

# Calculating discounts if applicable
discount_amounts = {}
discount_name = ''
discount_amount = 0

for discount_rule, (condition, discount) in discount_rules.items():
    if discount_rule == "flat_10_discount":
        if subtotal > condition:
            discount_amounts[discount_rule]=discount
    elif discount_rule == "bulk_5_discount":
        if any(quantity > condition for quantity in product_quantities.values()):
            discount_amounts[discount_rule]=sum(products[product_item] * quantity for product_item, quantity in product_quantities.items() if quantity > condition) * discount / 100
    elif discount_rule == "bulk_10_discount":
        if sum(product_quantities.values()) > condition:
            discount_amounts[discount_rule]=subtotal * discount / 100
    elif discount_rule == "tiered_50_discount":
        tiered_50_discount=0
        if sum(product_quantities.values()) > condition and any(quantity > 15 for quantity in product_quantities.values()):
            for product_item, quantity in product_quantities.items():
               if quantity > 15:
                    discounted_quantity = quantity - 15
                    tiered_50_discount+=products[product_item] * discounted_quantity * 50 / 100
            discount_amounts[discount_rule]= tiered_50_discount

# Dictionary of all applicable discounts
# print(discount_amounts)

# Output details & calculations
print("Product Details:")
for product_item, quantity in product_quantities.items():
    print(f"{product_item}: Quantity - {quantity}, Total Amount - {products[product_item] * quantity}")

# Subtotal
print("Subtotal:", subtotal)

# Selecting most beneficial discount for customer
if discount_amounts:
    discount_name, discount_amount = max(discount_amounts.items(), key=lambda x: x[1])
    print("Discount Applied:", discount_name)
    print("Discount Amount:", discount_amount)
else:
    print("No discounts applicable.")

# Calculate shipping fee
shipping_fee = 5 * ((sum(product_quantities.values()) - 1) // 10 + 1)
print("Shipping Fee:", shipping_fee)

# Calculate gift wrap fee
gift_wrap_fee = sum(quantity for product_item, quantity in product_quantities.items() if is_gift_wrapped[product_item])
print("Gift Wrap Fee:", gift_wrap_fee)

# Calculate total
total = subtotal - discount_amount + gift_wrap_fee + shipping_fee
print(f"Total: {total} \n Thank you! \U0001F603")
# \U0001F603 represents the Unicode code point for the "happy face" emoji.
