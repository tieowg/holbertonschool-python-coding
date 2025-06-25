#!/usr/bin/python3
'''Salam'''


class Square:
    '''Salam'''
    def __init__(self, size):
        self.__size = size
        if not isinstance(size, int):
            print("size must be an integer")
        if size < 0:
            print("size must be >= 0")
