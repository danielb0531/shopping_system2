import datetime #imports the datetime module so the receipt can show today's date

products = { #dictionary that holds the store inventory, product names are the keys and prices are the values
    "apple": 1.00,
    "banana": 0.50,
    "orange": 0.80,
    "grapes": 2.00,
    "mango": 1.50
}
shopping_cart = {} #this stays empty at first since the user has not added any products to the cart yet, product names will be the keys and quantities will be the values
checkout = False #this variable is used to control the "main loop" of the program, which will keep running until the user chooses to checkout


def get_number(prompt, low, high): #reusable function that keeps asking until the user enters a whole number from low to high
    answer = input(prompt).strip() #gets the user's answer as a string and removes extra spaces
    while not answer.isdigit() or int(answer) < low or int(answer) > high: #keeps looping if the answer is not a whole number or is outside the allowed range
        print(f"Invalid input. Enter a whole number from {low} to {high}.") #tells the user what went wrong
        answer = input(prompt).strip() #asks the user again
    return int(answer) #turns the valid answer into an integer and sends it back


def display_products(): #shows every product in the store and its price
    print("======= Available Products =======")
    if products == {}: #this is if there is nothing in the products dictionary
        print("No products available.") #tells the user there is nothing to show
    else:
        for product, price in products.items(): #.items() gives each product name and its price from the products dictionary
            print(f"- {product} - ${price:.2f}") #the :.2f format specifier is used to display the price with two decimal places
            print(" ")


def add_product(): #lets the user pick a product and how many they want
    print("======= Add Product to Cart =======")
    if products == {}: #this is if there is nothing in the products dictionary
        print("No products available to add to cart.") #tells the user there is nothing to add

    else: #runs when there are products to add

        item_number = 1 #counter used to number each product on the screen, starting at 1
        for product, price in products.items(): #.items() gives each product name and its price from the products dictionary
            print(f"{item_number}. {product} - ${price:.2f}") #shows the product's number, name, and price
            print(" ")
            item_number = item_number + 1 #moves the counter up by 1 for the next product
        product_num = get_number("Enter the number of the product: ", 1, len(products)) #gets a valid product number, it must be from 1 to the number of products

        product_names = list(products.keys()) #makes a list of just the product names so we can find a product by its number
        product = product_names[product_num - 1] #this gets the product the user picked, minus 1 because list indexes start at 0
        quantity = get_number(f"How many {product} do you want? ", 1, 100) #gets a valid quantity from 1 to 100

        if product in shopping_cart: #checks if the product is already in the cart
            shopping_cart[product] = shopping_cart[product] + quantity #adds the new amount to the amount already in the cart
        else: #runs when the product is not in the cart yet
            shopping_cart[product] = quantity #adds the product to the cart with the amount the user picked
        print(f"{quantity} {product} has been added to cart.") #tells the user what was added


def count_items(): #adds up how many units are in the whole cart
    total_items = 0 #starts the count at 0
    for quantity in shopping_cart.values(): #goes through the quantity of each product in the cart
        total_items = total_items + quantity #adds this product's quantity to the count
    return total_items #sends back the total number of items


def display_cart(): #shows each cart item with its unit price, quantity, and line total
    item_number = 1 #counter used to number each item on the screen, starting at 1
    for product, quantity in shopping_cart.items(): #.items() gives each product name and its quantity from the cart
        price = products[product] #gets the price of one unit from the products dictionary
        line_total = price * quantity #the price of one unit times how many the user wants
        print(f"{item_number}. {product} - ${price:.2f} x {quantity} = ${line_total:.2f}") #shows the number, product, unit price, quantity, and line total
        print(" ")
        item_number = item_number + 1 #moves the counter up by 1 for the next item
    print(f"Total Items: {count_items()}") #prints the total number of items in the cart


def remove_product(): #lets the user remove one unit of a product from the cart
    removed = input("Do you want to remove an item from the cart? (y/n): ") #asks if the user wants to remove something

    if removed == "y": #runs if the user said yes
        removed_item = get_number("Enter the number of the item to remove: ", 1, len(shopping_cart)) #gets a valid item number, it must be from 1 to the number of products in the cart
        cart_products = list(shopping_cart.keys()) #makes a list of just the product names in the cart so we can find one by its number
        removed_product = cart_products[removed_item - 1] #gets the product the user picked, minus 1 because list indexes start at 0
        shopping_cart[removed_product] = shopping_cart[removed_product] - 1 #removes one unit of that product
        if shopping_cart[removed_product] == 0: #checks if there are none of that product left
            shopping_cart.pop(removed_product) #deletes the product from the cart since its quantity is 0
        print(f"One {removed_product} has been removed from the cart.") #tells the user what was removed
    else: #runs if the user did not say yes
        print("No items removed from the cart.") #tells the user nothing changed


