#here * asterisk in parameter accepts multiple values and adds them in tuples

def toppings(*many):
    for topping in many:
        print(f"- {topping}")

toppings("Aakash")
toppings("RED","BLUE","BLack")
