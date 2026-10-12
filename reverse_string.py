# problem 3: reverse_string(s): reverse a string without using [::-1] or reversed().
#"hello" → "olleh"

def reverse_string(text):
    results = ""
    for i in range(len(text)- 1, -1, -1):
        results = results + text[i]
    return results

assert reverse_string("hello") == "olleh"
assert reverse_string("a") == "a"
assert reverse_string("") == ""

print("all tests have passed")