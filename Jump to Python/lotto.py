# import random
# import time

# def random_pop(data):
#     number = random.randint(0, len(data)-1)
#     return data.pop(number)

# data = list(range(1, 46))
# i = 1
# while i < 7:
#     i += 1
#     time.sleep(3)
#     print(random_pop(data))

# import random
# import time

# def lotto():
#     group = list(range(1, 46))
#     i = 0
#     while i < 6:
#         i += 1
#         n = random.choice(group)
#         group.remove(n)
#         print(n, end=' ')
#         time.sleep(1)

# lotto()

import random

result = []
while len(result) < 6:
    num = random.randint(1, 45)
    if num not in result:
        result.append(num)
print(result)