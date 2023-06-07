# Ask the user their username
username = input("What is your username? ")
# Ask the user their favourite integer
fav_numb = int(input("Favourite Number? "))
# Double, halve and square the number
double = fav_numb * 2
halve = fav_numb / 2
square = fav_numb * fav_numb
# Greet the user
print("Hi {}, your favourite number is {}".format(username, fav_numb))
print()
# Output the results of doubling,halving

# and squaring their favourite number
print("double {} is {}".format(fav_numb, double))
print("half {} is {}".format(fav_numb, halve))
print("square {} is {}".format(fav_numb, square))