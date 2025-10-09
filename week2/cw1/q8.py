def to_morse(word) :
    morse_dict = {
        "a": ".-",  "b": "-...",  "c": "-.-.", "d": "-..",
        "e": ".",   "f": "..-.",  "g": "--.",   "h": "....",
        "i": "..",   "j": ".---",  "k": "-.-",   "l": ".-..",
        "m": "--",   "n": "-.",    "o": "---",   "p": ".--.",
        "q": "--.-", "r": ".-.",   "s": "...",   "t": "-",
        "u": "..-",  "v": "...-",  "w": ".--",   "x": "-..-",
        "y": "-.--", "z": "--.."," ": "" }

    word = word.lower()
    result = ""

    for ch in word:
        if ch in morse_dict:
            result += morse_dict[ch] + " "
        else:
            result += "not right"

    return result.strip()
print(to_morse("Sed Mehdi Alavi"))