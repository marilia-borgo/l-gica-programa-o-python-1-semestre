x = int(input("digite o valor de x"))

if x <= 1:
    y = 1
elif x <= 2:
    y = 2
elif x <= 3:
    y = x**2
else:
    y = x**3

print(f"valor de f(x) {y}")
