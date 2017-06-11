from collections import Counter
def count_words(text):
    text=text.lower()
    skips = ['.', ',', ';', ':', '"', "'"]
    for ch in skips:
        text = text.replace(ch, '')

    word_counts = Counter(text.split(" "))
    return word_counts

print(len(count_words("This comprehension check is to check for comprehension.")))