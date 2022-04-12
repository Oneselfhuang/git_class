'''
回文是指一段数字或者文本，正着读和倒着读都是相同的，例如2002，110011都是回文数字。给定一个数字num，请编写一个函数，判断它是不是一个回文数字。

【示例】
输入：1221
输出：True
解释：1221倒过来依旧是1221，因此它是回文数字
'''

def solution(num: int)-> bool:

    if num == int(str(num)[::-1]):
        print(str(num)[::-1])
        return True
    else:
        return False



assert solution(1221) is True
assert solution(123322) is False
assert solution(2022) is False