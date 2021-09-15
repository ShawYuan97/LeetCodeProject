# 采用随机pivot快排
import random


def quick_sort(nums,l,r):
    """
    快排的函数
    :param nums:目标数组
    :param l: 数组左边界
    :param r: 数组右边界
    :return:
    """
    if l<r:
        pivot = l + int(random.random() * (r-l+1)) # 从数组中获取一个随机索引
        # 交换pivot和最后一个位置的值
        nums[pivot],nums[r] = nums[r],nums[pivot]
        # 根据最后一个值进行划分
        left,right = partition(nums,l,r)
        # 继续快排左右分区
        quick_sort(nums,l,left-1)
        quick_sort(nums,right+1,r)

def partition(nums,l,r):
    """
    根据最后一个值进行划分
    :param nums:
    :param l:
    :param r:
    :return:
    """
    # 利用三个指针来进行小于区间、等于区间、大于区间的划分
    # 三个指针分别指向 l r-1 以及 从l开始向右运动的指针
    left = l - 1 # 小于区间右边界
    right = r  # 大于区间左边界
    pivot = nums[r] # 哨兵 用来划分数组的值
    # 将p位置和最后一个位置值进行比较
    while l < right:
        if nums[l] < pivot:
            # 如果小于哨兵，小于区间右移，交换left和l,表示左边都是小于区间了，l右移
            left += 1
            nums[left],nums[l] = nums[l], nums[left]
            l += 1
        elif nums[l] > pivot:
            # 大于区间左移
            right -= 1
            # 如果大于哨兵，交换right和l,表示右边都是大于区间
            nums[l],nums[right] = nums[right],nums[l]
        else:
            l += 1
    nums[right],nums[r] = nums[r],nums[right]
    return left+1,right # 真相了，left+1才是等于区间第一个位置，right是等于区间最后一个位置

if __name__ == '__main__':
    nums = [*range(1,20)]
    random.shuffle(nums)
    print(f'排序前：\n {nums}')
    quick_sort(nums,0,len(nums)-1)
    print(f'排序后：\n {nums}')