def check_type(value):
    if not isinstance(value, (float, int)):
        return False
    return True


def average(lst):
    if not isinstance(lst, list):
        raise TypeError("Что то не так с типом данных")

    if not lst:
        raise ValueError

    for elem in lst:
        if not check_type(elem):
            raise TypeError("Проблема с элементом в списке , не тот тип данных")

    return sum(lst) / len(lst)
