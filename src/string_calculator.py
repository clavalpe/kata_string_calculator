class StringCalculator:
    def add(self, numbers: str) -> int:
        if not numbers:
            return 0
        
        if len(numbers) == 1:
            return int(numbers)   
        
        return self._sum_numbers(numbers)

    def _sum_numbers(self, numbers: str) -> int:
        list_of_numbers = numbers.split(',')
        sum = 0
        for number in list_of_numbers:
            sum +=  int(number)

        return sum