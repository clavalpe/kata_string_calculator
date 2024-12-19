class NegativeNumbersNotAllowed(Exception):
    def __init__(self, negative_numbers: str) -> None:
        message = f"error: negatives not allowed:{negative_numbers}"
        super().__init__(message)