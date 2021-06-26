################################
# Question 1
################################
def check_docstring():
    """
    This closure is used to check if the docstring has more than 50 characters.
    """
    num_chars = 50

    def inner_doc(fn):
        if len(" ".join(fn.__doc__.split())) >= num_chars:
            return True
        else:
            return False

    return inner_doc


################################
# Question 2
################################
def outer_fibo():

    ''' 
    This function gives the next number 
    in the fibonacci series.
    '''

    n = 0
    def nextFibonacci(a,b):
        nonlocal n
        if b == 0:
            b = 1
            return a+b
        else:
            n = a+b
            a = b
            b = n
        return n
    return nextFibonacci



################################
# Question 3
################################
g_counters = dict()


def global_counter(fn):
    """
    A closure to keep a count of how many times the function is called using a global dictionary.
    """
    cntr = 0 

    def inner(*args, **kwargs):
        nonlocal cntr
        cntr = cntr + 1
        g_counters[fn.__name__] = cntr  # counters is global
        return fn(*args, **kwargs)

    return inner


################################
# Question 4
################################
def param_counter(fn, counters):
    """
    A closure to keep a count of the number of times a function is called by passing a dictionary as an argument.
    """
    cntr = 0

    def inner(*args, **kwargs):
        nonlocal cntr
        cntr = cntr + 1
        counters[fn.__name__] = cntr
        return fn(*args, **kwargs)

    return inner
