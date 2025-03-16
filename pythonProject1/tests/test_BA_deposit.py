import pytest
from bank_account import BankAccount


@pytest.mark.parametrize('amount, expected_result',
                         [
                             (4, 4),
                             (200, 200),
                             (2000, 2000)
                         ])
def test_deposit_positive(amount, expected_result):
    ba = BankAccount()
    ba.deposit(amount)
    assert ba.get_balance() == expected_result


@pytest.mark.parametrize('amount, expected_result',

                         [
                             ('123', TypeError),
                             ([1, 2, 3, 4], TypeError),
                             (1.3, TypeError),
                             ((123, 124), TypeError),
                             (-1, ValueError),
                             (0, ValueError)
                         ])
def test_deposit_negative(amount, expected_result):
    with(pytest.raises(expected_result)):
        ba = BankAccount()
        ba.deposit(amount)


@pytest.mark.parametrize('amount, expected_result',

                         [
                             (100000000, 100000000),
                             (1, 1)
                         ])
def test_deposit_limit(amount, expected_result):
    ba = BankAccount()
    ba.deposit(amount)
    assert ba.get_balance() == expected_result
