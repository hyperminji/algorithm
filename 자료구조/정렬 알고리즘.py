"기수 정렬 알고리즘[Radix Sort]"
def radix(order):
    is_sorted = False
    position = 1

    while not is_sorted:
        is_sorted = Truequeue_list = [list() for _ in range(10)]

        for num in order:
            digit_number = (int) (num/position) % 10
            queue_list[digit_number].append(num)
            if is_sorted and digit_number > 0:
                is_sorted = False
        index=0

        for numbers in queue_list:
            for num in numbers:
                order[index] = num
                index = index +1
        position = position *10

x=[5, 2, 8, 6, 1, 9, 3, 7]
radix(x)
print(x)

"선택 정렬 알고리즘[SelectionSort]"
'''
가장 작은 데이터를 찾아서 제일 앞의 데이터와 교환하는 알고리즘
'''
def change(x, i, j):
    x[i], x[j] = x[j], x[i]

def selectionSort(x):
    for size in reversed(range(len(x))):
        max_i = 0
        for i in range(1, 1+size):
            if x[i] > x[max_i]:
                max_i = i
        change(x, max_i, size)

x=[5, 2, 8, 6, 1, 9, 3, 7]
selectionSort(x)
print(x)

"교환 정렬 알고리즘[Exchange Sort]"

'''
인접한 2개의 숫자를 비교하여 작은 숫자가 왼쪽에 가도록 교환 반복
'''
def exchangeSort(x):
    if len(x) > 1:
        mid = len(x) //2
        colx, rowx = x[:mid], x[mid:]
        exchangeSort(colx)
        exchangeSort(rowx)

        coli, rowi, i = 0,0,0
        while coli < len(colx) and rowi < len(rowx):
            if cols[coli] < rowx[rowi]:
                x[i] = colx[coli]
                coli = coli+1
            else:
                x[i] = rowx[rowi]
                rowi = rowi+1
            i = i+1
        x[i:] = colx[coli:] if coli != len(colx) else rowx[rowi :]


x=[5,2,8,6,1,9,3,7]
exchangeSort(x)
print(x)

"삽입 정렬 알고리즘[InsertSort]"
def insertSort(x):
    for size in range(1, len(x)):
        val = x[size]
        i = size

        while i>0 and x[i-1] > val:
            x[i] = x[i-1]
            i = i-1
        x[i] = val

x=[5,2,8,6,1,9,3,7]
insertSort(x)
print(x)


"쉘 정렬 알고리즘(Shell Sort)"
'''
삽입정렬 알고리즘의 속도 보완, 데이터의 그룹을 나누어 쉘정렬 수행 후 마지막에 삽입정렬
'''
def Between(x, start, ranges):
    for target in range(start+ranges, len(x), ranges):
        val = x[target]
        i = target
        while i> start:
            if x[i - ranges] > val:
                x[i] = x[i-ranges]
            else:
                break
            i = i-ranges
        x[i] = val

def shellSort(x):
    ranges = len(x) //2
    while ranges > 0:
        for start in range(ranges):
            Between(x, start, ranges)
        ranges = ranges//2

x=[5,2,8,1,9,3,7]
shellSort(x)
print(x)

"퀵 정렬 알고리즘[Quick Sort]"
'''
데이터를 중심으로 데이터 2등분
첫번째 원소를 기준으로 데이터 분리
반복
'''
def change(x, i, j):
    x[i], x[j] = x[j], x[i]

def Select(x, l, r):
    select_val = x[l]
    select_idx = l
    while l <= r:
        while l<= r and x[l] <= select_val:
            l= l+1
        while l <= r and x[r] >= select_val:
            r = r-l
        if l <= r:
            change(x, l, r)
            l = l+1
            r = r-1
    change(x, select_idx, r)
    return r

def quickSort(x, pivotMethod = Select):
    def Qsort(x, first, last):
        if first < last:
            splitP = pivotMethod(x, first, last)
            Qsort(x, first, split-l)
            Qsort(x, splitP+l, last)
    Qsort(x, 0, len(x)-1)

x=[5,2,8,6,1,9,3,7]
quickSort(x)
print(x)