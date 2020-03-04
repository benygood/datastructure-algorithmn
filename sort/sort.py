#mao pao/bubble
def bubble_sort(a):
    #stable
    n = len(a)
    cmp_count = 0
    swap_count = 0
    for i in range(n-1):
        swaped = False
        for j in range(n-1-i):
            cmp_count += 1
            if a[j] > a[j+1]:
                temp = a[j]
                a[j] = a[j+1]
                a[j+1] = temp
                swap_count += 1
                swaped = True
        if not swaped:
            break
    print("n={}, i={}, cmp_count={}, swap_count={}".format(n, i, cmp_count, swap_count))
    print(a)

def select_sort(a):
    #unstable because of swap
    n = len(a)
    cmp_count = 0
    swap_count = 0
    for i in range(n-1):
        min = a[i]
        min_index = i
        for j in range(i+1, n):
            cmp_count += 1
            if a[j] < min:
                min = a[j]
                min_index = j
                swap_count += 1
        a[min_index] = a[i]
        a[i] = min

    print("n={}, i={}, cmp_count={}, swap_count={}".format(n, i, cmp_count, swap_count))
    print(a)

def insert_sort(a):
    #stable
    n = len(a)
    cmp_count = 0
    assign_count = 0
    for i in range(1, n):
        a_i = a[i]
        insert_pos = i
        for j in range(i-1,-1,-1):
            cmp_count += 1
            if a_i < a[j]:
                a[j+1] = a[j]
                assign_count += 1
                insert_pos = j
            else:
                break
        a[insert_pos] = a_i
    print("n={}, i={}, cmp_count={}, assign_count={}".format(n, i, cmp_count, assign_count))
    print(a)


def test(func):
    a = [1,2,3,4,5,6,7,8,9]
    b = a[::-1]
    c = [100,200,4,45,343,2,55,111,566,1000,2,102]
    func(a)
    func(b)
    func(c)

print("========bubble_sort========")
test(bubble_sort)
print("========select_sort========")
test(select_sort)
print("========insert_sort========")
test(insert_sort)