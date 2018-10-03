string = "abcabacdea"
pat = "f"


def find(pattern):
    if pattern == "":
        return -1
    return string.find(pattern)

print(find(pat))
