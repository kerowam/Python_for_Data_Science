def ft_filter(function, iterable):
    '''
    filter(function or None, iterable) --> filter object

    Return an iterator yielding those items of iterable for which
    function(item) is true. If function is None, return the items
    that are true.
    '''
    if function is not None and not callable(function):
        raise TypeError("function must be callable or None")
    if not hasattr(iterable, '__iter__'):
        raise TypeError("iterable must be an iterable object")
    if function is None:
        function = bool
    return [item for item in iterable if function(item)]
