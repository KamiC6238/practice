# practice

'''
如果使用defaultdict的话，就可以避免KeyError,并且可以简化代码量。
defaultdict(<class 'int'>, {'bobby1': 2, 'bobby2': 3, 'bobby3': 1})
'''

from collections import defaultdict

users = ['bobby','bobby1','bobby2','bobby1','bobby','bobby']

statistics = defaultdict(int)
for user in users:
    statistics[user] += 1

print(statistics)

'''
下面是不适用defaultdict的情况下来统计每个元素出现的次数
由于直接使用statistics[user]可能会出现KeyError的异常，
所以这里使用字典的get方法，如果字典里没有这个key，那么就会返回None
第一次遍历到的时候，字典里面是没有这个key的,所以直接让statistics[user] = 1
第二次遍历开始就不断+1

'''
users = ['bobby','bobby1','bobby2','bobby1','bobby','bobby']

statistics = {}
for user in users:
    statistics[user] = statistics.get(user,0) + 1
print(statistics)
