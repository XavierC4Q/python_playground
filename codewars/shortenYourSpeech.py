def shorten_your_speech(strs):
    '''
    :strs A string of words
    :If word has more than four letters only include four letters + a .
    or if the 4th letter is a vowel, a dot. Words shorter than 4 are not
    affected.
    '''
    words = strs.split()
    result = []
    vowels = 'aeiou'
    
    for w in words:
        if len(w) < 4:
            result.append(w)
        else:
            rest = w[3:]
            pushed = False
            for l in range(len(rest)):
                if rest[l] in vowels:
                    result.append(w[:3 + l] + '.')
                    pushed = True
                    break
            if not pushed:
                result.append(w)
    return ' '.join(result)


print(shorten_your_speech('Hello fellow warriors !'))