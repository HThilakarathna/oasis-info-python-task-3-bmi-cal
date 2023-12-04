def calculate_bmi(weight, height):
    try:
        bmi = weight / (height ** 2)
        return bmi
    except ZeroDivisionError:
        return "Error: Height cannot be zero."

def classify_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"

def main():
    try:
        weight = float(input("Enter your weight in kilograms: "))
        height = float(input("Enter your height in meters: "))
    except ValueError:
        print("Error: Please enter valid numeric values for weight and height.")
        return

    bmi = calculate_bmi(weight, height)

    if isinstance(bmi, str):
        print(bmi)
    else:
        category = classify_bmi(bmi)
        print(f"Your BMI is: {bmi:.2f}")
        print(f"Category: {category}")

if __name__ == "__main__":
    main()
