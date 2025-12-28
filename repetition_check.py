def is_repeated(text, turns):
    for t in turns:
        if text[:50] in t["text"]:
            return True
    return False
