def pizza(size,*topings):
    print(f"This is positional argumnet {size.title()}")
    for toping in topings:
        print(f"THESE ALL ARE STORED IN (*) {toping.title()}")

order = pizza("large",  "carrot","apple","onion","etc")
