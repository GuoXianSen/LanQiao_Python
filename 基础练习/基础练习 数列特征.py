# n = int(input())
# a = list(map(int, input().split()))
# print(max(a))
# print(min(a))
# print(sum(a))
#
# # python内置的一些函数
# max()
# min()
# sum()
import requests
import re

# url = 'https://www.douyu.com/g_yz'
url = "https://www.baidu.com"
# url = "https://www.pronhub.com"
result = requests.get(url).text
print(result)

# reg = "window\.\$DATA =(.*?);.*?var pageType = 'list2';"
# data = re.findall(reg, result, re.S)
# print(data)
