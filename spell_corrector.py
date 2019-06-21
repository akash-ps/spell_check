
import dill
alphabet = 'abcdefghijklmnopqrstuvwxyz'
data_prep_path = "./"
with open("C:\\Users\\AKASH\\Downloads\\" +"spell_model", 'rb') as spell_model:
    NWORDS = dill.load(spell_model)

def edits1(word):
    splits = [(word[:i], word[i:]) for i in range(len(word) + 1)]
    deletes = [a + b[1:] for a, b in splits if b]
    transposes = [a + b[1] + b[0] + b[2:] for a, b in splits if len(b) > 1]
    replaces = [a + c + b[1:] for a, b in splits for c in alphabet if b]
    inserts = [a + c + b for a, b in splits for c in alphabet]
    return set(deletes + transposes + replaces + inserts)


def known_edits2(word):
    return set(e2 for e1 in edits1(word) for e2 in edits1(e1) if e2 in NWORDS)


def known(words):
    return set(w for w in words if w in NWORDS)


def correct(word):
    candidates = known([word]) or known(edits1(word)) or known_edits2(word) or [word]
    return max(candidates, key=NWORDS.get)


def spell_check(text):
    #print('Lower case query...',text)
    words = (text.split())
    correct_words = []
    for i in words:
        correct_words.append(correct(i))
    return " ".join(correct_words)


if __name__ == "__main__":
    print(spell_check("artifica inteligenc intenet"))
