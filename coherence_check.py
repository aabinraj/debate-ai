def is_coherent(text, topic):
    return topic.lower().split()[0] in text.lower()
