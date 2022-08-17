'''

alien = {"color":"green","gender":"male","points":15}
print(alien)

#printing value of color first
print(alien['color'])

#adding new enties to the dictionary
alien["damage"] = 200
print(alien)

alien["deathdamage"] = "Too Hard"
print(alien)


'''

#Advance Example
#alien distance tracking by initial point zero

alien = {"position":0, "speed":"medium"}
if alien["speed"]=="slow":
    increment=1
elif alien["speed"]=="medium":
    increment=5
else:
    increment=10
alien["position"] = alien["position"] + increment 
print(f"New position of alien is {alien['position']}")
