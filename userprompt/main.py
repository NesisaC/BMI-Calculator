print('Welcome to your BMI Calculator')

weight = float(input('Enter your weight: '))


height = float(input('Enter your height: '))

bmi = weight/(height**2)
print('Your bmi is : ' + format(bmi, '.2f'))

if bmi < 18.5:
    print('You are underweight')
elif 18.5 <= bmi < 25:
    print('You are in the healthy weight range')
elif 25 <= bmi < 30:
    print('You are in the overweight range')
else:
    print('You are in the obese weight range')