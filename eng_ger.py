
def get_word_pairs(txt_file):
    with open(txt_file) as doc:
        word_pairs = doc.read().splitlines()
    for item in word_pairs:
        eng = item.split('\t')[0].lower()
        ger = item.split('\t')[1].lower()
        print(eng + " * " + ger)

        iterative_levenshtein(eng, ger)


def iterative_levenshtein(s, t, *cost, **weight_dict):

    rows = len(s)+1
    cols = len(t)+1

    ## English and German alphabets
    alphabet = "abcdefghijklmnopqrstuvwxyzäöüß"

    ## case insensitive
    if cost:
        w = dict( (x, cost) for x in alphabet)
    else:
        w = dict( (x, (1, 1, 1)) for x in alphabet)

    if weight_dict:
        w.update(weight_dict)

    dist = [[0 for x in range(cols)] for x in range(rows)]

    for row in range(1, rows):
        dist[row][0] = dist[row-1][0] + w[s[row-1]][0]

    for col in range(1, cols):
        dist[0][col] = dist[0][col-1] + w[t[col-1]][1]


    for col in range(1, cols):
        for row in range(1, rows):
            deletes = w[s[row-1]][0]
            inserts = w[t[col-1]][1]
            subs = max( ( w[s[row-1]][2], w[t[col-1]][2] ) )
            if s[row-1] == t[col-1]:
                subs = 0
            else:
                subs = subs

            dist[row][col] = min(dist[row-1][col] + deletes,
                                 dist[row][col-1] + inserts,
                                 dist[row-1][col-1] + subs)

    edit_cost = dist[row][col]

    ## adjusting edit cost
    if not (s.startswith('t') and t.startswith('z')) \
    and not (s.startswith('th') and t.startswith('d')) \
    and not (s.endswith('day') and t.endswith('tag')):
        print("edit cost: " + str(edit_cost))
    else:
        print("edit cost BEFORE adjustman: " + str(edit_cost))
        if s.startswith('t') and t.startswith('z') or s.startswith('th') and t.startswith('d'):
            edit_cost = edit_cost - 1
        if s.endswith('day') and t.endswith('tag'):
            edit_cost = edit_cost - 2
        print("edit cost AFTER adjustman: " + str(edit_cost))

    ave_length = (len(s) + len(t)) / 2.00
    print("average length of word pairs: " + str(ave_length))


    ## evaluation
    if edit_cost >= ave_length * 0.9:
        print("Don't seem to be cognates\n")
    elif edit_cost >= ave_length * 0.75:
        print("Somewhat unlikely to be cognate\n")
    elif edit_cost >= ave_length * 0.5:
        print("Somewhat likely to be cognates\n")
    else:
        print("Likely to be cognates\n")

    return


if __name__ == '__main__':
    get_word_pairs('input/eng_ger.txt')
