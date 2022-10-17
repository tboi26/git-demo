# Calculator magic.
def calculate():
    operation = input("Adjon meg egy műveleti jelet: ")

    if operation == '+' or operation == '-' or operation == '*' or operation == '/':
        break
        
    else:
        return calculate

    number_1 = int(input('Első szám: '))
    number_2 = int(input('Második szám: '))


    if operation == '+' and (number_1 != '' or number_1 != "") and (number_2 !='' or number_2 != ""):
        print('{} + {} = '.format(number_1, number_2), (number_1 + number_2))
    
    else:
        print("Számot adj meg!")
        return number_1


    if operation == '-' and (number_1 != '' or number_1 != "") and (number_2 !='' or number_2 != ""):
        print('{} - {} = '.format(number_1, number_2), (number_1 - number_2))

    else:
        print("Számot adj meg!")
        return number_1


    if operation == '*' and (number_1 != '' or number_1 != "") and (number_2 !='' or number_2 != ""):
        print('{} * {} = '.format(number_1, number_2), (number_1 * number_2))
    
    else:
        print("Számot adj meg!")
        return number_1


    if operation == '/' and (number_1 != '' or number_1 != "") and (number_2 !='' or number_2 != ""):
        print('{} / {} = '.format(number_1, number_2), (number_1 / number_2))

    else:
        print("Számot adj meg!")
        return number_1


calculate()