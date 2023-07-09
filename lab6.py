fruits = {'red':'Apple',
          'yellow':'Banana',
          'orange':'Orange'}

#1
print(fruits["red"],"\n")

#2
fruits["black"] = "grape"
print(fruits,"\n")

#3
fruits["red"] = "cherry"
print(fruits,"\n")

#4
fruits.pop("yellow")
print(fruits,"\n")
