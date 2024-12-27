def add(numbers: str):
    if not numbers:
        return 0
    if numbers.startswith("//"):
        delimiter = numbers[2]     # assuming delimiter will be of length one
        numbers = numbers[4:]      # slicing numbers to remove delimiter initialization.
    else:
        delimiter = ','
    return sum(map(int, numbers.replace("\n", ",").split(delimiter)))