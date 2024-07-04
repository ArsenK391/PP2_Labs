import re

def find_sequences(S):
    pattern = r'\b[a-z]+_[a-z]+\b'
    matches = re.findall(pattern, S)
    return matches

S = [
    "hello_world",
    "hello_World",
    "Hello_world",
    "hello_world_123",
    "hello_world_again",
    "another_example",
    "no_underscore_here",
    "lowercase_only"
]

for test in S:
    print(f"'{test}': {find_sequences(test)}")