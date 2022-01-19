def hello_world():
    print("hello world " * 10)

    
hello_world()


def max_van_3(num_1, num_2, num_3):
    if num_1 > num_2 and num_1 > num_3:
        max_getal = num_1
    elif num_2 > num_1 and num_2 > num_3:
        max_getal = num_2
    elif num_3 > num_1 and num_3 > num_2:
        max_getal = num_3
    return max_getal


num_1 = input("Write first number:")
num_2 = input("Write second number:")
num_3 = input("Write third number:")

print("The biggest number of all is: ", max_van_3(num_1, num_2, num_3))

