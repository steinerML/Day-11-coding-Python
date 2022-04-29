#BMI calculator
#Units in Kilograms and meters

name1 = "Sam"
mass1 = 90
height1 = 1.9

name2 = "Peter"
mass2 = 88
height2 = 1.65

name3 = "Sally"
mass3 = 92
height3 = 1.93

name1

def bmi_calculator (name,mass,height):
    bmi = mass / height ** 2
    if bmi > 25:
        return name + " is overweight"  #Returns to result1,2,3 set.
    else:
        return name + " is not overweight" #Returns to result1,2,3 set.

result1 = bmi_calculator(name1,mass1,height1)
result2 = bmi_calculator(name2,mass2,height2)
result3 = bmi_calculator(name3,mass3,height3)

print(result1)
print(result2)
print(result3)