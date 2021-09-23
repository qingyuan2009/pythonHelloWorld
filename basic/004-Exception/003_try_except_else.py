def calculate_bmi(height, weight):
    """ calculate body mass index (BMI) """
    return weight / height**2

def evaluate_bmi(bmi):
    """ evaluate the bmi """
    if 18.5 <= bmi <= 24.9:
        return 'healthy'

    if bmi >= 25:
        return 'overweight'

    return 'underweight'

def main():
    try:
        height = float(input('Enter your height (meters):'))
        weight = float(input('Enter your weight (kilograms):'))

    except ValueError as error:
        print(error)
    else:
        bmi = round(calculate_bmi(height, weight), 1)
        evaluation = evaluate_bmi(bmi)

        print(f'Your body mass index is {bmi}')
        print(f'This is considered {evaluation}!')

main()