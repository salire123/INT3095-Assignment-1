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
