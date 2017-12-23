nodes = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i')

current = 'a'
currentPath = 0
vis = {}
unvis = {n: None for n in nodes}
unvis[current] = currentPath

paths = {
    'a': {'b': 4, 'h': 8},
    'b': {'a': 4, 'h': 11, 'c': 8},
    'c': {'d': 7, 'f': 4, 'i': 2},
    'd': {'e': 9, 'f': 14},
    'e': {'d': 9, 'f': 10},
    'f': {'c': 4, 'd': 14, 'e': 10},
    'g': {'f': 2, 'h': 1, 'i': 6},
    'h': {'a': 8, 'b': 11, 'g': 1, 'i': 7},
    'i': {'c': 2, 'g': 6, 'h': 7}}

while True:
    for nextPath, path in paths[current].items():
        if nextPath not in unvis:
            continue
        nPath = currentPath + path
        if unvis[nextPath] is None or unvis[nextPath] > nPath:
            unvis[nextPath] = nPath

    vis[current] = currentPath
    del unvis[current]

    if not unvis:
        break
    list = [i for i in unvis.items() if i[1]]
    current, currentPath = sorted(list, key = lambda x: x[1])[0]

print(vis)
