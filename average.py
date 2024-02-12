# average.py
numbers = input("Enter numbers separated by space: ").split()
numbers = [int(num) for num in numbers]
average = sum(numbers) / len(numbers)
print("Average:", average)