def calculate_total(): #adds up the price of everything in the cart
    total = 0 #starts the total at 0
    for product, quantity in shopping_cart.items(): #this is a for loop that will go through each product and its quantity in the shopping cart
        total = total + products[product] * quantity #gets the price from the products dictionary, multiplies it by the quantity, and adds it to the total
    return total #sends back the subtotal


def calculate_discount(total): #figures out the discount based on the subtotal
    discount = 0 #no discount unless the total is over $10
    if total > 10 and total <= 20: #this is an if statement that checks if the total is greater than 10 and less than or equal to 20. If it is, a discount of 5% is applied
        discount = total * 0.05 #5% of the total

    elif total > 20 and total <= 40: #checks if the total is greater than 20 and less than or equal to 40
        discount = total * 0.10 #10% of the total

    elif total > 40: #checks if the total is greater than 40
        discount = total * 0.15 #15% of the total

    return discount #sends back the discount amount


def print_receipt(subtotal, discount): #prints the final receipt after checkout
    today = datetime.date.today() #gets today's date from the datetime module
    print("======= Receipt =======")
    print(f"Date: {today.strftime('%m/%d/%Y')}") #prints the date as month/day/year
    display_cart() #shows every item with its quantity, unit price, line total, and the total number of items
    print(f"Subtotal: ${subtotal:.2f}") #prints the total before the discount
    print(f"Discount: ${discount:.2f}") #prints the discount amount
    print(f"Final Total: ${subtotal - discount:.2f}") #prints the total after the discount
    print("Thank you for shopping with us!") #prints the thank-you message


while checkout == False: #this is a while loop that will keep running until the user chooses to checkout. The condition checks if the checkout variable is False. If it is, the loop will continue to run. If it is True, the loop will stop and the program will end.
    print("======= Welcome to the store! =======")
    print("1. View available products")
    print("2. Add product to cart")
    print("3. View current cart")
    print("4. View current total")
    print("5. Checkout")
    choice = get_number("Enter your choice: ", 1, 5) #gets a valid menu choice from 1 to 5


    if choice == 1: #runs if the user picked option 1
        display_products() #shows the products and prices


    elif choice == 2: #runs if the user picked option 2
        add_product() #lets the user add a product to the cart


    elif choice == 3: #runs if the user picked option 3
        print("======= Current Cart =======")
        if shopping_cart == {}: #this if statement checks if the shopping cart is empty
            print("Your cart is empty.") #tells the user there is nothing in the cart

        else:

            display_cart() #shows what is in the cart
            remove_product() #asks if the user wants to remove an item


    elif choice == 4: #runs if the user picked option 4
        print("======= Current Total =======")
        if shopping_cart == {}: #this if statement checks if the shopping cart is empty
            print("Your cart is empty.") #tells the user there is nothing in the cart

        else:

            display_cart() #shows what is in the cart and the total number of items

            total = calculate_total() #gets the subtotal of the cart
            print(f"Subtotal: ${total:.2f}") #prints the subtotal with two decimal places


    elif choice == 5: #runs if the user picked option 5
        print("======= Checkout =======")
        if shopping_cart == {}: #this if statement checks if the shopping cart is empty
            print("Your cart is empty. Add a product before checking out.") #stops the user from checking out with an empty cart

        else:

            total = calculate_total() #gets the subtotal of the cart
            discount = calculate_discount(total) #gets the discount based on the subtotal
            print(f"Total Items: {count_items()}") #prints the total number of items in the cart
            print(f"Subtotal: ${total:.2f}") #prints the subtotal
            print(f"Discount: ${discount:.2f}") #prints the discount amount
            print(f"Total after discount: ${total - discount:.2f}") #prints the total after the discount


            maybe_checkout = input("Do you want to proceed to checkout? (y/n): ") #asks the user to confirm checkout
            if maybe_checkout == "y": #this if statement checks if the user wants to checkout and if they do then it stops the program
                checkout = True #makes the main loop stop
                print_receipt(total, discount) #prints the final receipt