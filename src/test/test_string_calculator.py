from string_calculator import StringCalculator


class TestStringCalculator:
    def test_it_returns_0_when_passed_the_empty_string(self):
        numbers = ''

        actual_result = StringCalculator().add(numbers)

        assert actual_result == 0

    def test_it_returns_the_number_when_it_receives_one_string_number(self):
        numbers = '4'
        
        actual_result = StringCalculator().add(numbers)

        assert actual_result == 4

    def test_it_sums_two_numbers(self):
        numbers = '1,2'
        
        actual_result = StringCalculator().add(numbers)

        assert actual_result == 3

    def test_it_handles_an_unknown_amount_of_numbers(self):
        numbers = '1,2,3,4,5,6,7,8,9'
        
        actual_result = StringCalculator().add(numbers)

        assert actual_result == 45