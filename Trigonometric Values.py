import math

print("\033c")

x = float(input("Enter a number : "))

sin = math.sin(x)
cos = math.cos(x)
tan = math.tan(x)

print(f"The sine of {x} is {sin}")
print(f"The cosine of {x} is {cos}")
print(f"The tangent of {x} is {tan}")