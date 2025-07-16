def is_palindrome(s):
    s=s.lower()
    s=s.replace(" ","")
    s2=s[::-1]
    if(s==s2):
        return True
    return False

print(is_palindrome("Racecar"))       # True
print(is_palindrome("hello"))         # False
