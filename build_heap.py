# python3
# Kristiāns Martiņjaks 221RDB223

def build_heap(data):
    swaps = []
    n = len(data)

    for i in range(n // 2, -1, -1):
        minHeap(data, n, i, swaps)
    return swaps

def minHeap(data, n, i, swaps):
    lSide = 2 * i + 1
    rSide = 2 * i + 2
    min = i

    if lSide <= n - 1 and data[lSide] < data[min]:
        min = lSide
    if rSide <= n - 1 and data[rSide] < data[min]:
        min = rSide
    if i != min:
        data[i], data[min] = data[min], data[i]
        swaps.append((i, min))
        minHeap(data, n, min, swaps)

    return swaps


def main():
    

    inputs = input()
    if "I" in inputs:
        n = int(input())
        data = list(map(int, input().split()))
    elif "F" in inputs:
        inputs2 = input()
        if "a" not in inputs2:
            with open("./tests/"+inputs2, mode='r') as fails:
                n = int(fails.readline())
                data = list(map(int,fails.readline().split()))
    else:
        print("error")
        return

    assert len(data) == n


    swaps = build_heap(data)

    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
