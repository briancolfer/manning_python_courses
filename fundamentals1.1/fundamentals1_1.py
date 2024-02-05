print("strings")
a = "a"
b = a
print(f"a: {a}, id(a) {id(a)} b: {b} id(b) {id(b)}")
b = "b"
print(f"a: {a}, id(a) {id(a)} b: {b} id(b) {id(b)}")
print("strings are immutable, so they are not the same object")

print("integers")
a = 1
b = a
print(f"a: {a}, id(a) {id(a)} b: {b} id(b) {id(b)}")
b = 2
print(f"a: {a}, id(a) {id(a)} b: {b} id(b) {id(b)}")
print("integers are immutable, so they are not the same object")

print("floats")
a = 1.0
b = a
print(f"a: {a}, id(a) {id(a)} b: {b} id(b) {id(b)}")
b = 2.0
print(f"a: {a}, id(a) {id(a)} b: {b} id(b) {id(b)}")
print("floats are immutable, so they are not the same object")

print("lists")
a = [1, 2, 3]
b = a
print(f"a: {a}, id(a) {id(a)} b: {b} id(b) {id(b)} id(b[0]) {id(b[0])}")
b[0] = 4
print(f"a: {a}, id(a) {id(a)} b: {b} id(b) {id(b)} id(b[0]) {id(b[0])}")
print("lists are mutable, so they are the same object")

print("tuples")
a = (1, 2, 3)
b = a
print(f"a: {a}, id(a) {id(a)} b: {b} id(b) {id(b)} id(b[0]) {id(b[0])} b[2] {id(b[2])} id(b[2]) {id(b[2])}")
b = (4, 2, 3)
print(f"a: {a}, id(a) {id(a)} b: {b} id(b) {id(b)} id(b[0]) {id(b[0])}, b[1] {id(b[1])} id(b[1]) {id(b[1])}")
print("tuples are immutable, so they are not the same object")

print("dictionaries")
a = {"a": 1, "b": 2}
b = a
print(f"a: {a}, id(a) {id(a)} b: {b} id(b) {id(b)} b['a'] {b['a']} id(b['a']) {id(b['a'])}")
b["a"] = 3
print(f"a: {a}, id(a) {id(a)} b: {b} id(b) {id(b)} b['a'] {b['a']} id(b['a']) {id(b['a'])}")
print("dictionaries are mutable so they are the same object and not sorted")

print("sets")
a = {1, 2, 3}
b = a
print(f"a: {a}, id(a) {id(a)} b: {b} id(b) {id(b)}")
b = {4, 2, 3}
print(f"a: {a}, id(a) {id(a)} b: {b} id(b) {id(b)}")
print("sets are mutable, so they are not the same object and sorted")


