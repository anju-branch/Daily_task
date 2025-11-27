#program for determining whether the string is a pangram

def is_pangram(s):
    return len({c for c in s.lower() if 'a' <= c <= 'z'}) == 26


#Test example

print(is_pangram("Pack my box with five dozen liquor jugs"))   # True
print(is_pangram("Bright vases on the table look nice"))       # False
