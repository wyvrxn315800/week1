import struct
with open ("recods.bin","rb") as file:
    recods_size = struct.calcsize('i20sif')
    while True:
        data = file.read(recods_size)
        if not data:
            break
        recods = struct.unpack('i20sif',data)
        recods = (recods[0],recods[1].decode().strip('\x00'),recods[2],recods[3])
        print("ID: {recods[0]},name{recods[1]},age:{recods[2]},gpa{recods[3]}")