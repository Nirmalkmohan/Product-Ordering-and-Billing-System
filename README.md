# Product-Ordering-and-Billing-System
This is a Python program that allows users to enter product quantities and select gift wrap options for each product. It calculates the subtotal based on the product prices and quantities, applies applicable discounts based on predefined rules, and calculates the shipping fee and gift wrap fee. Finally, it provides the total amount to be paid by the customer.

<h3>Features</h3>
Enter quantities and gift wrap option for each product.<br>
Calculates subtotal based on the product prices and quantities.<br>
Applies discounts based on predefined rules.<br>
Considers bulk discounts, tiered discounts, and flat discounts.<br>
Calculates shipping fees based on the total quantity.<br>
Calculates gift wrap fees based on the selected options.<br>
Provides a detailed summary of the product details and amounts.<br>
Displays the total bill amount after applying discounts and adding shipping and gift wrap fees.<br>

<h3>Description</h3>
The program have a product catalog with corresponding prices. <br>
Defined discount rules with a specific condition and discount.  <br>
User need to enter Quantity for each product and an option for gift wrap (for each unit) <br>
The program iterates over the discount rules and checks if the conditions are met. For each applicable rule, the program calculates the discount amount based on the corresponding logic:  <br>

<h4>Flat 10% Discount:</h4> If the subtotal exceeds $200, a flat $10 discount is applied to the total amount.  <br>
<h4>Bulk 5% Discount:</h4> If the quantity of any single product exceeds 10 units, a 5% discount is applied to that item's total price. <br>
<h4>Bulk 10% Discount:</h4> If the total quantity of all products exceeds 20 units, a 10% discount is applied to the total amount. <br>
<h4>Tiered 50% Discount:</h4> If the total quantity of all products exceeds 30 units and any single product quantity is greater than 15, a 50% discount is applied to the excess quantity above 15 units. <br>

The calculated discount amounts are stored in a dictionary (discount_amounts). <br>
If any discounts are applicable (discount_amounts is not empty), the program selects the most beneficial discount by choosing the one with the highest discount amount. It displays the applied discount name and amount.<br>
The program calculates the shipping fee based on the total quantity of products. It adds $5 for every 10 units.<br>
The program calculates the gift wrap fee by summing the quantities of products that have the gift wrap option selected.<br>
The program calculates the total amount by subtracting the discount amount from the subtotal and adding the shipping fee and gift wrap fee.<br>
 The program displays the product details, including the quantities and total amounts for each product, subtotal,  shipping fee, gift wrap fee, and the final total amount. It also includes a cheerful message and a smiley face emoji to signify completion.<br>
 
<h3>Usage</h3>
Run the Python program.<br>
Enter the quantity for each product when prompted.<br>
Choose the gift wrap option for each product (y/n)<br>
