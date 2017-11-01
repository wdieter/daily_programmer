"""
problem description: https://www.reddit.com/r/dailyprogrammer/comments/6t0zua/20170811_challenge_326_hard_multifaceted_alphabet/

Idea is to try to maximize the number of words that can use any one block, temporarily discarding words once they have
been used for a block face.
For example: the ideal solution for a list of words with length of 12 letters would be a block set of length 12 where each block 
is used by 100% of the words. This algorithm attemps to cover each word with each block to attempt 100% word coverage per block. 
"""

with open('real_words.txt') as fo:
    text = fo.read()
    word_list = text.splitlines()

def get_best_letter(sub):
    # best letter defined as the letter that appears in most words
    letter_dict = get_letter_dict(sub)
    try:
        return max(letter_dict, key=letter_dict.get)
    except:
        return False

def get_letter_dict(words):
    # returns dict containing all unique letters like {a:3, b:1, c:2...}
    # where a is present (at least once) in 3 words, b in 1 word...
    d = {}
    for word in words:
        for unique_letter in set(word):
            d[unique_letter] = d.get(unique_letter, 0) + 1
    return d

def run(word_list):
    blocklist = []
    row = 0
    while word_list:
        blocklist.append([]) # add new block
        temp_word_list = word_list[:] # create a copy of word list contents, not object word list is bound to
        for i in range(0, row+1): 
            letter = get_best_letter(temp_word_list)
            if not letter: 
                continue  # all words have been used for this block, cannot use block more than once
            blocklist[row].extend(letter)
            # replace ONLY ONE instance of letter in word
            word_list[:] = [word.replace(letter, '', 1) if word in temp_word_list else word for word in word_list]
            # drop words that can be spelled completely with blockset
            word_list[:] = [word for word in word_list if not word == '']
            # drop words that have been used for current block
            temp_word_list[:] = [word for word in temp_word_list if letter not in word]
        row += 1
    return blocklist

blocklist = run(word_list)
for block in blocklist:
    print("".join(block))

