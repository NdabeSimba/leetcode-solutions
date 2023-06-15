def count_dict(st):
    count = dict()
    for char in st:
        if char in count:
            count[char] = count.get(char) + 1
        else:
            count[char] = 1
    return count

st = "anagram"
print(count_dict(st))