import atexit


def memory_usage():
    import resource
    return resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024


def print_memory_usage_at_exit():
    print('>>>>>>> Memory used: {} KB'.format(memory_usage()))

atexit.register(print_memory_usage_at_exit)
