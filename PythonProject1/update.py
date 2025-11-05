def main():
    LA = [1, 3, 5, 7, 8]
    k = 5
    j = 2
    n = len(LA)
    item = 10
    items = 6
    print("The original array elements are: \n")
    for i in range(n):
        print(f"LA[{i}] = {LA[i]}")

    if 0 <= k - 1 < n:
        LA [k - 1] = item
        LA [j - 1] = items
    else:
        print(f"Error: Index {k-1} is out of bounds for the list of size {n}.")

    print("\nThe array elements after deletion: ")
    for i in range(n):
        print(f"LA[{i}] = {LA[i]}")

if __name__ == "__main__":
    main()