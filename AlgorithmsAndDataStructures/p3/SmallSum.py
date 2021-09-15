# 使用归并排序的方法实现求小和
import random


def SamllSum(nums):
    """
    求小和
    :param nums: 目标数组
    :return: 小和
    """
    if len(nums)<2 and nums==None:
        return 0
    return process(nums,0,len(nums)-1)

def process(nums,l,r):
    """
    处理数组，分治以及返回小和
    :param nums: 目标数组
    :param l: 左边界
    :param r: 右边界
    :return: 左边子数组+右边子数组+整个数组的小和
    """
    # 归并排序的分治过程
    # 如果分治到只有两个数，返回零
    if l==r:
        return 0
    # 否则从中间开始划分
    # note:>>右移操作的优先级较低 应该将(r-l)>>1 括起来
    mid = l + ((r-l)>>1)
    # 求出左右两边的小和
    sum_left = process(nums,l,mid)
    sum_right = process(nums,mid+1,r)
    # 返回左右两边小和以及归并后整个数组的小和
    return sum_left+sum_right+merge(nums,l,mid,r)

def merge(nums, l, mid, r):
    """
    归并数组
    :param nums: 目标数组
    :param l: 左边界
    :param mid: 数组中间索引
    :param r: 数组右边界
    :return:
    """
    # 记录小和
    res = 0
    # 辅助数组,用来让数组有序
    help = []
    # 开始从左往右比较两个子数组
    i = l
    j = mid+1
    while i <= mid and j <=r:
        if nums[i] < nums[j]:
            res += nums[i] * (r-j+1)
            help.append( nums[i])
            i += 1
        else:
            help.append( nums[j])
            j += 1
    while i < mid+1:
        help.append( nums[i])
        i+=1
    while j < r+1:
        help.append( nums[j])
        j += 1
    nums[l:r+1] = help
    return res

# 暂未完成对数器
if __name__ == '__main__':
    nums = [*range(10)]
    random.shuffle(nums)
    print(f'nums:{nums}')
    sum = SamllSum(nums)
    print(f'smallSum:{sum}')

