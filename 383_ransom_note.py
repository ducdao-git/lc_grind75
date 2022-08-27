from collections import Counter


def can_construct(ransomNote, magazine):
    ransomNote = Counter(ransomNote)
    magazine = Counter(magazine)

    return ransomNote == ransomNote & magazine
