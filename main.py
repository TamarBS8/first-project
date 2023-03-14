# First_Screen
import coin
import ils
import usd
from ils import ILS
from usd import USD

print('Welcome to currency converter')

def get_user_input(prompt, valid_input):
    user_input = None
    while user_input not in valid_input:
        user_input = input(prompt)
        if user_input not in valid_input:
            print('Invalid Choice, please try again')
    return user_input

def get_float_user_input(prompt):
    user_input = None
    valid_input = False
    while not valid_input:
        try:
            user_input = float(input(prompt))
            valid_input = True
        except ValueError:
            print('Invalid Choice, please try again')

    return user_input


user_input = None
results = []
while user_input != 'N' and user_input != 'n':
    print('Please choose an option (1/2)')
    print('1. Dollars to Shekels \n2. Shekels to Dollars')

    user_input = get_user_input('Your Choice: ', ['1', '2'])
    coin = None
    if user_input == '1':
        coin = USD()
    elif user_input == '2':
        coin = ILS()
    value_to_convert = get_float_user_input('please enter an amount to convert: ')
    result = coin.calculate(value_to_convert)
    print('Result: ' + str(result))
    results.append(result)
    user_input = get_user_input('Do you want to convert again? (Y / N)', ['Y', 'y', 'N', 'n'])

print('Thanks for using our currency converter')
print('Conversions: ')
for result in results:
    print(str(result))


with open('C:\\Users\\tamar\\OneDrive\\שולחן העבודה\\results.txt', 'w') as file:
    for result in results:
        file.write(str(result))
        file.write('\n')



if __name__ == '__main__':
    pass