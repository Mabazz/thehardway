name = "Zed A. Shaw"
age = 35
height = 74
weight = 180
eyes = "Blue"
teeth = "White"
hair = "Brown"

print(f"Let's talk about {name}.")
print(f"He's {height} inches tall.")
print(f"he's {weight} pounds heavy.")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"He's teeth are usually {teeth} depending on the coffee.")
total = age + height + weight
print(f"If I add {age}, {height} and {weight} I get {total}")

inches = 1
cm = 2.54
cm_height = height * cm
print(cm_height)

pound = 1
kg = 0.453592
kg_weight = weight * kg
print(kg_weight)

# Para redondear floatings se utiliza round()
round(1.7)
