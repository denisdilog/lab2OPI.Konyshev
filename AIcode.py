# Напиши функцію на Python, яка приймає список чисел і повертає лише парні числа, відсортовані за зростанням.
def get_sorted_even_numbers(numbers):
    even_numbers = [num for num in numbers if num % 2 == 0]
    return sorted(even_numbers)

# Тестування функції
if __name__ == "__main__":
    test_list = [10, 3, 2, 8, 7, 4, 1, 6]
    result = get_sorted_even_numbers(test_list)
    print(f"Початковий список: {test_list}")
    print(f"Відфільтровані парні числа: {result}")