import re

def match_a_anything_b(S):
    pattern = r'^a.*b$'
    
    if re.match(pattern, S):
        return True
    else:
        return False
    
S = ["ab", "a123b", "axyzb", "abbb", "a", "b", "ba", "aab", "ab", "acb"]

for test in S:
    print(f"'{test}': {match_a_anything_b(test)}")