def get_res(txt):
    return sum([1 for x in txt.lower() if x in 'aeiou'])