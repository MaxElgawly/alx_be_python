FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
     return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
         return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def main():
    try:
        # Prompt for temperature input
        temp_input = input("Enter the temperature to convert: ")
        temperature = float(temp_input)  # Validate numeric value

        # Prompt for unit
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

        if unit == "F":
            celsius = convert_to_celsius(temperature)
            print(f"{temperature}°F is {celsius}°C")
        elif unit == "C":
            fahrenheit = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is {fahrenheit}°F")
        else:
            raise ValueError("Invalid temperature unit. Please enter 'C' or 'F'.")

    except ValueError as ve:
        print("Error:", ve)
        print("Invalid temperature. Please enter a numeric value.")

if __name__ == "__main__":

    main()

