import pytest
import random
import Assignment1
import statistics
import math

# Test q2
def test_functions_q2():
    # Test data
    list1 = [1, 4.2, 11, 2, 30, 23]
    list2 = [1]
    list3 = [1, 2, 3]
    # Randomly generate 100 integers
    list4 = random.sample(range(10**10), 100)

    listlist = [list1, list2, list3, list4]

    for _ in listlist:
        A = Assignment1.question2(_)
        assert A.my_sum() == sum(_)
        assert A.my_mean() == statistics.mean(_)
        assert A.my_median() == statistics.median(_)
        if len(_) > 1:
            assert math.isclose(A.my_stdev(), statistics.stdev(_), rel_tol=1e-9)
        else:
            assert A.my_stdev() == 0
        assert A.my_max() == max(_)


# Test q1
def test_functions_q1():

    assert Assignment1.question1(0, None, None).run() == "Error, input not valid"
    assert Assignment1.question1("hahaha", None, None).run() == "Error, input not valid"
    assert Assignment1.question1(1, 3, 2).run() == ("x = (-3 ± sqrt(1))/2*1", (-1.00,-2.00))
    assert Assignment1.question1(1, 2, 1).run() == ("x = -2/(2*1)", -1.0)
    assert Assignment1.question1(1, 1, 3).run()[0] == "x = (-1 ± i sqrt(11))/2*1" #not check -0.50+1.66i and -0.50-1.66i idk how to write

