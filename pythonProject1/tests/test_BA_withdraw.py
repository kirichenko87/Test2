import pytest
from bank_account import BankAccount


@pytest.mark.parametrize('amount, amount_draw, expected_result',
                         [
                             (100, 90, 10),
                             (125, 25, 100),
                             (100, 99, 1),
                             (10, 9, 1)
                         ])
def test_withdraw_positive(amount, amount_draw, expected_result):
    ba = BankAccount()
    ba.deposit(amount)
    ba.withdraw(amount_draw)
    assert ba.get_balance() == expected_result


@pytest.mark.parametrize('amount, amount_draw, expected_result',
                         [
                             (500, '123', TypeError),
                             (500, [1, 2, 3, 4], TypeError),
                             (500, 1.3, TypeError),
                             (500, (123, 124), TypeError),
                             (500, 600, ValueError)

                         ]
                         )
def test_withdraw_negative(amount, amount_draw, expected_result):
    ba = BankAccount()
    ba.deposit(amount)
    with(pytest.raises(expected_result)):
        ba.withdraw(amount_draw)


@pytest.mark.parametrize('amount, amount_draw, expected_result',

                         [
                             (100000001, 100000000, 1),
                             (1, 1, 0)

                         ])
def test_withdraw_limit(amount, amount_draw, expected_result):
    ba = BankAccount()
    ba.deposit(amount)
    ba.withdraw(amount_draw)
    assert ba.get_balance() == expected_result
