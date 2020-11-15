'''
Author: your name
Date: 2020-11-14 17:20:05
LastEditTime: 2020-11-15 12:03:16
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \VSwork\sort\sort_compare.py
'''
import random


def InsertSort(list):
    """插入排序"""
    count = 0
    # 第一层for表示循环插入的遍数
    for i in range(1, len(list)):
        # 设置当前需要插入的元素
        current = list[i]
        # 与当前元素比较的比较元素
        pre_index = i - 1
        while pre_index >= 0 and list[pre_index] > current:
            # 当比较元素大于当前元素则把比较元素后移
            list[pre_index + 1] = list[pre_index]
            # 往前选择下一个比较元素
            pre_index -= 1
            count += 1
        # 当比较元素小于当前元素，则将当前元素插入在其后面
        list[pre_index + 1] = current
    return count


def BubbleSort(list):
    """冒泡排序"""
    count = 0
    n = len(list)
    for j in range(0, n - 1):
        for i in range(0, n - 1):  # i每循环一次都能把最大的值以此从右边排起
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]
            count += 1
    return count


def SelectSort(list):
    """选择排序"""
    count = 0
    # 第一层for表示循环选择的遍数
    for i in range(len(list) - 1):
        # 将起始元素设为最小元素
        min_index = i
        # 第二层for表示最小元素和后面的元素逐个比较
        for j in range(i + 1, len(list)):
            if list[j] < list[min_index]:
                # 如果当前元素比最小元素小，则把当前元素角标记为最小元素角标
                min_index = j
                count += 1
        # 查找一遍后将最小元素与起始元素互换
        list[min_index], list[i] = list[i], list[min_index]
    return count


def QuickSort(list, left, right):
    """快速排序"""
    count = 0
    if left >= right: return  #递归终止条件
    i, j = left, right
    pivot = list[i]  #拿出一个比较值
    while i < j:
        while i < j and list[j] >= pivot:
            j -= 1
            count += 1
        if i < j:
            list[i] = list[j]
            i += 1
            count += 1
        while i < j and list[i] <= pivot:
            i += 1
        if i < j:
            list[j] = list[i]
            j -= 1
            count += 1
    list[i] = pivot
    QuickSort(list, left, i - 1)
    QuickSort(list, i + 1, right)
    return count


def ShellSort(list):
    """希尔排序"""
    count = 0
    # 取整计算增量（间隔）值
    gap = len(list) // 2
    while gap > 0:
        # 从增量值开始遍历比较
        for i in range(gap, len(list)):
            j = i
            current = list[i]
            # 元素与他同列的前面的每个元素比较，如果比前面的小则互换
            while j - gap >= 0 and current < list[j - gap]:
                list[j] = list[j - gap]
                j -= gap
                count += 1
            list[j] = current
        # 缩小增量（间隔）值
        gap //= 2
    return count


def HeapSort(list):
    """堆排序"""
    count = 0

    def heapify(list, n, i):
        nonlocal count
        largest = i
        l = 2 * i + 1  # left = 2*i + 1
        r = 2 * i + 2  # right = 2*i + 2
        if l < n and list[i] < list[l]:
            largest = l
            count += 1
        if r < n and list[largest] < list[r]:
            largest = r
            count += 1
        if largest != i:  #largest记录了 i,l,r 三个数里面最大的
            count += 1
            list[i], list[largest] = list[largest], list[i]  # 交换
            heapify(list, n, largest)

    n = len(list)
    # Build a maxheap.
    for i in range(n, -1, -1):
        heapify(list, n, i)
    # 一个个交换元素
    for i in range(n - 1, 0, -1):
        list[i], list[0] = list[0], list[i]  # 交换
        heapify(list, i, 0)
    return count


if __name__ == '__main__':
    list1, list2 = [], []
    for i in range(100):
        list1.append(random.randint(0, 100))
    print("数据量为100的排序比较")
    print("插入排序比较次数:", InsertSort(list1.copy()))
    print("冒泡排序比较次数:", BubbleSort(list1.copy()))
    print("选择排序比较次数:", SelectSort(list1.copy()))
    print("快速排序比较次数:", QuickSort(list1.copy(), 0, len(list1) - 1))
    print("希尔排序比较次数:", ShellSort(list1.copy()))
    print("堆排序比较次数:", HeapSort(list1.copy()))

    for i in range(10000):
        list2.append(random.randint(0, 10000))
    print("数据量为10000的排序比较")
    print("插入排序比较次数:", InsertSort(list2.copy()))
    print("冒泡排序比较次数:", BubbleSort(list2.copy()))
    print("选择排序比较次数:", SelectSort(list2.copy()))
    print("快速排序比较次数:", QuickSort(list2.copy(), 0, len(list2) - 1))
    print("希尔排序比较次数:", ShellSort(list2.copy()))
    print("堆排序比较次数:", HeapSort(list2.copy()))
