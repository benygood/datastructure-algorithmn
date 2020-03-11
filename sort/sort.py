#mao pao/bubble
def bubble_sort(a):
    #stable
    n = len(a)
    cmp_count = 0
    assign_count = 0
    for i in range(n-1):
        swaped = False
        for j in range(n-1-i):
            cmp_count += 1
            if a[j] > a[j+1]:
                temp = a[j]
                a[j] = a[j+1]
                a[j+1] = temp
                assign_count += 3
                swaped = True
        if not swaped:
            break
    print("n={}, i={}, cmp_count={}, assign_count={}".format(n, i, cmp_count, assign_count))
    print(a)

def select_sort(a):
    #unstable because of swap
    n = len(a)
    cmp_count = 0
    assign_count = 0
    for i in range(n-1):
        min = a[i]
        min_index = i
        for j in range(i+1, n):
            cmp_count += 1
            if a[j] < min:
                min = a[j]
                min_index = j
                assign_count += 2
        assign_count += 2
        a[min_index] = a[i]
        a[i] = min

    print("n={}, i={}, cmp_count={}, assign_count={}".format(n, i, cmp_count, assign_count))
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
                assign_count += 2
                insert_pos = j
            else:
                break
        assign_count += 1
        a[insert_pos] = a_i
    print("n={}, i={}, cmp_count={}, assign_count={}".format(n, i, cmp_count, assign_count))
    print(a)

def quick_sort(a):
    n = len(a)
    if n<=1: return a, 0, 0
    pivot = a[0]

    cmp = assign = 0

    #不稳定排序
    # i=1
    # j=n-1
    # while i <= j:
    #     while j>0 and a[j] >= pivot: j-=1
    #     while i<=j and i<n and a[i] <= pivot:  i+=1
    #     if i<j:
    #         temp = a[i]
    #         a[i] = a[j]
    #         a[j] = temp
    #         j-=1
    #         i+=1
    # l = quick_sort(a[1:i])
    # r = quick_sort(a[i:n])

    #不稳定排序
    j = i = 1
    while i<n:
        cmp += 1
        if a[i] < pivot:
            cmp += 1
            if i!=j:
                assign += 3
                temp = a[i]
                a[i] = a[j]
                a[j] = temp
            j += 1
        i+=1

    l,l_cmp,l_assign = quick_sort(a[1:j])
    r,r_cmp,r_assign = quick_sort(a[j:n])

    #如何让快速排序变稳定:
    #   不采用交换，借助额外空间，把小于或大于pivot的值放两个数组里，等于pivot的要看原来在pivot左边还是右边，来决定放哪边
    return l+[pivot]+r,cmp+l_cmp+r_cmp, assign+l_assign+r_assign

def quick_sort_wrap(a):
    n = len(a)
    ret, cmp, assign = quick_sort(a)
    print("n={}, cmp_count={}, assign_count={}".format(n, cmp, assign))
    print(ret)

def merge_sort(a):
    if len(a) <= 1:
        return a, 0, 0
    n = len(a)
    l,l_cmp,l_assign = merge_sort(a[:n//2])
    r,r_cmp,r_assign = merge_sort(a[n//2:])
    i = j = 0
    c = []
    cmp = assign = 0
    while i<len(l) and j<len(r):
        cmp += 1
        assign += 1
        if l[i] > r[j]:
            c.append(r[j])
            j+=1
        else:
            c.append(l[i])
            i+=1
    if i < len(l):
        assign += len(l) - i
        c.extend(l[i:])
    if j < len(r):
        assign += len(r) - j
        c.extend(r[j:])
    return c, cmp+l_cmp+r_cmp, assign+l_assign+r_assign

def merge_sort_wrap(a):
    n = len(a)
    ret, cmp, assign = merge_sort(a)
    print("n={}, cmp_count={}, assign_count={}".format(n, cmp, assign))
    print(ret)


def test(func):
    a = [1,2,3,4,5,6,7,8,9]
    b = a[::-1]
    c = [100,200,4,45,343,2,55,111,566,1000,2,102]
    d = [13,999,4,4,90,4,100,102,50,1,3,50,7]
    func(a)
    func(b)
    func(c)
    func(d)

print("========bubble_sort========")
test(bubble_sort)
print("========select_sort========")
test(select_sort)
print("========insert_sort========")
test(insert_sort)
print("========quick_sort========")
test(quick_sort_wrap)
print("========merge_sort========")
test(merge_sort_wrap)