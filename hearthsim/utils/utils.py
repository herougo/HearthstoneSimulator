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
        if hasattr(v, 'copy'):
            kwargs[k] = v.copy()
    return type(val)(**kwargs)