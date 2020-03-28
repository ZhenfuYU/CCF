# 商业转载请联系作者获得授权，非商业转载请注明出处。
# For commercial use, please contact the author for authorization. For non-commercial use, please indicate the source.
# 协议(License)：署名-非商业性使用-相同方式共享 4.0 国际 (CC BY-NC-SA 4.0)
# 作者(Author)：Yuzhenfu
# 链接(URL)：https://yuzhenfu.cn/index.php/2019/02/01/ccf-201312-1-%e5%87%ba%e7%8e%b0%e6%ac%a1%e6%95%b0%e6%9c%80%e5%a4%9a%e7%9a%84%e6%95%b0/
# 来源(Source)：Recruited

# 数值输入
n = int(input())
# 定义字符串数组
num = []
for i in range(10001):
    # 将字符串数组转换成数值数组
    num += [0]
# 将输入数值去空格存储到s字符串中
s = input().split()
for i in range(n):
    # 类型转换
    s[i] = int(s[i])
    # 输入数值对应下标的值+1
    num[s[i]] += 1
# 前0表示出现次数  后0表示数组下标
max_num = [0, 0]
for i in range(10001):
    #   >避免了次数相同的比较
    if num[i] > max_num[0]:
        # 将次数最大的最小数存入
        max_num[0], max_num[1] = num[i], i
print(max_num[1])