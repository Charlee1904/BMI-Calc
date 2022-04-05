# Body mass index (BMI) is a value derived from the mass (weight) and height of a person. The BMI is defined as the body mass divided by the square of the body height, and is expressed in units of kg/m2

height = input("Enter your height in m:")
weight = input("Enter your weight in kg:")


bmi = int(weight) / float(height) ** 2
bmi_int = int(bmi)
print(bmi_int)