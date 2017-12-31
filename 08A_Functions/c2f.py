def input_temp():
    temp = float(input('Enter the temperature in °C: '))
    return temp

def convert_temp(c):
    f = 9/5 * c + 32
    return f
    
def output_temp(f):
    print('The temperature is', f, '°F.')
    
def main():
    c = input_temp()
    f = convert_temp(c)
    output_temp(f)

# Determine whether the program is run directly or imported
if __name__ == '__main__':
    main()