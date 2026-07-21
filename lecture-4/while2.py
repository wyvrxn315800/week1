keep_going ="y"
while keep_going =="y":
    salas = float(input("Enter The amount of sales: "))
    comm_rate =float(input("Enter the commisson rate: "))
    commission=salas*comm_rate
    print(f"The commissionn is ${commission:.2f}")
    keep_going = input("Do you want to calculate another" "comission(Enter y for yer ):")