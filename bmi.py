

# bmi calculator

def bmicalculator():
    height = float(input('enter your height in m:\n '))
    weight = float(input('enter your weight in kg:\n '))
    bmi =  int(weight) / height ** 2
    print(f'your bmi is {bmi} ')
    if bmi < 18.5:
        print(f'your bmi is {bmi}, therefore you are underweight')
    elif bmi > 18.5 and bmi < 25:
        print('you have a normal weight')
    elif bmi > 25 and bmi < 30:
        print('You are overweight')
    elif bmi > 30 and bmi < 35:
        print(' You are obese')
    else:
        print(' you are Clinically obese')

bmicalculator()