def popular_words(text, words):
    res = {}
    text = tuple(text.lower().split())
    for i in text:
        for j in words:
            res[j] = res.get(j, 0)
            if j == i:
                res[i] = res.get(i, 0) + 1
    return res




i = popular_words('''When I was One I had just begun When I was Two I was nearly new ''', ['i', 'was', 'three', 'near'])

print(i)

# assert popular_words('''When I was One I had just begun When I was Two I was nearly new ''', ['i', 'was', 'three', 'near']) == { 'i': 4, 'was': 3, 'three': 0, 'near': 0 }, 'Test1'
# print('OK')

