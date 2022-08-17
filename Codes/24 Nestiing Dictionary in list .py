'''
#here we store 3 alien dictionaries in a list name aliens and after that printed that list by for loop#
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
    print(alien)
'''
#create 30 green aleen dict in a list and then print only 5 aliens
# Make an empty list for storing aliens.
ali = []
# Make 30 green aliens.
for alien in range(30):
    alie = {"color":"green", "gender":"male", "age":20}
    ali.append(alie)
'''
# Show the first 5 aliens.
for alien in ali[:5]:
    print(alien)
# Show how many aliens have been created.
print(f"Total numbers of alien created are - {len(ali)}")
'''



#to chnage the value of first three values of alien.
for alien in ali[:3]:
      alien["color"]="yello"
      alien["gender"]="female"
      alien["age"]= 10
for alien in ali[:5]:
    print(alien)
