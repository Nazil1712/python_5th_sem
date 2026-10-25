def variable_length_func(*args):
    print('#'.join(map(str, args)))


variable_length_func(1, 2, 3, 4, 5)
variable_length_func('apple', 'banana', 'orange', 'grape')
