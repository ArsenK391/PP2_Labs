import re

def insert_spaces(S):
    pattern = r'(?<!^)(?=[A-Z])'
    
    result = re.sub(pattern, ' ', S)
    
    return result

S = [
    "HelloWorld",
    "ThisIsATest",
    "InsertSpacesBetweenWords",
    "StartingWithCapitalLetters",
    "PythonProgrammingLanguage"
]

for test in S:
    print(f"'{insert_spaces(test)}'")