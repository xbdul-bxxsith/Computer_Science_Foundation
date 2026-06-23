orders_list = [] #An empty list to add the orders after an order is created.
count_order_id = 1 #This variable is to count how many orders has been created.
footer = "="*60 #This prints my custom footer after every endings.

#---------------------------------------------------------------------------------------------------------------------------------------------------

food_menu = { #I have added 20 items in a dictionary as the menu.
    1: {"item": "Chicken Kottu", "price": 1200.00},
    2: {"item": "Chicken Cheese Kottu", "price": 1450.00},
    3: {"item": "Egg Fried Rice", "price": 900.00},
    4: {"item": "Chicken Fried Rice", "price": 1100.00},
    5: {"item": "Rice & Curry (Chicken)", "price": 550.00},
    6: {"item": "Naasi Goreng", "price": 1400.00},
    7: {"item": "Devilled Chicken Pizza", "price": 2400.00},
    8: {"item": "Cheese & Tomato Pizza", "price": 1950.00},
    9: {"item": "Beef Burger With Fries", "price": 1400.00},
    10: {"item": "Crispy Chicken Submarine", "price": 1250.00},
    11: {"item": "Pasta (Mexican)", "price": 1650.00},
    12: {"item": "Roasted Chicken", "price": 1200.00},
    13: {"item": "Chicken Biriyani", "price": 1300.00},
    14: {"item": "Garlic Bread (4 Pcs)", "price": 600.00},
    15: {"item": "French Fries (Large)", "price": 800.00},
    16: {"item": "Chocolate Biscuit Pudding", "price": 550.00},
    17: {"item": "Caramel Pudding", "price": 400.00},
    18: {"item": "Eclairs", "price": 300.00},
    19: {"item": "Chocolate Milkshake", "price": 500.00},
    20: {"item": "Vanilla Milkshake", "price": 400.00},
}

#---------------------------------------------------------------------------------------------------------------------------------------------------

def display_food_menu(): #This function is to print/display the above created food menu along with a few custom string formatings.
    print("\n=============== FOOD MENU | ELITE RESTAURANT ===============\n")
    for num, details in food_menu.items():
        print(f"{num:<2}: {details['item']:<42} - Rs. {details['price']:.2f}")
    print(f'\n{footer}')

#---------------------------------------------------------------------------------------------------------------------------------------------------

def add_orders(): #This function is to create a new order (ive added a feauture to automatically generate id numbers for every orders).
    global count_order_id
    print('\n=============== NEW ORDER | ELITE RESTAURANT ===============\n')
    assigned_id = f'ID{count_order_id:03d}'
    print(f'Order ID: {assigned_id}')

    customer_name = str(input("Enter Customer Name: ")).capitalize()

    cart = []
    order_total_amount = 0.0
    display_food_menu()

    while True:
        try:
            menu_choice = int(input("\nEnter Food Number (0 To Finish): "))
            if menu_choice == 0:
                break
            if menu_choice not in food_menu:
                print("Invalid: Item Does Not Exist!")
                print(f'\n{footer}')
                continue
            quantity = int(input(f'Enter Quantity For {food_menu[menu_choice]["item"]}: '))
            if quantity <= 0:
                print("Invalid: Quantity Must Be Atleast 1!")
                print(f'\n{footer}')
                continue
        except ValueError:
            print("Invalid: Please Enter A Valid Number!")
            print(f'\n{footer}')
            continue

        item_name = food_menu[menu_choice]['item']
        item_price = food_menu[menu_choice]['price']
        item_total = item_price * quantity

        item_found = False
        for cart_item in cart:
            if cart_item['item-name'] == item_name:
                cart_item['quantity'] += quantity
                cart_item['item-total'] += item_total
                item_found = True
                print(f'\n• Updated: {item_name} x{cart_item["quantity"]} Rs.{cart_item["item-total"]:.2f}')
                print(f'\n{footer}')
                break
        
        if not item_found:
            cart.append({
                'item-name': item_name,
                'quantity': quantity,
                'item-total': item_total
            })
            print(f'\n• Added: {item_name} x{quantity} Rs.{item_total:.2f}')
            print(f'\n{footer}')

        order_total_amount = sum(item['item-total'] for item in cart)

    if not cart:
        print("No Items Selected. Order Cancelled!")
        print(f'\n{footer}')
        return

    new_order = {
        "ID": assigned_id,
        "Name": customer_name,
        "Items Ordered": cart,
        "Amount": order_total_amount,
        "Status": "Pending"
    }

    orders_list.append(new_order)
    print(f'\n• Order {assigned_id} Saved!\n--→ Total Items: {len(cart)} | Bill Total: Rs. {order_total_amount:.2f}')
    print(f'\n{footer}')
    count_order_id = count_order_id + 1

#---------------------------------------------------------------------------------------------------------------------------------------------------

