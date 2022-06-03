def maybe_wrap_as_tuple(x):
    if isinstance(x, tuple):
        return x
    else:
        return (x,)

def deep_copy(val):
    kwargs = vars(val)
    for k, v in kwargs.items():
        if k == 'memory':
            continue
        kwargs[k] = deep_copy(v)
    return type(val)(**kwargs)