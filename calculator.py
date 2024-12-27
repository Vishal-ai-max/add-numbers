def add(numbers: str):
    if not numbers:
        return 0
    return sum(map(int, numbers.replace("\n", ",").split(',')))