from calculation.calculateBMI import calculate_bmi


def user_prompt(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print('Please enter a positive number')
            else:
                return value
        except ValueError:
            print('Please enter a valid number')


# def main():
#     print('Welcome to your BMI Calculator')
#
#     weight = user_prompt("Enter your weight in kilograms: ")
#     height = user_prompt("Enter your height in metres: ")
#
#     bmi = calculate_bmi(weight, height)
#     category = category_bmi(bmi)
#
#     print('Your bmi is : ' + format(bmi, '.2f'))
#     print(f"Your are in the {category} range")


def category_bmi(bmi):
    if bmi < 18.5:
        print('You are underweight')
    elif 18.5 <= bmi < 25:
        print('You are in the healthy weight range')
    elif 25 <= bmi < 30:
        print('You are in the overweight range')
    else:
        print('You are in the obese weight range')


# if __name__ == "__main__":
#     main()
print('Welcome to your BMI Calculator')
weight = user_prompt("Enter your weight in kilograms: ")
height = user_prompt("Enter your height in metres: ")
bmi = calculate_bmi(weight, height)
category = category_bmi(bmi)

print('Your bmi is : ' + format(bmi, '.2f'))
print(f"Your are in the {category} range")
