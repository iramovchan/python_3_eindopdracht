dictionary = {"banaan": "geel", "aardbei": "rood", "kiwi": "groen"}


def add_new(key, value):
    dictionary[key] = value


def delete(key):
    del dictionary[key]


def show_all():
    for key, value in dictionary.items():
        print(key, value)


def find():
    key = input("What do you want to find? ")
    if key in dictionary:
        print(dictionary[key])
    else:
        print("Not found")


one = {1: 45, 9: 200}
two = {"one": "fourty five", "three": "nine"}
three = {"(": ")", "<": ">"}


def mix_3(dict_1, dict_2, dict_3):
    dict_4 = {}

    for key, value in dict_1.items():
        dict_4[key] = value
    for key, value in dict_2.items():
        dict_4[key] = value
    for key, value in dict_3.items():
        dict_4[key] = value
    print(dict_4)


def generate_dict():
    generated_dict = {}
    for key in range(5):
        generated_dict[key+1] = (key+1)**2

    print(generated_dict)


generate_dict()

mix_3(one, two, three)

show_all()

find()
