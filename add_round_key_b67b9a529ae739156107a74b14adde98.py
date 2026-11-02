state = [
    [206, 243, 61, 34],
    [171, 11, 93, 31],
    [16, 200, 91, 108],
    [150, 3, 194, 51],
]

round_key = [
    [173, 129, 68, 82],
    [223, 100, 38, 109],
    [32, 189, 53, 8],
    [253, 48, 187, 78],
]
def matrix2byte(matrix):
    full_list = [item for sublist in matrix for item in sublist]
    return bytes(full_list)

def add_round_key(s, k):
    result = [[i^j for i,j in zip(s_row,k_row)]
    for s_row,k_row in zip(s,k)]
    return result


print(matrix2byte(add_round_key(state, round_key)))