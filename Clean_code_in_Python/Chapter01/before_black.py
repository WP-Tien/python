"""
    Clean Code in Python - Chapter 1: Introduction, Tools, and Formatting

    > Black:
        A code that is compliant with PEP-8, but that still can be modified by back

    Run::
        black -l 79 before_black.py
        
    -l là viết tắt của --line-length
    79 = độ dài tối đa của một dòng code
    
    => Nghĩa là:
    Nếu một dòng code dài hơn 79 ký tự (79 là con số chuẩn theo PEP8(style guide của Python))

    Black sẽ tự động xuống dòng/tách dòng  

To see the difference
"""


def my_function(name):
    """
    >>> my_function('black')
    'received Black'
    """
    return "received {0}".format(name.title())
