def is_palindrome(word):
    return word == word[::-1]

word = input("Enter a word: ")

print(is_palindrome(word))
