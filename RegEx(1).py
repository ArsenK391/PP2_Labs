import re

def match_ab_pattern(S):
    pattern = r'^ab*$'

    if re.match(pattern, S):
        return True
    else:
        return False
    

S = ["a", "ab", "abb", "abbb", "b", "ba", "aab", "abc"]
for test in S:
    print(f"'{test}': {match_ab_pattern(test)}")