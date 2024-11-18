def strict(func):
    def wrapper(*args, **kwords):
        annotations = func.__annotations__

        for i, (arg, expected_type) in enumerate(annotations.items()):
            if i < len(args):
                if not isinstance(args[i], expected_type):
                    raise TypeError(f"Argument {arg} should be of type {expected_type}, "
                                    f"but got {type(args[i])}.")

        for key, value in kwords.items():
            if key in annotations and not isinstance(value, annotations[key]):
                raise TypeError(f"Argument '{key}' should be of type {annotations[key]}, "
                                f"but got {type(value)}.")

        return func(*args, **kwords)

    return wrapper
