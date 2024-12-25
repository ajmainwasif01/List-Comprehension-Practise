user_input = int(input("Enter a number: "))

odd_numbers = [num for num in range(1, user_input) if num % 2 != 0]

additional_odd_numbers = [num for num in range(1, user_input + 1, 2)]

print("Odd numbers under the input value:", odd_numbers)
print("Another list of odd numbers:", additional_odd_numbers)






fruits = ["apple", "banana", "cherry", "date", "berry"]

capitalized_fruits = [fruit.capitalize() for fruit in fruits]

print("Original list of fruits:", fruits)
print("Updated list of fruits with capitalized first letters:", capitalized_fruits)
