def calcAddress(base, rowlb, collb, rowub, colub, element_size):
    n = colub - collb + 1  

    print(f"\nFor array a[{rowlb}:{rowub},{collb}:{colub}] with element size {element_size}")

    for i in range(rowlb, rowub + 1):
        for j in range(collb, colub + 1):
            const_part = (rowlb * n + collb) * element_size
            var_part = (i * n + j) * element_size
            address = base - const_part + var_part
            print(f"a[{i},{j}] address = {address}")


def main():
    calcAddress(1200, 0, 0, 2, 2, 1)
    calcAddress(100, 1, 1, 2, 2, 2)
    calcAddress(100, 2, 3, 4, 5, 4)
    calcAddress(100, -1, -1, 1, 2, 8)

if __name__ == "__main__":
    main()
