import re

def camel_to_snake(camel_str):
    pattern = r'([a-z0-9])([A-Z])'
    snake_str = re.sub(pattern, r'\1_\2', camel_str).lower()
    return snake_str

S = [
    "helloWorld",
    "thisIsATest",
    "convertCamelToSnake",
    "exampleString",
    "camelCaseToSnakeCase"
]

for test in S:
    print(f"'{camel_to_snake(test)}'")