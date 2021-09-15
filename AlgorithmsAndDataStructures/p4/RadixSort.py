import random


def radixSort(nums):
    """
    实现基数排序
    :param nums: 目标列表
    :return:
    """
    if nums ==None and len(nums)<2:
        return
    radixsort(nums,0,len(nums)-1,maxbits(nums))

def maxbits(nums):
    """
    计算数组的位数，决定使用几轮入桶出桶 大循环
    :param nums:
    :return:
    """
    max_num = max(nums)
    return len(str(max_num))

def getDigit(num,d):
    """
    获取num的第-1-d位的数字
    :param num:
    :param d:
    :return:
    """
    return  int(str(num)[-1-d]) if len(str(num)) > d else 0




def radixsort(nums,l,r,digit):
    # 多少进制的排序
    radix = 10

    for d in range(digit):
        # 定义一个计数的桶，记录某一位数字出现的次数
        count = [0]*radix
        for num in nums[l:r+1]:
            j = getDigit(num,d)
            count[j] += 1
        # 累加计数桶，得到每个数在每一轮的位置
        for i in range(1,radix):
            count[i] += count[i-1]
        # 从每个计数桶中出来 放入一个临时数组
        bucket = [0] * (r-l+1)
        for i in range(len(nums)):
            j = getDigit(nums[i],d)
            bucket[count[j]-1] = nums[i]
            count[j] -= 1
        # 将桶中的数放入nums
        nums[l:r+1] = bucket



if __name__ == '__main__':
    nums = [*range(90,120)][::5]
    random.shuffle(nums)
    print(f'排序前：{nums}')
    radixSort(nums)
    print(f'排序后：{nums}')
