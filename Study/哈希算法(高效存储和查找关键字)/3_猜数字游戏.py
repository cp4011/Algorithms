"""LeetCode 299
你正在和你的朋友玩 猜数字（Bulls and Cows）游戏：你写下一个数字让你的朋友猜。每次他猜测后，你给他一个提示，告诉他有
多少位数字和确切位置都猜对了（称为“Bulls”, 公牛），有多少位数字猜对了但是位置不对（称为“Cows”, 奶牛）。你的朋友将会
根据提示继续猜，直到猜出秘密数字。
请写出一个根据秘密数字和朋友的猜测数返回提示的函数，用 A 表示公牛，用 B 表示奶牛。
请注意秘密数字和朋友的猜测数都可能含有重复数字。
示例 1:
输入: secret = "1807", guess = "7810"
输出: "1A3B"
解释: 1 公牛和 3 奶牛。公牛是 8，奶牛是 0, 1 和 7。
示例 2:
输入: secret = "1123", guess = "0111"
输出: "1A1B"
解释: 朋友猜测数中的第一个 1 是公牛，第二个或第三个 1 可被视为奶牛【最终B是由该数在秘密数字中和在猜测数字中更小的那方决定】
说明: 你可以假设秘密数字和朋友的猜测数都只包含数字，并且它们的长度永远相等。
"""


def getHint(secret, guess):
    """
    :type secret: str
    :type guess: str
    :rtype: str
    """
    secret_dict = {}
    guess_dict = {}
    A = 0
    B = 0
    for i in range(len(secret)):
        if secret[i] == guess[i]:                               # A的数量
           A += 1
        else:                                                   # 非公牛的记录在字典中
            secret_dict[secret[i]] = secret_dict.get(secret[i], 0) + 1
            guess_dict[guess[i]] = guess_dict.get(guess[i], 0) + 1
    for digit in secret_dict:
        if digit in guess_dict:
            B += min(secret_dict[digit], guess_dict[digit])     # B的数量是由该数在秘密数字中和在猜测数字中更小的那方决定
    return str(A)+"A"+str(B)+"B"                                # 输出


# test
secret = input()
guess = input()
print(getHint(secret, guess))
