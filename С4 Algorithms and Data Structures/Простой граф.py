G = {
    'A': {'B': 5, 'C': 3},
    'B': {'A': 5, 'C': 4},
    'C': {'A': 3, 'B': 4}
}

D = {'A': 0, 'B': 100, 'C': 100}

min_k = min([k for k in D.keys()], key=lambda x: D[x])
print(min_k) # A

# for v in G[min_k].keys()
# for v in ['B', 'C']:
D['B'] = min(D['B'], D[min_k] + G[min_k]['B'])


# D = min('B','C', key = lambda x:G['A'][x])
print(D['B'])