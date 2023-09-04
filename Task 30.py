def arithmetic_progression(a1, d, n):
    progression = [a1 + i * d for i in range(n)]
    print(" ".join(map(str, progression)))

a1 = int(input("Enter the first term of the arithmetic progression: "))
d = int(input("Enter the difference of the arithmetic progression: "))
n = int(input("Enter the number of terms of the arithmetic progression: "))
arithmetic_progression(a1, d, n)