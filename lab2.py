#1
seq = input("Please type comma number : ")
a = seq.split(",")

print("List : ",a)
print("Tuple : ",tuple(a))

#2
color_list = ["Red","Green","White" ,"Black", "Yellow", "Gray" ]

print("First element : ",color_list[0])
print("Last element : ",color_list[-1])
print("First two element : ",color_list[0:2])
print("Last three elements : ",color_list[-3:])
print("Second element to the fourth element : ",color_list[1:4])

#3
exam_st_date = (11, 12, 2020)
print("The examination will start from : ",exam_st_date[0],'/',exam_st_date[1],'/',exam_st_date[2])

