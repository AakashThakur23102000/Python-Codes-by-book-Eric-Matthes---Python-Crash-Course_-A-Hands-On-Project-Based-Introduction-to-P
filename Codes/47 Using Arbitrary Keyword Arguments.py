##  **is used to build a arbitary dictionary names detailes here

def users(first,last,**details):
    details["first_name"] = first
    details["last_name"] = last
    return details

profile = users("Aakash","Thakur",
                Age=21,
                Gender="Male")

print(profile)  
    
