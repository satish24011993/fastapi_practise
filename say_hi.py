from typing import Optional, Union

def say_hi_o(name: Optional[str]=None):
    if name is not None:
        print(f'Hey {name}!')
    else:
        print('Hello World')


say_hi_o('Satish')

# without optional
# def say_hi_w(name: str | None = None):
#     if name is not None:
#         print(f'Hey {name}!')
#     else:
#         print('Hello World')


# say_hi_w('Satish')

# Above code gives error
# TypeError: unsupported operand type(s) for |: 'type' and 'NoneType'

def say_hi_wo(name: Optional[str]):
    print(f'Hey {name}!')

say_hi_wo('Satish Kurakula')

def say_hi_w(name: Union[str, None] = None):
    print(f'Hey {name}!')

say_hi_w('S')

# Above code is giving error

