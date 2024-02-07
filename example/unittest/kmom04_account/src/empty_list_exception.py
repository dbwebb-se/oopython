#!/usr/bin/env python3

class EmptyAccountListException(Exception):
    """ Exception raised when get accounts and owner has no accounts """
    pass