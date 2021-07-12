weight = input("input your weight: ")
unit = input("(L)bs or (K)g: ")

if unit.upper() == "L":
    conv = int(weight)*0.45
    print(f"your weight is {conv} killos")

else:
    conv2 = int(weight)//0.45
    print(f"your weight is {conv2} pounds")