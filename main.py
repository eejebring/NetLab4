def fibonacci(endValue):
    prev_value = 1
    curr_value = 0
    while curr_value < endValue:
        next_value = curr_value + prev_value
        prev_value = curr_value
        curr_value = next_value
        yield curr_value


a = fibonacci(1000000)

while 1 == 1:
    try:
        print(a.__next__())
    except:
        break
