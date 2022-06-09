def generate_class(name, base_class):
    return type(name, (base_class,), {})