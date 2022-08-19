total = 0
for i in range (1, 1000000):
    i_1 = i // 100000
    i_2 = i % 100000 // 10000
    i_3 = i % 10000 // 1000
    i_4 = i % 1000 // 100
    i_5 = i % 100 // 10
    i_6 = i % 10

    s1 = i_1 + i_2 + i_3
    s2 = i_4 + i_5 + i_6

    if s1 == s2:
        total = total + 1

print(total)
