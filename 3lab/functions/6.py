def reversed_words(s):
    l = []
    t = ""
    for x in s:

        if x == " ":
            l.append(t)
            t = ""
            continue
        t += x

    l.append(t)
    l.reverse()
    return l


s = input()
l = []
print(' '.join(reversed_words(s)))