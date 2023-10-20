def ft_filter(f: callable, iterable):
    """
    ft_filter(function or None, iterable) --> filter object

    Return an iterator yielding those items of iterable for which function(item)
    is true. If function is None, return the items that are true.
    """
    return [elem for elem in iterable if f(elem)]
