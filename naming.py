import random

vowels = ("a", "e", "i", "o", "u", "y")
consonants = ("b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z",
              "ch", "gh", "ph", "sh", "th")
metalsuffix = ("ium", "lium")

def metalname():
    namestring = random.choice(consonants)
    namestring = namestring + random.choice(vowels)
    namestring = namestring + random.choice(consonants)
    namestring = namestring + random.choice(metalsuffix)
    return namestring
