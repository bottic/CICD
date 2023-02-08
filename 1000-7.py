from time import sleep
x = 1000

while x > 0:
    print(x, ' - 7')
    x = x - 7
    sleep(0.01)

#
# DATA = {
#     'omlet': {
#         'яйца, шт': 2,
#         'молоко, л': 0.1,
#         'соль, ч.л.': 0.5,
#     },
#     'pasta': {
#         'макароны, г': 0.3,
#         'сыр, г': 0.05,
#     },
#     'buter': {
#         'хлеб, ломтик': 1,
#         'колбаса, ломтик': 1,
#         'сыр, ломтик': 1,
#         'помидор, ломтик': 1,
#     },
#
# }
#
# context = {}
#
# for x, y in DATA['omlet'].items():
#     context[x] = y*
#
# print(context)