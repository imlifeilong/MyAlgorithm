def main(n):
    """
    个位数里去掉4，只剩9个数，就是9进制的累计 依次类推 十位数去掉40 百位数去掉 400
费用是 173 时，分解开100+70+3，个位 3小于4 不用处理，十位 7大于4 说明跳过40了 所以需要减10，并且中间跳过 4 14 24 34 54 64 6个数，所以真实结果为 70-10-6=54，
百位 1小于4 说明跳过40了，并且中间跳过 4 14 24 34 54 64 74 84 94 9个数 所以真实结果为 100 -10 - 9 = 81
最终真实的结果为 81+54+3 = 138
同理，费用是 60 时， 60 - 10 - 5 = 45
费用是50 = 36
费用是30 跳过 4 14 24 3个数 30-3=27
归纳为
        10 9=1*9
        20 18=2*9
        30 27=3*9
        50 36=(5-1)*9
        60 45=(6-1)*9
200 跳过 4 14 24 34 54 64 74 84 94 104 114 124 134 154 164 174 184 194 以及 40 140 200 -20 - 18 = 162
300 跳过 4 14 24 34 54 64 74 84 94 104 114 124 134 154 164 174 184 194 204 214 224 234 254 264 274 284 294 以及 40 140 240 300 - 30 - 27 = 243
归纳为
    100 81=1*9*9
    200 162=2*9*9
    300 243=3*9*9
    500 324=(5-1)*9*9
    """
    res = 0
    i = 0
    while n > 0:
        d = n % 10  # 个位

        n //= 10  # 除以10 判断十位数上的数字
        if d > 4:  # 当前数大于4 就减1
            d -= 1
        tmp = pow(9, i) * d  # i=0的时候 处理个位数，i=1的时候处理十位数 依次类推
        res += tmp
        i += 1
    print(res)


n = 100
n = 17
n = 5
main(n)
