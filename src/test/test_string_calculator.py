from string_calculator import StringCalculator
import pytest
from exceptions import NegativeNumbersNotAllowed


class TestStringCalculator:
    def test_it_returns_0_when_passed_the_empty_string(self):
        numbers = ""

        actual_result = StringCalculator().add(numbers)

        assert actual_result == 0

    def test_it_returns_the_number_when_it_receives_one_string_number(self):
        numbers = "4"

        actual_result = StringCalculator().add(numbers)

        assert actual_result == 4

    def test_it_sums_two_numbers(self):
        numbers = "1,2"

        actual_result = StringCalculator().add(numbers)

        assert actual_result == 3

    def test_it_handles_an_unknown_amount_of_numbers(self):
        numbers = "1,2,3,4,5,6,7,8,9"

        actual_result = StringCalculator().add(numbers)

        assert actual_result == 45

    def test_it_recognises_newlines_and_commas_as_separators(self):
        numbers = "1\n2,3"

        actual_result = StringCalculator().add(numbers)

        assert actual_result == 6

    def test_it_supports_custom_separators(self):
        numbers = "//;\n1;2"

        actual_result = StringCalculator().add(numbers)

        assert actual_result == 3

    def test_it_disallow_one_negative_number(self):
        numbers = "1,-2"

        with pytest.raises(
            NegativeNumbersNotAllowed, match="error: negatives not allowed: -2"
        ):
            StringCalculator().add(numbers)

    def test_it_disallow_several_negative_numbers(self):
        numbers = "1,-2,-3"

        with pytest.raises(
            NegativeNumbersNotAllowed, match="error: negatives not allowed: -2 -3"
        ):
            StringCalculator().add(numbers)

    def test_it_ignores_bigger_numbers_than_1000(self):
        numbers = "1001, 2"

        actual_result = StringCalculator().add(numbers)

        assert actual_result == 2