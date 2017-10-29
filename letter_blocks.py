"""
problem description: https://www.reddit.com/r/dailyprogrammer/comments/6t0zua/20170811_challenge_326_hard_multifaceted_alphabet/

Idea is to try to maximize the number of words that can use any one block, temporarily discarding words once they have
been used for a block face.

"""
with open('real_words.txt') as fo:
    text = fo.read()
    word_list = text.splitlines()


def get_best_letter(sub):
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
        blocklist.append([])
        temp_word_list = word_list[:]
        for i in range(0, row+1):
            letter = get_best_letter(temp_word_list)
            if not letter:
                continue
            blocklist[row].extend(letter)
            word_list[:] = [word.replace(letter, '', 1) if word in temp_word_list else word for word in word_list]
            word_list[:] = [word for word in word_list if not word == '']
            temp_word_list[:] = [word for word in temp_word_list if letter not in word]
        row += 1
    return blocklist


blocklist = run(word_list)
for block in blocklist:
    print("".join(block))

