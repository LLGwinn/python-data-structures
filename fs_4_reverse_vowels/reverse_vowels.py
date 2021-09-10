def reverse_vowels(s):
    """Reverse vowels in a string.

    Characters which re not vowels do not change position in string, but all
    vowels (y is not a vowel), should reverse their order.

    >>> reverse_vowels("Hello!")
    'Holle!'

    >>> reverse_vowels("Tomatoes")
    'Temotaos'

    >>> reverse_vowels("Reverse Vowels In A String")
    'RivArsI Vewols en e Streng'

    reverse_vowels("aeiou")
    'uoiea'

    reverse_vowels("why try, shy fly?")
    'why try, shy fly?''
    """

    sList = list(s)
    foundVowels = []
    vowelPositions = []

    for i in range(len(sList)):
        if s[i].lower() in 'aeiou':
            foundVowels.append(s[i])
            vowelPositions.append(i)

    revVowelPositions = vowelPositions[::-1]

    for i in range(len(revVowelPositions)):
        sList[revVowelPositions[i]] = foundVowels[i]   

    return ''.join(sList)

    
    
