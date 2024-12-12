from string_calculator import StringCalculator


class TestStringCalculator:
    def test_it_returns_0_when_passed_the_empty_string(self):
        numbers = ''

        actual_result = StringCalculator().add(numbers)

        assert actual_result == 0

    def test_when_it_receives_one_string_number_it_returns_the_number(self):
        numbers = '4'
        
        actual_result = StringCalculator().add(numbers)

        assert actual_result == 4