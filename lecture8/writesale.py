num_days = int(input("For hoe many days do you have sale"))
with open('sales.txt','w') as sales_file:
    for count in range (1,num_days+1):
        sales = float(input(f"Enter the sale foe day count:"))
        sales_file.write(str(sales)+'\n')
    print("Data written to sales.txt")