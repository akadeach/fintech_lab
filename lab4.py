#1
for i in range(1,21):
    print (i)

#2
a = int(input("value : "))
x = 0

for i in range(10):
    x = x + a    
print(x)


#3
b = int(input("Please specify height: "))
x = ""

for i in range(b):  
    x = x + "*"
    print(x)

#4
for i in range(101):
    if i%2 == 0:
        print(i)

#5
grade = ['A','B','C','D','F']

print(f'You got {grade[0]}. Excellent Job')
print(f'You got {grade[1]}. Good Job')
print(f'You get {grade[2]}. Not bad')
print(f'You get {grade[3]}. Maybe try harder?')
print(f'You get {grade[4]}. That’s okay try again. It is not the end of the world. Everyone can improve as long as you keep trying.') 

