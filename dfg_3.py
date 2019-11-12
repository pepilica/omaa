res = {}
sort_res = {}
for i in range(int(input())):
    word = input().lower()
    a = tuple(sorted(word))
    if a not in res.keys():
        res[a] = [word]
        sort_res[a] = word
    else:
        sort_res[a] = min(sort_res[a], word)
        if word not in res[a]:
            res[a].append(word)
d = {}
for key in res.keys():
    d[sort_res[key]] = res[key]
keys = sorted(d.keys())
for k in keys:
    if len(d[k]) > 1:
        print(*sorted(d[k]))
