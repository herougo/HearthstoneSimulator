def maybe_wrap_as_tuple(x):
    if isinstance(x, tuple):
        return x
    else:
        return (x,)

def deep_copy(val, copied_subclasses):
    for subclass in copied_subclasses:
        if isinstance(val, subclass):
            kwargs = vars(val)
            for k, v in kwargs.items():
                if k == 'memory':
                    continue
                kwargs[k] = deep_copy(v, copied_subclasses)
            return type(val)(**kwargs)

    return val