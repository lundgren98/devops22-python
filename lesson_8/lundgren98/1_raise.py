
def check_float(f: float):
    if not isinstance(f, float):
        raise TypeError(f'{f} is not a float!')

check_float(1)
