#problem 1: count_vowels(s): count the vowels in a string.
# "leetcode" → 4

def count_vowels(word):
    count= 0
    english_vowels = ["a","e","i", "o", "u", "y"]
    for n in word:
        if n in english_vowels:
            print(n, count)
            count = count + 1
    return count

#print(count_vowels("Yahya"))  # should be 4
print(f"The final vowel count is: {count_vowels('Yahya')}") # I learned how to use f-string
