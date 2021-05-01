print('Price for 1 item is 10.95 $\nPrice for each subsequent item is 2.95 $')
q = int(input('Enter the quantity of items: '))
def shipping_calc(quantity):
    if q == 1:
        return 10.95
    if q>1:
        return 10.95 + 2.95*(q-1)
print(f'Price for {q} items is', shipping_calc(q), '$')