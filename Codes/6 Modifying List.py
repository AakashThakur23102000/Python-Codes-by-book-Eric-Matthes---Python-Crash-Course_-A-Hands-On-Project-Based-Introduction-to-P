##modifying a list


#Override a list valie

bike = ["Yamaha","Pulsar","BMW","Ducati","FZ"]
print(bike)

    #to over ride or change value of yamaha to R1 we do
    
bike[0]="R1"
print(bike)


    #to add/append items in a list
bike.append("ZEN")
print(bike)

    #to insert element in a list.
bike.insert(1, "oldZen")
print(bike)

    #to delete element from a list we use del statement using index number
del bike[1]
print(bike)

    #delete by pop() method
    ##The pop() method removes the last item in a list, but it lets you work
    ##with that item after removing it.
print(bike)
poped_bike = bike.pop()
print(bike)
print(poped_bike)
