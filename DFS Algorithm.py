def dfs(adj_list, node):
    stack = [node]
    visited = [False] * len(adj_list)
    result = []

    while stack:
        checked_node = stack.pop()

        if not visited[checked_node]:
            visited[checked_node] = True
            result.append(checked_node)

            for neighbor in range(len(adj_list)):
                if adj_list[checked_node][neighbor] == 1:
                    stack.append(neighbor)

    return result


print(dfs([
    [0, 1, 0, 0],
    [1, 0, 1, 0],
    [0, 1, 0, 1],
    [0, 0, 1, 0]
], 1))
