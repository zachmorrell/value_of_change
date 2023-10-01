# change.py
#   A program to calculate the value of some change in dollars.


def main():
    print("This program takes the number of USD change and returns the total value.")
    print()
    print("Please enter the count of each coin type.")

    # Takes the count of change as a float and multiplies it by it's currency value and adds all the values together.
    total = float(input("Quarters: ")) * 0.25 + float(input("Dimes: ")) * .1 + float(input("Nickles: ")) *.05 + float(input("Pennies: ")) * .01
    print()
    print(total)

main()