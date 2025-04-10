def reverse_string(s):
    """reversed"""
    return s[::-1]

def capitalize_words(s):
    """Capitalize"""
    return ' '.join(word.capitalize() for word in s.split())

def remove_punctuation(s):
    """Remove"""
    import string
    return s.translate(str.maketrans('', '', string.punctuation))
