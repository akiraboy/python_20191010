print('  ', end="")

for x in range(10):
    print(f"{x:2}", end=" ")
print()

for i in range(10):
    print(i, end=" ")
    for y in range(10):
        print(f"{y * i:2}", end=" ")
    print()
