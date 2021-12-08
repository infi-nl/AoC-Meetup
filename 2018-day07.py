# https://adventofcode.com/2018/day/7

with open('input-2018-day07.txt', 'r') as file:
    lines = file.read().splitlines()

edges = [(line.split(' ')[1], line.split(' ')[7]) for line in lines]


def get_start_nodes(edges):
    source_nodes = set(edge[0] for edge in edges)
    target_nodes = set(edge[1] for edge in edges)
    return source_nodes.difference(target_nodes)


print(get_start_nodes(edges))


def traverse(nodes):
    sorted_nodes = sorted(nodes)


def get_child_nodes(node):
    return set(edge[1] for edge in edges if edge[0] == node)


def get_parent_nodes(node):
    return set(edge[0] for edge in edges if edge[1] == node)


# --- Part 1 --- #

# output = ''
# while len(edges) > 0:
#     start_nodes = get_start_nodes(edges)
#     sorted_start_nodes = sorted(start_nodes)
#     start_node = sorted_start_nodes[0]
#     end_nodes = [edge[1] for edge in edges if edge[0] == start_node]
#     edges = [edge for edge in edges if edge[0] != start_node]
#     output += start_node
#     if len(edges) == 0:
#         sorted_end_nodes = sorted(end_nodes)
#         output += ''.join(sorted_end_nodes)
#
# print(output)

# --- Part 2 --- #

workers = [[None, 0] for _ in range(2)]
print(workers)

end_nodes = []
output = ''
seconds = -1
while len(edges) > 0 or len(end_nodes) > 0:
    end_nodes = []
    seconds += 1
    for worker in workers:
        if worker[0] is not None:
            worker[1] -= 1
            if worker[1] == 0:
                candidates = [edge[1] for edge in edges if edge[0] == worker[0]]
                edges = [edge for edge in edges if edge[0] != worker[0]]
                end_nodes += [node for node in candidates if node not in [edge[0] for edge in edges]]
                end_nodes = [node for node in end_nodes if node != worker[0]]
                output += worker[0]
                worker[0] = None

    in_progress_nodes = [worker[0] for worker in workers]
    start_nodes = [node for node in get_start_nodes(edges).union(set(end_nodes)) if node not in in_progress_nodes]
    sorted_start_nodes = sorted(start_nodes)

    for worker in workers:
        if len(sorted_start_nodes) == 0:
            continue
        if worker[0] is None:
            worker[0] = sorted_start_nodes[0]
            worker[1] = 1 + (ord(sorted_start_nodes[0]) - ord('A'))
            sorted_start_nodes = sorted_start_nodes[1:]

    print(f"seconds: {seconds}, workers: {workers}")

print(output)
print(seconds)
