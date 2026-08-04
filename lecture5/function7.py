def print_all(*args):
    for index, value in enumerate(args):
        print(f"Argument {index + 1}: {value}")
print_all("Python", 3.8, True, [1, 2, 3], {"key": "value"})