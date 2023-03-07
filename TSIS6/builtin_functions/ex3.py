s = input()
def isPalindrome(s):
    if (s == s[::-1]):
     return True
    else:
       return False
print(isPalindrome(s))
 