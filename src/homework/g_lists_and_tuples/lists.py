def get_p_distance(list1, list2):
    differences = 0
    for a, b in zip(list1, list2):
        if a != b:
            differences += 1
    return differences / len(list1)


def get_p_distance_matrix(dna_lists):
    size = len(dna_lists)
    matrix = [[0.0] * size for _ in range(size)]

    for i in range(size):
        for j in range(size):
            if i != j:
                matrix[i][j] = round(get_p_distance(dna_lists[i], dna_lists[j]), 5)
    return matrix
