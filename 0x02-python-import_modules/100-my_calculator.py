#!/usr/bin/python3
if __name__ == '__main__':
    import calculator_1, sys

    count = len(sys.argv) - 1
    if count < 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    elif count == 3:
        if sys.argv[2] == "+":
            result = calculator_1.add(sys.argv[1], sys.argv[3])
            print("{} {} {} = {}".format(sys.argv[1], sys.argv[2], sys.argv[3], result))
        elif sys.argv[2] == "-":
            result = calculator_1.sub(sys.argv[1], sys.argv[3])
            print("{} {} {} = {}".format(sys.argv[1], sys.argv[2], sys.argv[3], result))
        elif sys.argv[2] == "*":
            result = calculator_1.mul(sys.argv[1], sys.argv[3])
            print("{} {} {} = {}".format(sys.argv[1], sys.argv[2], sys.argv[3], result))
        elif sys.argv[2] == "/":
            result = calculator_1.div(sys.argv[1], sys.argv[3])
            print("{} {} {} = {}".format(sys.argv[1], sys.argv[2], sys.argv[3], result))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            sys.exit(1)
