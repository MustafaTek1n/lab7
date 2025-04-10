def count_characters(s):
    """Count the number of characters."""
    return len(s)

def count_words(s):
    """Count the number of words"""
    return len(s.split())

def average_word_length(s):
    """Calculate the average length"""
    words = s.split()
    if len(words) == 0:
        return 0
    return sum(len(word) for word in words) / len(words)
