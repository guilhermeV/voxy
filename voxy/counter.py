from collections import Counter
import re


def count(text_block):
    words = re.findall(r'\w+', text_block.lower())
    return {'quantity': len(words), 'distinct': len(Counter(words))}