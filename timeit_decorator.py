def timefn(fn):
    from functools import wraps

    @wraps(fn)
    def measure_time(*args, **kwargs):
        """
        Timeit uses the best available timing function on your system
        Timeit turns off garbage collection
        """
        import timeit

        timeit.template = """
def inner(_it, _timer{init}):
    {setup}
    _t0 = _timer()
    for _i in _it:
        retval = {stmt}
    _t1 = _timer()
    return _t1 - _t0, retval
"""

        t = timeit.Timer(lambda: fn(*args, **kwargs))
        runs = 10
        exec_time, result = t.timeit(number=runs)
        print("@timefn:" + fn.__name__ + " took an average of " + str(exec_time / runs) + " seconds per run for " + str(runs) + " runs.")
        return result
    return measure_time
