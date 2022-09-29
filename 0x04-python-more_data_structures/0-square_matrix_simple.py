#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    Nsquare = []
    i = 0
    for x in matrix:
        Nsquare.append([])
        for y in matrix[i]:
            Nsquare[i].append(y**2)
        i += 1
    return (Nsquare)
