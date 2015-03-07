def accept_varargs(arg1, *args, kwarg1=None, **kwargs):
    print('arg1 = ', arg1)
    print('kwarg1 = ', kwarg1)
    print('args = ', args)
    print('kwargs = ', kwargs)


accept_varargs(0)
accept_varargs(0, 1)
accept_varargs(0, 1, 2, kwarg1=3, what_do_to='kill yourself', will_they_block_github='for sure')
