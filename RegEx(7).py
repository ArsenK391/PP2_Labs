import re

def snake_to_camel(snake_str):
    components = snake_str.split('_')
    camel_str = components[0] + ''.join(x.title() for x in components[1:])
    return camel_str


S = [
    "hello_world",
    "this_is_a_test",
    "convert_snake_to_camel",
    "example_string",
    "snake_case_to_camel_case"
]

for test in S:
    print(f"Camel Case: '{snake_to_camel(test)}'")