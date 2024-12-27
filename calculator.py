def add(numbers: str):
    if not numbers:
        return 0
    if numbers.startswith("//"):
        delimiter = numbers[2]     # assuming delimiter will be of length one
        numbers = numbers[4:]      # slicing numbers to remove delimiter initialization.
    else:
        delimiter = ','
    negative_numbers = []
    int_numbers = []
    for num in numbers.replace("\n", ",").split(delimiter):
        int_numbers.append(int(num))
    for num in int_numbers:
        if num < 0:
            negative_numbers.append(num)
    if negative_numbers:
        raise ValueError(f"negative numbers not allowed: {', '.join(map(str, negative_numbers))}")
    return sum(int_numbers)