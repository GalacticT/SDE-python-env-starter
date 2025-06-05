#You want the function below to print a greeting message to the screen.
# This code will not be executed until it is 'called'.
def say_hello(name):
    print(f'Hello {name}')


# Our function is defined above, so now we can 'call' it
say_hello('Bob')
# Add a second parameter called ‘City’
# Update the print statement so it says: “Hello            , welcome to                 .”
# Call the function using a name and a city to see if it works!
def say_hello(name, city):
    print(f'Hello {name}, welcome to {city}!')
say_hello('Bob', 'Garland')
