#Use the .get() method to safely access the price of 'grape' from the dictionary {'apple': 50, 'banana': 20, 'orange': 30}.
fruit_prices = {'apple': 50, 'banana': 20, 'orange': 30}
grape_price = fruit_prices.get('grape', 'Not found')
print(grape_price)