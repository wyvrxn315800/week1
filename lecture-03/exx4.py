hours_w = int(input("enter the number of hours:"))
pay_rate = int(input("Enter pay rate:"))
pay=(hours_w-40)*pay_rate*1.5+(40*pay_rate)
print(f"The gross pay is ${pay:.2f}")