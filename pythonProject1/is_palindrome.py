def is_palindrome(s):
    if not isinstance(s, str): raise TypeError

    return s == s[::-1]


