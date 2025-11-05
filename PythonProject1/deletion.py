def main():
    LA = [1, 2, 3, 4, 5]
    k = 3
    n = len(LA)

    print("The original array elements are: ")
    for i in range(n):
        print(f"LA[{i}] = {LA[i]}")

    j = k
    if 0 <= k - 1 < n:
        while j < n:
            LA [j - 1] = LA[j]
            j = j + 1
        n = n - 1
        LA = LA[:n]
    print("\nThe array elements after deletion:")
    for i in range(n):
        print(f"LA[{i}] = {LA[i]}")

if __name__ == "__main__":
    main()