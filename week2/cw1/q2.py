import random

def random_sentence(names, verbs, adverbs):
    name = random.choice(names)
    verb = random.choice(verbs)
    adverb = random.choice(adverbs)
    return f"{name} {verb} {adverb}"


names = ["Ali", "Sara", "Reza"]
verbs = ["runs", "jumps", "eats"]
adverbs = ["quickly", "slowly", "happily"]

print(random_sentence(names, verbs, adverbs))