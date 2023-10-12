# Produtos cartesianos colors x sizes
colors = ['black', 'white']
sizes = ['S', 'M', 'L']
tshirts = [(color, size) for color in colors for size in sizes]
tshirts2 = [(color, size) for size in sizes for color in colors]

if __name__ == "__main__":
    print(tshirts)
    print(tshirts2)

    for color in colors:
        for size in sizes:
            print((color, size))
