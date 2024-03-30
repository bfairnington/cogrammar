"""
Practical Task
Follow these steps:
● Imagine you are running a cafe. Create a new Python file in your folder
called cafe.py.
● Create a list called menu, which should contain at least four items sold in
the cafe.
● Next, create a dictionary called stock, which should contain the stock
value for each item on your menu.
● Create another dictionary called price, which should contain the prices for
each item on your menu.
● Next, calculate the total_stock worth in the cafe. You will need to
remember to loop through the appropriate dictionaries and lists to do
this.
Tip: When you loop through the menu list, the ‘items’ can be set as keys
to access the corresponding ‘stock’ and ‘price’ values. Each ‘item_value’ is
calculated by multiplying the stock value by the price value. For example:
item_value = (stock[items] * price[items])
● Finally, print out the result of your calculation.
"""

# Create menu
menu = ["Tea", "Coffee", "Water", "Coke"]

# Create stock values
stock = {"Tea": 150,
         "Coffee": 200,
         "Water": 50,
         "Coke": 100}

# Create prices
price = {"Tea": 2.00,
         "Coffee": 2.50,
         "Water": 1.50,
         "Coke": 1.80}

# Calculate total stock
total_stock = 0
for keys_stock, values_stock in stock.items():
    for keys_price, values_price in price.items():
        if keys_stock == keys_price:
            total_stock += values_stock * values_price

print(f"The total value of all stock in the cafe is {total_stock}.")

questions = [["What color is the daytime sky on a clear day? ", "blue"],
            ["What is the answer to life, the universe and everything? ", "42"],
            ["What is a three letter word for mouse trap? ", "cat"]]

# Check if there are any questions in the questions list
print(len(questions))
 





