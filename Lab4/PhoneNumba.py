letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
numbers = [2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 7, 8, 8 ,8, 9, 9, 9, 9]

number_to_call = "1800CallIan" # -> 18002255426
# Create Dict
my_dict: dict[str, int] = {}
# Add all str as keys and the number attached to the str into dict
for let, num in zip(letters, numbers):
    my_dict[let] = num
# Make all str lower so you don't need to worry about capital
lower = number_to_call.lower()

for letter in lower:
    if letter.islower():
        print(my_dict[letter])
    else:
        print(letter)
