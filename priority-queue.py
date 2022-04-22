"""

Задача на программирование: очередь с приоритетами

Первая строка входа содержит число операций 1≤n≤105 1 \le n \le 10^5 1≤n≤105.
Каждая из последующих n n n строк задают операцию одного из следующих двух типов:

    Insert {\tt Insert} Insert x {\tt x} x, где 0≤x≤109 0 \le x \le 10^9 0≤x≤109
        — целое число;
    ExtractMax {\tt ExtractMax} ExtractMax.

Первая операция добавляет число x x x в очередь с приоритетами, вторая — извлекает
максимальное число и выводит его.

"""

def insert_x(x):
    global len_heap
    global heap
    heap.append(x)
    len_heap += 1
    if len_heap > 1:
        index_x = len_heap - 1
        index_parent = (index_x - 1) // 2
        while heap[index_x] > heap[index_parent] and index_x != 0:
            heap[index_x], heap[index_parent] = heap[index_parent], heap[index_x]
            index_x = index_parent
            index_parent = (index_x - 1) // 2


def ExtractMax():
    global len_heap
    global heap
    if len_heap > 0:
        print(heap[0])
        len_heap -= 1
        last_list = heap.pop()
        if len_heap > 0:
            heap[0] = last_list
            index_x = 0
            index_ch_max = 1
            while index_ch_max < len_heap:
                if index_ch_max + 1 < len_heap:
                    if heap[index_ch_max] < heap[index_ch_max + 1]:
                        index_ch_max += 1
                if heap[index_x] < heap[index_ch_max]:
                    heap[index_x], heap[index_ch_max] = heap[index_ch_max], heap[index_x]
                    index_x =index_ch_max
                    index_ch_max = index_x * 2 + 1
                else:
                    break


heap = []
len_heap = 0
N = int(input())

for _ in range(N):
    comanda = input().split()
    if comanda[0] == 'Insert':
        insert_x((int(comanda[1])))
    elif comanda[0] == 'ExtractMax':
        ExtractMax()



