#SimpleBmiCalculator
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
#Warning you should round the result to the nearest whole number. The interpretation message needs to include the words in bold from the interpretations above. e.g. underweight, normal weight, overweight, obese, clinically obese.
bmi = weight / (height**2)
#print(round(bmi)) first check round works :) 
roundBmi = round(bmi)
if(roundBmi < 19):
    print(f"Your BMI is {roundBmi}, you are underweight.")
elif(roundBmi < 25):
    print(f"Your BMI is {roundBmi}, you have a normal weight.")
elif(roundBmi < 30):
    print(f"Your BMI is {roundBmi}, you are slightly overweight.")
elif(roundBmi < 35):
    print(f"Your BMI is {roundBmi}, you are obese.")
else:
    print(f"Your BMI is {roundBmi}, you are clinically obese.")
