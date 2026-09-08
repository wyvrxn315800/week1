with open ("employee.txt","r") as file:
    lines = file.readlines()
    for line in range(0,len(lines),3):
        print("Name :",lines[line].strip())
        print("ID :",lines[line+1].strip())
        print("Dept :",lines[line+2].strip())
    