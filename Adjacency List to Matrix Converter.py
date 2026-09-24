def adjacency_list_to_matrix(adj_list):
    nodes_number = len(adj_list)

    matrix = [[0 for _ in range(nodes_number)] for _ in range(nodes_number)]

    for node, neighbors in adj_list.items():
        for neighbor in neighbors:
            matrix[node][neighbor] = 1

    for row in matrix:
        print(row)

    return matrix
