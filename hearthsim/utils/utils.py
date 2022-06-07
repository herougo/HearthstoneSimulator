def maybe_wrap_as_tuple(x):
    if isinstance(x, tuple):
        return x
    else:
        return (x,)

def deep_copy(val):
    kwargs = {
        k: v for k, v in vars(val).items()
        if k != 'memory' and (not k.startswith('_'))
    }
    for k, v in kwargs.items():
        if hasattr(v, 'copy'):
            kwargs[k] = v.copy()
    return type(val)(**kwargs)