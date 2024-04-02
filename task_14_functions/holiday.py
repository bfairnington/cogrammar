"""
Practical Task 1
Follow these steps:
● Create a Python file called holiday.py.
● Your task will be to calculate a user’s total holiday cost, which includes the
plane cost, hotel cost, and car-rental cost.
● First, get the following user inputs:
○ city_flight: The city they will be flying to. (You can create some
options for them. Remember each city will have different flight
costs.)
○ num_nights: The number of nights they will be staying at a hotel
○ rental_days: The number of days for which they will be hiring a
car.
● Next, create the following four functions:
● hotel_cost: This function will take num_nights as an argument,
and return a total cost for the hotel stay (you can choose the price
per night charged at the hotel).
● plane_cost: This function will take city_flight as an argument
and return a cost for the flight. (Hint: use if/else if statements in
the function to retrieve a price based on the chosen city.)
● car_rental: This function will take rental_days as an argument
and return the total cost of the car rental (you can choose the daily
rental cost.)
● holiday_cost: This function will take the three arguments
hotel_cost, plane_cost, car_rental. Using these three
arguments, you can call all three of the above functions with
respective arguments and finally return a total cost for your
holiday.
● Print out all the details about the holiday in a readable way.
● Try running your program with different combinations of input to show
its compatibility with different options.
"""

# Create user inputs
city_flights = {
    "Amsterdam" : 60,
    "Athens" : 95,
    "Barcelona" : 80,
    "Berlin" : 50,
    "Budapest" : 55,
    "Brussels" : 40,
    "Copenhagen" : 45,
    "Dublin" : 30,
    "Dubrovnik" : 75,
    "Helsinki" : 85,
    "Lisbon" : 70,
    "Madrid" : 75,
    "Milan" : 90,
    "Munich" : 60,
    "Oslo" : 70,
    "Paris" : 55,
    "Porto" : 75,
    "Prague": 80,
    "Rome" : 90,
    "Stockholm" : 65
}
num_nights = 5
rental_days = 2

# Define functions
def hotel_cost(num_nights):
    cost = num_nights * 100 
    return cost # £100 per night

def plane_cost(city_flight):
    cost = city_flights[f"{city_flight}"]
    return cost  # Cost of flight, depending on city

def car_rental(rental_days):
    cost = rental_days * 30
    return cost # £30 per day

def holiday_cost(hotel_cost, plane_cost, car_rental):
    cost = hotel_cost + plane_cost + car_rental
    return cost # Sum of all costs


# Output printed in a readable way
print("\nSelect a flight from the following list:")

# Enumerate dictionary to show all flights and prices
for num, (key, value) in enumerate(city_flights.items()):
    print(f"{num + 1})", key, f"\t £{value}")

# Define cost inputs
city_flight = input("\nType the name of the city to which you want to fly: ")
num_nights = int(input("\nType the number of nights you want to stay: "))
rental_days = int(input("\nType the number of days you want to rent a car: "))

# Display cost breakdown and total cost
print("\nThe total cost of your holiday is:")
print(f"Flight cost: \t \t£{plane_cost(city_flight)}")
print(f"Hostel cost: \t \t£{hotel_cost(num_nights)}")
print(f"Car rental cost: \t£{car_rental(rental_days)}")
print(f"Total cost: \t \t£{holiday_cost(hotel_cost(num_nights), plane_cost(city_flight), car_rental(rental_days))}")

