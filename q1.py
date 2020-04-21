start_num = 2000
end_num = 3200
for num in range(2000, 3201):
    if((num%7 == 0) and (num%5 != 0)):
        print(num, end = ", ")