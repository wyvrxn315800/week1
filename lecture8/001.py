num_emps = int(input("how amny employee create?"))
with open('employee.txt',"w") as emp_file:
    for count in range(1,num_emps+1):
        print("enter data for employee",count,sep="")
        name =input("name: ")
        id_num = input("ID number :")
        dept = input ("department:")
        emp_file.write( name +'\n')
        emp_file.write(id_num +'\n')
        emp_file.write(dept + '\n')
        print()
print("employee recorde written to employee.txt")