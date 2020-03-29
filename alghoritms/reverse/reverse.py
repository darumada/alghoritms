def reverse(iterable):
    start = 0
    end = len(iterable) - 1

    while start < end:
        iterable[start], iterable[end] = iterable[end], iterable[start]
        start += 1
        end -= 1


def reverse_rec(iterable):
    def _reverse(start, end):
        if start > end:
            return

        iterable[start], iterable[end] = iterable[end], iterable[start]

        _reverse(start + 1, end - 1)

    _reverse(0, len(iterable) - 1)


arr = [1, 2, 3]

reverse(arr)
print(arr)
