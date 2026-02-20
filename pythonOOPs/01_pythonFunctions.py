def my_custom_decorator(func):
    def wrapper(*args, **kwargs):
        
        # fetch the positonal argument 
        # assign default value
        args_list = list(args)
        if len(args) < 2:
            args_list = args_list + [1, 2]
        first_num = args_list[0]
        second_num = args_list[1]

        # validate the positional arguments
        if not (isinstance(first_num, int) and isinstance(second_num, int)):
            raise ValueError("One of the input is not an integer")
        
        # covert to tuple
        args = tuple([first_num, second_num])

        # fetch and assign the default value of keywords argument
        kwargs.setdefault("d", 0)
        kwargs.setdefault("e", 0) 
        first_kw = kwargs["d"]
        second_kw = kwargs["e"]

        # validate keyword arguments
        if not (isinstance(first_kw, int) and isinstance(second_kw, int)):
            raise ValueError("One of the input keyword is not an integer")

        # return function
        return func(*args, **kwargs)
    return wrapper

@my_custom_decorator
def addition(a, b, **kwargs):
    """
    add two position argument and two key words argument
    sum = addition(2, 3, d=1, e=1)
    sum = addiiton(2, d=1)
    sum = addition()
    """ 
    d = kwargs["d"]
    e = kwargs["e"]
    sum = a + b + d + e
    return sum

print(addition(2, e=4))
