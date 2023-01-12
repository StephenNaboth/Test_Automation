from hypothesis import given, strategies as st
'''
from hypothesis import given, strategies is an import statement in Python that imports the given and strategies modules from the Hypothesis library.

hypothesis is a Python library for generating test inputs, it can be used to write test case that can handle edge cases, and it's often used as a complement to pytest testing framework.

The given function is a decorator that is used to declare a test function and specify the strategies for generating the inputs to that test. given takes one or more arguments, where each argument is a strategy for generating an input for the test.
'''


@given(st.integers(), st.integers())
def test_ints_are_commutative(x, y):
    assert x + y == y + x


@given(x=st.integers(), y=st.integers())
def test_ints_cancel(x, y):
    assert (x + y) - y == x


@given(st.lists(st.integers()))
def test_reversing_twice_gives_same_list(xs):
    # This will generate lists of arbitrary length (usually between 0 and
    # 100 elements) whose elements are integers.
    ys = list(xs)
    ys.reverse()
    ys.reverse()
    assert xs == ys


@given(st.tuples(st.booleans(), st.text()))
def test_look_tuples_work_too(t):
    # A tuple is generated as the one you provided, with the corresponding
    # types in those positions.
    assert len(t) == 2
    assert isinstance(t[0], bool)
    assert isinstance(t[1], str)


'''
In this example, test_example is a test function that takes two arguments: x and y. The @given decorator is used to specify that the test should be run with two strategies, strategies.integers() which will generate random integer values and strategies.text() which will generate random text values as inputs.

The strategies module contains a number of pre-defined strategies for generating various types of input data, such as integers, lists, dictionaries, etc. It's also possible to create custom strategies if the pre-defined strategies don't suit your needs.

hypothesis library provides a way to write test case that can handle edge cases and random values, it helps to find bugs in your code that you wouldn't think to test for manually.
'''
