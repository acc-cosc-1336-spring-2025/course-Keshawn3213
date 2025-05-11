def get_hamming_distance(dna1, dna2):
    distance = 0
    for i in range(len(dna1)):
        if dna1[i] != dna2[i]:
            distance += 1
    return distance

def get_dna_complement(dna):
    complement = ''
    for i in range(len(dna) - 1, -1, -1):
        base = dna[i]
        if base == 'A':
            complement += 'T'
        elif base == 'T':
            complement += 'A'
        elif base == 'C':
            complement += 'G'
        elif base == 'G':
            complement += 'C'

