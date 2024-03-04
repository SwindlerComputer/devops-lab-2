# average.py

numbers = input("Enter numbers separated by space: ").split()
numbers = [int(num) for num in numbers]

average = sum(numbers) / len(numbers)
print("Average:", average)

# Calculate and display the largest and smallest numbers
if numbers:
    largest = max(numbers)
    smallest = min(numbers)
    print("Largest number:", largest)
    print("Smallest number:", smallest)
else:
    print("No numbers entered.")
