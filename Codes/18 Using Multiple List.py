'''The following example defines two lists. Where customer list is compared with shop list'''

shops_list = ["apple","banana","cake","chips","jelly","curry"]

customers_list = ["dog","cat","banana","rat","jelly"]
for customer_list in customers_list:
    if customer_list in shops_list:
        print(f"Added {customer_list}")
    else:
        print("Not avilable right now")
