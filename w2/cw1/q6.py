def palindrome(string):
    string = string.lower()
    if string == string[::-1]:
        return True

    else:
        return False

print(palindrome("maDaM"))