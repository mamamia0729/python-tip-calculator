# --- Tiny Tip Calculator ---

print("Welcome to the Tiny Tip Calculator!")

# 1. Get User Input
# Using float() for monetary values to allow for decimals
bill_total_str = input("What was the total bill amount? $")
bill_total = float(bill_total_str)

tip_percentage_str = input("What percentage tip would you like to give? (e.g., 15 for 15%) ")
tip_percentage = float(tip_percentage_str)

num_people_str = input("How many people are splitting the bill? ")
num_people = int(num_people_str) # Using int() as you can't split with half a person

# 2. Calculate Tip Amount
# Operator precedence: division happens before multiplication, but parentheses ensure percentage is calculated first
tip_amount = bill_total * (tip_percentage / 100)

# 3. Calculate Total Bill with Tip
total_bill_with_tip = bill_total + tip_amount

# 4. Calculate Amount Per Person
# Using round() to ensure the amount per person is displayed nicely with 2 decimal places
amount_per_person = round(total_bill_with_tip / num_people, 2)

# 5. Display Results
print("\n--- Calculation Summary ---")
print(f"Original Bill: ${bill_total:.2f}") # Formats to 2 decimal places
print(f"Tip Percentage: {tip_percentage}%")
print(f"Calculated Tip Amount: ${tip_amount:.2f}")
print(f"Total Bill (including tip): ${total_bill_with_tip:.2f}")
print(f"Number of people splitting: {num_people}")
print(f"Each person should pay: ${amount_per_person:.2f}")
print("--------------------------")

print("Thank you for using the Tiny Tip Calculator!")
