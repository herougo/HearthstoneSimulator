from hearthsim.utils.enums import Tag


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


def matches_tag(desired_tag, actual_tag):
    return ((desired_tag == Tag.ANY.value) or
            actual_tag == Tag.ALL.value or
            (desired_tag == Tag.ALL.value and actual_tag is not None) or
            desired_tag == actual_tag)
