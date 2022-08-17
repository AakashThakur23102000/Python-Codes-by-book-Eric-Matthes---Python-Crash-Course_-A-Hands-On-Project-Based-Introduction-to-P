def describe_pet(animal_type, animal_name):
    """Display information about a pet."""
    print(f"My {animal_type}'s name is {animal_name.title()}.")

describe_pet(animal_type="DOG",animal_name="X")
describe_pet(animal_name="Y",animal_type="DOG")


