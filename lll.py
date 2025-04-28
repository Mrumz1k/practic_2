def count_jewels_in_stones(J, S):
    jewels = set(J)
    count = 0
    for stone in S:
        if stone in jewels:
            count += 1
    return count

J = input("Введите строку J (драгоценности): ")
S = input("Введите строку S (камни): ")

print(count_jewels_in_stones(J, S))