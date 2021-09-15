# 构造堆类
import random


class Heap():
    def __init__(self,length):
        self.heap = [0] * (length+1)
        self.size = 0

    def push(self,val):
        if self.size == len(self.heap)-1:
            return False
        self.size += 1
        self.heap[self.size] =val
        self.shiftup(self.size)

    def shiftup(self,n):
        val = self.heap[n]
        while n>>1 > 0:
            parent = n >> 1
            if self.heap[parent] > val:
                self.heap[n] = self.heap[parent]
                n = parent
            else:
                break
        self.heap[n] = val

    def peek(self):
        assert self.size>0,f'size = 0 '
        return self.heap[1]

    def pop(self):
        val = self.peek()
        self.shiftdown(1)
        return val

    def shiftdown(self,n):
        self.heap[1] = self.heap[self.size]
        self.heap[self.size] = 0
        val = self.heap[n]
        self.size -= 1
        while n<<1 <self.size:
            child = n<<1
            if child+1 != self.size:
                child = child if self.heap[child] < self.heap[child+1] else child+1
            if self.heap[child] < val:
                self.heap[n] = self.heap[child]
                n = child
            else:
                break
        self.heap[n] = val

    def heapSort(self,nums):
        for i in range(len(nums)):
            self.push(nums[i])
        for i in range(len(nums)):
            nums[i] = self.pop()


if __name__ =='__main__':
    nums = [*range(10)]
    random.shuffle(nums)
    print(f'排序前：f{nums}')
    heap = Heap(len(nums))
    heap.heapSort(nums)
    print(f'排序后：f{nums}')