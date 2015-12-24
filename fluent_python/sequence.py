# -*- coding: utf-8 -*-
"""
Chapter 2: Ann Array of Sequences
"""
import array
import bisect


class Seq(object):
    """
    Sequence with multidimensional slice
    """

    def __init__(self, value=None):
        self.value = value or []

    def __getitem__(self, index):
        if not isinstance(index, slice):
            s = slice(*index)
        else:
            s = index
        return self.value[s]

    def __add__(self, other):
        print 'call to __add__'
        return self.value + other.value

    def __str__(self):
        return '{} - {}'.format(self.__class__, self.value)


class SeqWithIAdd(Seq):

    def __iadd__(self, other):
        print 'call to __iadd__'
        self.value.extend(other.value)
        return self  # this will be assigned to the result


def multidimensional_seq():
    s = Seq(range(10))
    print 'slice:', s[1, 3]
    slice_obj = slice(1, 3)
    print 'slice from obj:', s[slice_obj]
    print '=' * 50


def assigning_to_slices():
    l = range(10)
    print 'l:', l
    l[2:5] = [20, 30]
    print 'l after l[2:5]=[20, 30]:', l
    del l[5:7]
    print 'del l[5:7]:', l
    print '=' * 50


def assign_add():
    a = Seq(range(10))
    b = Seq(range(10, 20))
    print id(a), a
    a += b
    print id(a), a

    a = SeqWithIAdd(range(10))
    print id(a), a
    a += b
    print id(a), a
    print '=' * 50


def list_append_in_tuple():
    """Argumented operation(+=, *=, etc.) is not atomic
    """
    t = (1, 2, [3, 4])
    print 't before:', t
    try:
        t[2] += [5, 6]
    except Exception as e:
        print 'Exception Raised:', e
    print 't after:', t

    t[2].append(7)
    t[2].extend([8, 9])
    print 'change with extend and append:', t
    print '=' * 50


def bisect_usage():
    breakpoints = [60, 70, 80, 90]
    grades = 'FDCBA'

    def grade(score):
        return grades[bisect.bisect(breakpoints, score)]
    print [grade(score) for score in [33, 60, 69, 99, 88, 77]]


def main():
    multidimensional_seq()
    assigning_to_slices()
    assign_add()
    list_append_in_tuple()
    bisect_usage()


if __name__ == "__main__":
    main()
