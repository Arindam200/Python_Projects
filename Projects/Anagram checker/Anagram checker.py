#Check if two strings are anagrams

def is_anagram():
    firstw =input('your first word goes here...\n ')
    secondw = input('and the other word goes here...\n ')
    return sorted(firstw) == sorted(secondw)