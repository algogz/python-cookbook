graph1 = {
    'start': {
        'a': 6,
        'b': 2
    },
    'a': {
        'fin': 1
    },
    'b': {
        'a': 3,
        'fin': 5
    },
    'fin': {}
}

graph = {
    'start': {
        'a': 5,
        'b': 2
    },
    'a': {
        'c': 4,
        'd': 2
    },
    'b': {
        'a': 8,
        'd': 7
    },
    'c': {
        'fin': 3,
        'd': 6
    },
    'd': {
        'fin': 1
    },
    'fin': {}
}

infinity = float('inf')
costs = {
    'a': 5,
    'b': 2,
    'c': infinity,
    'd': infinity,
    'fin': infinity
}

parents = {
    'a': 'start',
    'b': 'start',
    'c': None,
    'd': None,
    'fin': None
}

processed = []


def find_lowest_cost_node(costs):
    lowest_cost = infinity
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    print(f"lowest cost node found: {lowest_cost_node}")
    return lowest_cost_node


node = find_lowest_cost_node(costs)
while node is not None:
    cost = costs[node]
    neighbors = graph[node]
    print(f'\tneighbors {neighbors.keys()}')
    for n in neighbors.keys():
        new_cost = cost + neighbors[n]
        if costs[n] > new_cost:
            costs[n] = new_cost
            parents[n] = node
            print(f'\tupdated {parents[n]} <== {n}(cost={costs[n]})')
    processed.append(node)
    node = find_lowest_cost_node(costs)

# output
node = 'fin'
while True:
    if node == 'start':
        break
    parent = parents[node]
    cost = graph[parent][node]
    print(f"{node}({cost})", end='<==')
    node = parent
print('start\n')
