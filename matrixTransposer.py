input_matrix = [[1, 2, 3, 4],
                [5, 6, 7, 8]]
output_matrix = [[x[y] for x in input_matrix] for y in range(len(input_matrix[1]))]

print(output_matrix)
