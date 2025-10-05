def vorodi(matn):
    abc = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j",
           "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
           "u", "v", "w", "x", "y", "z","a"]
    matn = matn.lower()
    natije = ""
    for ch in matn:
        for i in range(len(abc)):
            if ch == abc[i]:
                natije += abc[i + 1]
                break

    return natije


print(vorodi("ABCZ"))