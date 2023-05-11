#!/usr/bin/python3
if __name__ == '__main__':
    import calculator_1
    from sys import argv, exit

    count = len(argv) - 1
    if count < 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    elif count == 3:
        if argv[2] == "+":
            result = calculator_1.add(int(argv[1]), int(argv[3]))
            print("{} {} {} = {}".format(argv[1], argv[2], argv[3], result))
        elif argv[2] == "-":
            result = calculator_1.sub(int(argv[1]), int(argv[3]))
            print("{} {} {} = {}".format(argv[1], argv[2], argv[3], result))
        elif argv[2] == "*":
            result = calculator_1.mul(int(argv[1]), int(argv[3]))
            print("{} {} {} = {}".format(argv[1], argv[2], argv[3], result))
        elif argv[2] == "/":
            result = calculator_1.div(int(argv[1]), int(argv[3]))
            print("{} {} {} = {}".format(argv[1], argv[2], argv[3], result))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            sys.exit(1)
