import re

def split_at_uppercase(S):
    pattern = r'(?=[A-Z])'
    split_strings = re.split(pattern, S)
    split_strings = [s for s in split_strings if s]
    return split_strings


S = [
    "HelloWorld",
    "ThisIsATest",
    "SplitAtUppercase",
    "UppercaseLetters",
    "PythonProgrammingLanguage"
]

for test in S:
    print(split_at_uppercase(test))