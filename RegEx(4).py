import re

def find_sequences(S):
    pattern = r'\b[A-Z][a-z]+\b'
    matches = re.findall(pattern, S)
    return matches

S = [
    "Hello",
    "world",
    "This is a Test",
    "AnotherExample",
    "UPPER lower",
    "camelCase",
    "Python Programming"
]

for test in S:
    print(f"'{test}: {find_sequences(test)}'")