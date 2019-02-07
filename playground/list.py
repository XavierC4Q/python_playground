y = lambda a: a * 200
z = lambda str: str * 4

times_two_hundred = [y(el) for el in range(15)]
long_names = [z(i) for i in 'avalanche']

zipper = zip(times_two_hundred, long_names)

abba = list(zipper)

a = [13, 4, 55, 6, 7, 9, 4, [5, 6, 7]]
b = [13, 4, 55, 6, 7, 9, 4, [5, 6, 7]]

print(a == b)



