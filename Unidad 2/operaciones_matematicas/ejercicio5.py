def main():

    x = int(input("Introduce un número entero: "))

    if x < 1:
        print("Error: Introduce un número mayor o igual que 1.")
        return

    pascal = []

    for i in range(x):
        if i == 0:
            pascal.append([1])
        else:
            last_row = pascal[-1]
            new_row = [1]

            for j in range(len(last_row) - 1):
                new_row.append(last_row[j] + last_row[j + 1])

            new_row.append(1)
            pascal.append(new_row)

    for row in pascal:
        print(row)

if __name__ == "__main__":
    main()