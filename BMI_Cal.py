def BMI_Start():

    global weight_kg
    global height_m
    global gender

    gender = input("What is your gender? (M/F): ")
    weight_kg = float(input("What is your weight? (in Kilograms): "))
    height_m = float(input("What it your height? (in meter)?: "))                

    result = round((weight_kg / height_m ** 2), 4)

    print("BMI:", result)

BMI_Start()