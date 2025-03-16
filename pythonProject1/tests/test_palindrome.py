import pytest

from is_palindrome import is_palindrome


@pytest.mark.parametrize("value, expected_result",
                         [
                             ('121', True),
                             ('rfr', True),
                             ('1tt1', True),
                             ('1111', True)

                         ])
def test_palindrome_positive(value, expected_result):
    assert is_palindrome(value) == expected_result


@pytest.mark.parametrize("value, expected_result",
                         [
                             (1001, TypeError),
                             ([1211], TypeError),
                             ({1: "RRRRR"}, TypeError),
                             ((1, 2, 3, 3, 2, 1), TypeError)

                         ]
                         )
def test_palindrome_negative(value, expected_result):
    with pytest.raises(expected_result):
        is_palindrome(value)


@pytest.mark.parametrize("value, expected_result",
                         [
                             ("0", True),
                             ("", True)

                         ]
                         )
def test_palindrome_limit(value, expected_result):
    assert is_palindrome(value) == expected_result
