# --- Item 1 Details ---
item1_name = "Apples"
item1_price = 4.99
item1_qty = 2

# --- Item 2 Details ---
item2_name = "Bread"
item2_price = 2.50
item2_qty = 3

# --- Item 3 Details ---
item3_name = "Coffee"
item3_price = 10.00
item3_qty = 1

# --- Calculations ---
item1_total = item1_price * item1_qty
item2_total = item2_price * item2_qty
item3_total = item3_price * item3_qty

subtotal = item1_total + item2_total + item3_total

# Sales tax calculation (e.g., 8.875% tax rate)
tax_rate = 0.08875
sales_tax = subtotal * tax_rate

final_total = subtotal + sales_tax

# --- Receipt Output ---
print("========== STORE RECEIPT ==========")

print(item1_name + ": " + str(item1_qty) + " x $" + str(item1_price) + " = $" + str(item1_total))
print(item2_name + ": " + str(item2_qty) + " x $" + str(item2_price) + " = $" + str(item2_total))
print(item3_name + ": " + str(item3_qty) + " x $" + str(item3_price) + " = $" + str(item3_total))

print("-----------------------------------")
print("Subtotal:     $" + str(subtotal))
print("Sales Tax:    $" + str(sales_tax))
print("TOTAL:        $" + str(final_total))
print("===================================")
print("     Thank you for shopping!       ")
print("===================================")