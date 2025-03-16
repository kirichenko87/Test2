import pytest
from bank_account import BankAccount


@pytest.mark.parametrize('amount, expected_result',
                         [
                             (100, 100),
                             (150, 150)
                         ]
                         )
def test_get_balance_positive(amount, expected_result):
    ba = BankAccount()
    ba.deposit(amount)
    assert ba.get_balance() == expected_result
