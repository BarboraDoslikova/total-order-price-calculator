''' The program calculates the total price of an order for one item, which can be discounted, with two categories of shipping costs.
For example, if you sell your book at a 20% discount from the original price of 50.00 CAD and want to ship the first 10 copies for 10.00 CAD and the next 90 copies at 5.00 CAD,
the total price of the order will be 4550.00 CAD.
'''

name = input('Enter your item\'s name: ')

price = input('Enter your item\'s price in CAD: ')
price = float(price)

discount = input('Enter your item\'s discount as a %: ')
discount = (float(discount))/(100) * price

discounted_price = price - discount


shipping_cost_1 = input('Enter your item\'s first shipping category cost in CAD: ')
shipping_cost_1 = float(shipping_cost_1)

no_items_shipped_1 = input('Enter the number of items you want to ship at the first shipping category cost: ')
no_items_shipped_1 = float(no_items_shipped_1)

shipping_cost_2 = input('Enter your item\'s second category shipping cost in CAD: ')
shipping_cost_2 = float(shipping_cost_2)

no_items_shipped_2 = input('Enter the number of items you want to ship at the second category shipping cost: ')
no_items_shipped_2 = float(no_items_shipped_2)

print ('')

def count_total(d, c1, n1, c2, n2):
    total = 0
    if d <= 0:
        print ("Your item cannot cost 0.0 CAD.")
    else:
        total = ((d + c1) * n1) + ((d + c2) * n2)
    return float(total)

print ('Sooo... the total price to pay for the order is', count_total(discounted_price, shipping_cost_1, no_items_shipped_1, shipping_cost_2, no_items_shipped_2), 'CAD.')

''' To improve:
Make this useful either for the seller OR the buyer!
Handle errors better...
'''
