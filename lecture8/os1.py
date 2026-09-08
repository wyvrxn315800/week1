import struct
num_records = int(input("How many recods do you want to create?"))
with open("recods.bin","wb") as file:
    for _ in range(num_records):
        id_num = int(input("Enter ID"))
        name = int(input("Enter anme"))
        age = int(input("Enter age"))
        gpa = int(input("Enter gpa"))
        data = struct.pack('i20sif',id_num,name.encode(),age,gpa)
        file.write(data)
    print(f"(num_recods) recods have been written to recods.bin")