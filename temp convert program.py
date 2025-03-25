def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def fahrenheit_to_kelvin(fahrenheit):
    celsius = fahrenheit_to_celsius(fahrenheit)
    return celsius_to_kelvin(celsius)

def kelvin_to_fahrenheit(kelvin):
    celsius = kelvin_to_celsius(kelvin)
    return celsius_to_fahrenheit(celsius)

def temperature_converter():
    while True:
        print("\nTemperature Converter:")
        print("1. Celsius to Fahrenheit")
        print("2. Fahrenheit to Celsius")
        print("3. Celsius to Kelvin")
        print("4. Kelvin to Celsius")
        print("5. Fahrenheit to Kelvin")
        print("6. Kelvin to Fahrenheit")
        print("7. Exit")

        choice = input("Enter choice (1/2/3/4/5/6/7): ")

        if choice == '7':
            print("Exiting...")
            break

        temp = float(input("Enter temperature: "))

        if choice == '1':
            print(f"{temp} Celsius = {celsius_to_fahrenheit(temp)} Fahrenheit")
        elif choice == '2':
            print(f"{temp} Fahrenheit = {fahrenheit_to_celsius(temp)} Celsius")
        elif choice == '3':
            print(f"{temp} Celsius = {celsius_to_kelvin(temp)} Kelvin")
        elif choice == '4':
            print(f"{temp} Kelvin = {kelvin_to_celsius(temp)} Celsius")
        elif choice == '5':
            print(f"{temp} Fahrenheit = {fahrenheit_to_kelvin(temp)} Kelvin")
        elif choice == '6':
            print(f"{temp} Kelvin = {kelvin_to_fahrenheit(temp)} Fahrenheit")
        else:
            print("Invalid input")

temperature_converter()
