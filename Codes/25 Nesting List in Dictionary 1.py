# Store information about a pizza being ordered.
pizza = {
    "crust": "thick",
    "toppings": ["mushrooms", "cheese", "paneer"],
    }

# Summarize the order.
print(f"You orderd a {pizza['crust']}-crust pizza"
      " with the following topings:")
for top in pizza["toppings"]:
    print("\t" + top)
