keep_going ="y"
while keep_going =="y":
    numitem = float(input("Enter The item sales: "))
    comm_rate =float(input("Enter the commisson rate: "))
    item_price=numitem*2.5
    print(f"price is ${item_price:.2f}")
    keep_going = input("Do you want to calculate another" "Do you have another item (Enter y for yes ):")