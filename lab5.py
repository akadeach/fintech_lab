#1
def myname(val):
    return val

print("My name is : ",myname("Akadeach Moncharoen"))


#2
def print_circle(r):
    PI = 3.14
    area = PI * (r*r)
    print("Print area of circle is : ",area)

radius = float(input("Input radius for print area of circle : "))
print_circle(radius)

#3
def cal_circle(r):
    PI = 3.14
    area = PI * (r*r)

    return area

radius = float(input("Input radius for cal area of circle : "))

print("Cal area of circle is : ",cal_circle(radius))


#4
radius = float(input("Input radius of circle for increases by 1 : "))
for i in range(1,6):  
    print(f'Area of Circle time {i} : ', cal_circle(radius))
    radius += 1


#5
#num_list = ['1','2','3','4','5']

def sum_list(val):
    x = 0
    num_list = val.split(",")
    for i in range(len(num_list)):
        x = x + int(num_list[i])
    return x

val = input("Input list number : ")
print("Sum of list number : ",sum_list(val))



