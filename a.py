def add_product(product):

    # atvēram failu
    products_file = open('products.txt', 'r', encoding='utf-8')
    # nolasām failu
    products = products_file.read().split('\n')
    # aizvēram failu
    products_file.close()


    if product in products:

        cart_file = open('cart.txt', 'a', encoding='utf-8')
        cart_file.write(product + '\n')
        cart_file.close()

        print('Produkt tika ielikts grozā!')

    else:
        print('Diemžēl produkts nav pieejams :(')
    


def remove_product(product):

    # dabūt sarakstu ar grozu
    # izdzēst no saraksta
    # ievietot failā jaunu sarakstu

    cart_file = open('cart.txt', 'r', encoding='utf-8')
    cart = cart_file.read().split('\n')
    cart_file.close()

    if product in cart:

        cart.remove(product)

        cart_file = open('cart.txt', 'w', encoding='utf-8')
        cart_file.writelines(cart)
        cart_file.close()

        print('Produkt tika izņemts no groza!')

    else:
        print('Produkts nav grozā :(')


while True:

    print("Actions: 'add', 'remove', 'stop' ")
    action = input('Action: ')

    if action == 'add':
        add_product(product=input('Enter product: '))

    elif action == 'remove':
        remove_product(product=input('Enter product: '))

    elif action == 'stop':
        quit()








print(a)