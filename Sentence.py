from pprint import pprint
sentence = "This is a common interview question"
dictionary = {letter: sentence.count(letter) for letter in sentence}
# print(dictionary)
# sorted_dictionary = sorted(key=lambda item: item[1], dictionary)
# sorted_dictionary = dictionary.sort(key=lambda item: item[1])

# my = dict(("a"=1), ("b"=2), ("c"=56), ("d"=14), ("e"=13))
# print(my)
# # my2 = sorted(my, key=lambda item: item[1])
# print(sorted(my, key=lambda item: item[1]))


a = dict(a=2)
# print(a)


b = {'a': 2, 'b': 33, 'c': 22, 'd': 12, 'e': 442, 'f': 22, 'g': 32}
# print(b)

c = dict(a=2, b=3, v=4, c=2, x=2, s=2, w=2, q=2)
# print(c)

d = [("a", 2), ("b", 3), ("v", 4), ("c", 2),
     ("x", 2), ("s", 2), ("w", 2), ("s", 2)]
# print(d)
# print()
# print(sorted(d, key=lambda item: item[1]))


# print(sorted(b.items(), key=lambda item: item[0]))

h = {letter: sentence.count(letter) for letter in sentence}
sorted_h = sorted(h.items(), key=lambda item: item[1], reverse=True)
print(h)
pprint(sorted_h, width=10)