def view_orders(): #This function is to print/display all the orders that has been created.
    print("\n============== ALL ORDERS | ELITE RESTAURANT ===============\n")
    if not orders_list:
        print("No Orders Recorded Yet.")
        print(f'\n{footer}')
        return
    for order in orders_list:
        print(f"ID: {order['ID']} | Customer: {order['Name']} | Status: [{order['Status']}]\n")
        for sub_item in order['Items Ordered']:
            print(f"• {sub_item['item-name']} x{sub_item['quantity']} Rs. {sub_item['item-total']:.2f}")
        print(f"\nTotal Bill: Rs. {order['Amount']:.2f}")
        print(f'\n{footer}')

#---------------------------------------------------------------------------------------------------------------------------------------------------

def search_orders(): #This function is to search orders by id's and view them (doesnt matter whether the order status is pending or completed).
    print("\n============= SEARCH ORDERS | ELITE RESTAURANT =============\n")
    search_id = input("Enter Order ID (Ex: ID001): ").strip().upper()

    for order in orders_list:
        if order['ID'] == search_id:
            print(f'\nOrder Found!')
            print(f"Order ID: {order['ID']}")
            print(f"Customer Name: {order['Name']}")
            print(f"Status: {order['Status']}")
            print("\nItems Ordered:")
            for sub_item in order['Items Ordered']:
                print(f"- {sub_item['item-name']} x{sub_item['quantity']} (Rs. {sub_item['item-total']:.2f})")
            print(f"\nTotal Bill Amount: Rs. {order['Amount']:.2f}")
            print(f'\n{footer}')
            return
        print("Invalid: Order ID Not Found!")
        print(f'\n{footer}')

#---------------------------------------------------------------------------------------------------------------------------------------------------

def update_order_status(): #This function is to update the statuses of the order that has been created already - all the newly created orders are by default assigned as 'Pending' - so by this function the orders can be assigned as 'Completed' or vise versa.
    print("\n============= ORDERS STATUS | ELITE RESTAURANT =============\n")
    search_id = input("Enter Order ID (Ex: ID001): ").strip().upper()

    for order in orders_list:
        if order['ID'] == search_id:
            try:
                choice = int(input("1. Set To Pending\n2. Set To Completed\nSelect Status (1 or 2): "))
                if choice == 1:
                    order['Status'] = "Pending"
                    print(f"\n{order['ID']} Updated To 'Pending'")
                    print(f'\n{footer}')
                    return
                elif choice == 2:
                    order['Status'] = "Completed"
                    print(f"\n{order['ID']} Updated To 'Completed'")
                    print(f'\n{footer}')
                    return 
                else:
                    print("Invalid: Status Unchanged!")
                    print(f'\n{footer}')
            except ValueError:
                print("Invalid: Please Enter A Valid Number!")
                print(f'\n{footer}')
            return
    print("Order ID Not Found!")

#---------------------------------------------------------------------------------------------------------------------------------------------------

def total_sales(): #This function is to calculate the total revenue that is gained by the restaurant after the orders has been "completed".
    print("\n============== TOTAL SALES | ELITE RESTAURANT ==============\n")
    total = 0.0
    for order in orders_list:
        if order['Status'] == "Completed":
            total = total + order['Amount']
    print(f'Total Sales Revenue From All Orders: Rs.{total:.2f}')
    print(f'\n{footer}')


#---------------------------------------------------------------------------------------------------------------------------------------------------

def completed_orders(): #This function shows how many orders has been completed for the day.
    print("\n=========== COMPLETED ORDERS | ELITE RESTAURANT ============\n")
    completed_count = 0
    for order in orders_list:
        if order['Status'] == "Completed":
            completed_count = completed_count + 1
    print(f'Completed Orders Count: {completed_count} Orders.')
    print(f'\n{footer}')

#---------------------------------------------------------------------------------------------------------------------------------------------------

def main_menu(): #This function is the main function which runs in a loop until the exitting condition is met.
    while True:
        print("\n============================================================")
        print("=      RESTAURANT ORDERING SYSTEM | ELITE RESTAURANT       =")
        print("============================================================\n")
        print("1. Add Orders")
        print("2. View Orders")
        print("3. Search Orders")
        print("4. Update Order Status")
        print("5. Total Sales")
        print("6. Completed Orders")
        print("7. Exit")
        user_choice = input("\nEnter Your Choice (1-7): ").strip()
        print(f'\n{footer}')

        if user_choice == "1":
            add_orders()
        elif user_choice == "2":
            view_orders()
        elif user_choice == "3":
            search_orders()
        elif user_choice == "4":
            update_order_status()
        elif user_choice == "5":
            total_sales()
        elif user_choice == "6":
            completed_orders()
        elif user_choice == "7":
            confirm_exit = input("Are You Sure? (y/n): ").lower()
            if confirm_exit == "y":
                break
            else:
                print("Returning To Main Menu!")

#---------------------------------------------------------------------------------------------------------------------------------------------------

main_menu() #By calling out this function the restaurant ordering system begins!