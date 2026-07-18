str = "Hello World"
print(str.replace("World", "Python"))
print(str)

str = "hello everyone"
print(' '.join(str))

str = "hello_everyone"
print(str.split("_"))

str = "hello everyone"
print(str.index("e"))

str = "hello everyone"
print(str.count("e"))

str = "hello everyone"
print(str[0], str[1], str[2])

list_ = [1, 2, 3, 4, 5, "hello", 3.14, True, [1, 2, [11, "world"], 3]]
print(list_[0], list_[1], list_[5], list_[8], list_[8][2][1][2])

list_ = [1, 2, 3, 4, 5]
list_[0] = 10
print(list_)

list_ = [1, 2, 3, 4, 5]
list_.append(6)
print(list_)

list_ = [1, 2, 3, 4, 5]
list_.extend([6, 7, 8])
print(list_)

list_ = [1, 2, 3, 4, 5]
list_.append("python")
print(list_)
list_.extend("python")
print(list_)

list_ = [1, 2, 3, 4, 5]
list_.remove(3)
print(list_)

list_ = [1, 2, 3, 4, 5]
list_.pop(2)
print(list_)
list_.pop()
print(list_)
