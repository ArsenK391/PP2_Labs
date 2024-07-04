import re

def match_ab_patterns(S):
    pattern = r'^ab{2,3}$'
    if re.match(pattern, S):
        return True
    else:
        return False
    

S = ["a", "ab", "abb", "abbb", "abbbb", "b", "ba", "aab", "abc"]
for test in S:
    print(f"'{test}': {match_ab_patterns(test)}")