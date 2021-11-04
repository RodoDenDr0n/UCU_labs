def generate_pascal_triangle(height):
    triangle = []
    triangle_elements = []

    for i in range(height):
        triangle_elements.append(1)
        triangle.append(tuple(triangle_elements))

    for i in range(len(triangle)):
        triangle[i] = list(triangle[i])

    for i in range(2, len(triangle)):
        try:
            for j in range(len(triangle[i])):
                try:
                    triangle[i][j+1] = triangle[i-1][j] + triangle[i-1][j+1]
                except:
                    continue
        except:
            break

    return triangle

print(generate_pascal_triangle(-1))
