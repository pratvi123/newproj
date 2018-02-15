# -*- coding: utf-8 -*-
"""
Created on Wed Feb 08 12:40:14 2017

@author: DELL
"""

def my_decorator(some_function):
    def wrapper():
        num = 10
        if num == 10:
            print("Yes!")
        else:
            print("No!")
        some_function()
        print("Something is happening after some_function() is called.")

    return wrapper


def just_some_function():
    print("Wheee!")

just_some_function = my_decorator(just_some_function)

just_some_function()
