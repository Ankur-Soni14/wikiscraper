from collections import OrderedDict
import operator


def dictionary():
    key_value = {}

    key_value[2] = 56
    key_value[1] = 2
    key_value[5] = 12
    key_value[4] = 24
    key_value[6] = 18
    key_value[3] = 323

    print("Task 1:-\n")

    print("key_value", key_value)

    for i in sorted(key_value.keys()):
        print(i, end=" ")


def main():
    dictionary()


if __name__ == "__main__":
    main()


dict = {'ravi': '10', 'rajnish': '9',
        'sanjeev': '15', 'yash': '2', 'suraj': '32'}

dict1 = OrderedDict(sorted(dict.items()))
print(dict1)
