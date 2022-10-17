# Calculator magic.
def calculate():
    operation = input("Adjon meg egy műveleti jelet: ")

    if operation != '+' or operation != '-' or operation != '*' or operation != '/':
        return calculate()

    number_1 = int(input('Első szám: '))
    number_2 = int(input('Második szám: '))


    if operation == '+' and (number_1 != '' or number_1 != "") :
        print('{} + {} = '.format(number_1, number_2), (number_1 + number_2))

    elif operation == '-':
        print('{} - {} = '.format(number_1, number_2), (number_1 - number_2))

    elif operation == '*':
        print('{} * {} = '.format(number_1, number_2), (number_1 * number_2))

    elif operation == '/':
        print('{} / {} = '.format(number_1, number_2), (number_1 / number_2))

    else:
        print("Rossz adatot/adatokat adtál meg!")
        return calculate()


calculate()