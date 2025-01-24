# Range-Elevation Data as a dictionary
range_elevation_data = {
    0: 0,
    50: 0.35,
    100: 0.70,
    150: 1.05,
    200: 1.20,
    250: 1.75,
    300: 2.05,
    350: 2.45,
    400: 2.80,
    450: 3.15,
    500: 3.50,
    550: 3.80,
    600: 4.10,
    650: 4.45,
    700: 4.85,
    750: 5.45,
    800: 5.60,
    850: 5.90,
    900: 6.45,
    950: 6.90,
    1000: 7.30,
    1050: 7.60,
    1100: 8.00,
    1150: 8.50,
    1200: 8.90,
    1250: 9.55,
    1300: 9.70,
    1350: 10.25,
    1400: 10.75,
    1450: 11.40,
    1500: 12.00,
    1550: 12.55,
    1600: 13.10,
    1650: 13.80,
    1700: 14.50,
    1750: 15.10,
    1800: 15.90,
    1850: 16.20,
    1900: 16.50,
    1950: 17.00,
    2000: 17.60,
    2050: 18.35,
    2100: 19.10,
    2150: 19.70,
    2200: 20.30,
    2250: 21.35,
    2300: 21.60,
    2350: 22.10,
    2400: 23.05,
    2450: 24.00,
    2500: 25.75,
    2550: 26.80,
    2600: 27.90,
    2650: 29.05,
    2700: 30.20,
    2750: 32.60,
    2800: 34.30,
    2850: 39.10,
    2900: 45.00,
    2950: 46.10,
    3000: 47.60,
    3050: 50.35,
    3100: 52.10,
    3150: 54.45,
    3200: 57.50,
    3250: 60.25,
    3300: 62.90,
    3350: 65.65,
    3400: 68.40,
    3450: 70.65
}

# Maximum allowed range
MAX_RANGE = 3450

def get_elevation(range_value):
    # Find the two closest range values in the dictionary
    ranges = list(range_elevation_data.keys())
    
    # Handle the case where the range value is below the smallest or above the largest in the table
    if range_value <= min(ranges):
        return range_elevation_data[min(ranges)]
    elif range_value >= max(ranges):
        return range_elevation_data[max(ranges)]
    
    # Find the closest range values for interpolation
    lower = max([r for r in ranges if r <= range_value])
    upper = min([r for r in ranges if r > range_value])
    
    # Linear interpolation to find the corresponding elevation
    lower_elevation = range_elevation_data[lower]
    upper_elevation = range_elevation_data[upper]
    
    # Interpolation formula
    elevation = lower_elevation + (upper_elevation - lower_elevation) * (range_value - lower) / (upper - lower)
    
    return elevation

def main():
    print("Made by: @DorkwingYT\n")
    
    while True:
        try:
            range_value = float(input("Enter the range you are from your target (in meters): "))
            
            if range_value > MAX_RANGE:
                print(f"\nThe maximum allowed range is {MAX_RANGE} meters. Please enter a valid range.\n")
                print(f"xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n")
                continue
            
            elevation = get_elevation(range_value)
            print(f"\nTo hit something {range_value} meters away set your elevation to ({elevation:.2f}) degrees.\n")
            print(f"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
        except ValueError:
            print("\nInvalid input. Please enter a valid range value.\n")
            print(f"xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n")

main()