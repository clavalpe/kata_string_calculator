from exceptions import NegativeNumbersNotAllowed


class StringCalculator:
    def add(self, numbers: str) -> int:
        if not numbers:
            return 0

        if self._has_custom_separator(numbers):
            separator = numbers[2]
            return self._sum_numbers_custom_separator(numbers[4:], separator)

        return self._sum_numbers(numbers)

    def _has_custom_separator(self, numbers) -> bool:
        return numbers[0:2] == "//"

    def _sum_numbers(self, numbers: str) -> int:
        list_of_numbers = self._clean_and_split_numbers(numbers)
        
        sum = 0
        negative_numbers = ""

        for number in list_of_numbers:
            if int(number) < 0:
                negative_numbers += " " + number
                continue

            if int(number) > 1000:
                continue

            sum += int(number)

        if negative_numbers:
            raise NegativeNumbersNotAllowed(negative_numbers)

        return sum

    def _clean_and_split_numbers(self, numbers):
        numbers = numbers.replace("\n", ",")
        list_of_numbers = numbers.split(",")
        return list_of_numbers

    def _sum_numbers_custom_separator(self, numbers: str, separator: str) -> int:
        numbers = numbers.replace(separator, ",")
        return self._sum_numbers(numbers)