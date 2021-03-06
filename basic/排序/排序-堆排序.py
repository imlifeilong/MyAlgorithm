# _*_ coding:UTF-8 _*_
#堆排序：大根堆要求每个节点的值都小于等于父节点的值，小根堆要求每个节点的值大于等于父节点的值
#父节点 list[i]  左节点 list[2i+1] 右节点 list[2i+2]
#大根堆 list[i] >= list[2i+1] && list[i] >= list[2i+2]
#小根堆 list[i] <= list[2i+1] && list[i] <= list[2i+2]
'''
在堆的数据结构中，堆中的最大值总是位于根节点（在优先队列中使用堆的话堆中的最小值位于根节点）。堆中定义以下几种操作：

最大堆调整（Max Heapify）：将堆的末端子节点作调整，使得子节点永远小于父节点
创建最大堆（Build Max Heap）：将堆中的所有数据重新排序
堆排序（HeapSort）：移除位在第一个数据的根节点，并做最大堆调整的递归运算

'''


import random


def MAX_Heapify(heap, HeapSize, root):#在堆中做结构调整使得父节点的值大于子节点

    left = root * 2 + 1
    right = root * 2 + 2
    larger = root #先选择父节点作为最大点
    # print(heap[left], heap[right], heap[larger])
    if left < HeapSize and heap[larger] < heap[left]:
        # 和左节点比较如果左节点大于父节点，将左节点选为最大点
        larger = left
    if right < HeapSize and heap[larger] < heap[right]:
        larger = right
    if larger != root:
        #如果最大点不是父节点，这个时候做对调值操作
        heap[larger], heap[root] = heap[root], heap[larger]
        # 调换完了之后，要比较该节点和他的父节点，直到所有的子节点小于父节点
        MAX_Heapify(heap, HeapSize, larger)

def Build_MAX_Heap(heap):#构造一个堆，将堆中所有数据重新排序
    HeapSize = len(heap)
    for i in range((HeapSize-2)//2, -1, -1):
        # 从后往前获取有子节点的元素（n/2-1到0之间的元素有子节点）
        # print(heap[i])
        MAX_Heapify(heap, HeapSize, i)

def HeapSort(heap):#将根节点取出与最后一位做对调，对前面len-1个节点继续进行对调整过程。
    Build_MAX_Heap(heap)
    for i in range(len(heap)-1,-1,-1):
        # 将根与最后一位元素交换，然后调整堆
        heap[0], heap[i] = heap[i], heap[0]
        MAX_Heapify(heap, i, 0)
    return heap

if __name__ == '__main__':
    a = [23,4,66,23,4,66,43,14,8,32,43,14,8]
    HeapSort(a)
    print(a)
    