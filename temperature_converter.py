def convert_temperature(temp, unit):
    unit = unit.upper()
    if unit == 'C':
        return round((temp * 9/5) + 32, 2)
    elif unit == 'F':
        return round((temp - 32) * 5/9, 2)
    else:
        raise ValueError("Invalid unit. Use 'C' for Celsius or 'F' for Fahrenheit.")



try:
    temperature = float(input("Enter the temperature value: "))
    unit = input("Enter the unit of the input temperature (C for Celsius, F for Fahrenheit): ")

    converted = convert_temperature(temperature, unit)
    if unit.upper() == 'C':
        print(f"{temperature}°C is {converted}°F")
    elif unit.upper() == 'F':
        print(f"{temperature}°F is {converted}°C")
except ValueError as e:
    print("Error:", e)

