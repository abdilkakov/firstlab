def isPalindrome(s):
    s=s.lower()
    return s==s[::-1]

s=input()
if isPalindrome(s):
    print("Yeah, it is Palindrome")
else:
    print("Ohh noo, it is not a Palindrome")