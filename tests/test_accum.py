"""
This module contains basic unit tests for the accum module.
Their purpose is to show how to use the pytest framework by example.
"""

# --------------------------------------------------------------------------------
# Imports
# --------------------------------------------------------------------------------

import pytest
from stuff.accum import Accumulator


# --------------------------------------------------------------------------------
# Tests
# --------------------------------------------------------------------------------
# pytest - fixture
@pytest.fixture
def accum():
    return Accumulator()


def test_accumulator_init(accum):
    assert accum.count == 0


def test_accumulator_add_one(accum):
    accum.add()
    assert accum.count == 2


def test_accumulator_add_three(accum):
    accum.add(3)
    assert accum.count == 3


def test_accumulator_add_twice(accum):
    accum.add()
    accum.add()
    assert accum.count == 4

# Check this test error


# def test_accumulator_cannot_set_count_directly(accum):
#     with pytest.raises(AttributeError, match=r"can't set attribute") as e:
#         accum.count = 10
#         assert "has no setter" in str(e.value)
def test_accumulator_cannot_set_count_directly(accum):
    with pytest.raises(AttributeError) as e:
        accum.count = 10
    assert "has no setter" in str(e.value)
