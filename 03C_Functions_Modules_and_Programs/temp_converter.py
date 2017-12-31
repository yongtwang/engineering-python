# temp_converter.py
# This program converts temperature from Celsius to Fahrenheit
# or from Fahrenheit to Celsius, depending on user's choice

# Celsius to Fahrenheit
def c2f(c):
    f = (9/5) * c + 32
    return f

# Fahrenheit to Celsius
def f2c(f):
    c = (5/9) * (f - 32)
    return c
    
def main():
    print("If you want to convert from °C to °F, press 1.")
    print("If you want to convert from °F to °C, press 2.")
    choice = input("Enter your choice: ")
    if choice == '1':
        c = float(input("Enter the temperature in °C: "))
        f = c2f(c)
        print("The temperature is", f, "°F.")
    elif choice == '2':
        f = float(input("Enter the temperature in °F: "))
        c = f2c(f)
        print("The temperature is", c, "°C.")
    else:
        print("This is not a valid choice.")

main()