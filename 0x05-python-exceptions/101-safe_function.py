#!/usr/bin/python3
def safe_function(fct, *args):
    try:
        result = fct(*args)
        return result
    except (ZeroDivisionError, IndexError) as error:
        import sys
        print("Exception: {}".format(error), file=sys.stderr)
        return None
