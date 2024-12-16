from exceptions import NegativeNumbersNotAllowed


class StringCalculator:
    def add(self, numbers: str) -> int:
        if not numbers:
            return 0
                
        if numbers[0:2] == '//':
            separator = numbers[2] 
            return self._sum_numbers_custom_separator(numbers[4:], separator)
            
        return self._sum_numbers(numbers)

    def _sum_numbers(self, numbers: str) -> int:
        numbers = numbers.replace('\n', ',')
        list_of_numbers = numbers.split(',')
        sum = 0
        for number in list_of_numbers:
            if int(number) < 0:
                raise NegativeNumbersNotAllowed()
            sum +=  int(number)

        return sum
    
    def _sum_numbers_custom_separator(self, numbers: str, separator: str) -> int:
        numbers = numbers.replace(separator, ',')
        return self._sum_numbers(numbers)