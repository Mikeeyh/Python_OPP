def get_prime(list_of_numbers: list):
    prime_numbers = []
    start_index = 0

    while start_index < len(list_of_numbers):
        yield start_index
        if list_of_numbers[start_index] // 2:
            prime_numbers.append(list_of_numbers[start_index])
            start_index += 1
