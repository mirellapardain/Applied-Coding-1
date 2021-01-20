name1 = "Mirella"
height_m1 = 1.6
weight_kg1 = 50
name2 = "Iisak"
height_m2 = 1.75
weight_kg2 = 74
name3 = "Patrik"
height_m3 = 1.8
weight_kg3 = 195
def bmi_calculator(name, height_m, weight_kg):
    bmi = weight_kg / (height_m** 2)
    if bmi < 25:
        return name + " is not overweight"
    else:
        return name + " is overweight"

result1 = bmi_calculator(name1, height_m1, weight_kg1)
result2 = bmi_calculator(name2, height_m2, weight_kg2)
result3 = bmi_calculator(name3, height_m3, weight_kg3)

print (result1)
print (result2)
print (result3)

