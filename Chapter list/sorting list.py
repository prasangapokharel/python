
# Take input from the user to create the list of cars
get = input("Enter a list of cars separated by spaces: ")
cars = get.split()

# Sort the list of cars alphabetically
cars.sort()

# Print the sorted list of cars
print("Sorted list of cars:", cars)
