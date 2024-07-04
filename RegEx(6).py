import re

def replace_with_colon(S):
    pattern = r'[,.]'
    result = re.sub(pattern, ':', S)
    return result

S = [
    "Hello, world. This is a test.",
    "Python, programming language.",
    "Space, comma, and dot.",
    "Replace all spaces, commas, and dots."
]

for test in S:
    print(replace_with_colon(test))