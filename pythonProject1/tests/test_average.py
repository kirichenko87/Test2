from average import average
import pytest


@pytest.mark.parametrize('value, expected_result',
                         [
                             ([1, 2, 3, 4], 2.5),
                             ([-1, -1, -1, - 1], -1),
                             ([0, 0, 0], 0),
                             ([25, 25], 25),
                             ([1.1, 1.2, 3.5], 1.9333333333333333)
                         ]
                         )
def test_average_positive(value, expected_result):
    assert average(value) == expected_result


@pytest.mark.parametrize('value, expected_result',
                         [
                             ('1,2,3,4', TypeError),
                             ({1: "wef", "roror": 34}, TypeError),
                             ((123, 423, 3), TypeError),
                             (234, TypeError),
                             (None, TypeError)
                         ]
                         )
def test_average_negative(value, expected_result):
    with pytest.raises(expected_result):
        average(value)


@pytest.mark.parametrize('value, expected_result',
                         [
                             ([1], 1),
                             ([], ValueError),
                             ([-1], -1),
                             ([0], 0)
                         ]
                         )
def test_average_limit(value, expected_result):
    assert average(value) == expected_result
