from __init__ import Test, TestCase
# from utesting import Test, TestCase (for real using)
# import asyncio for async testing way

t = Test()

cases1 = [TestCase({"a": 100000}, 100000), TestCase({"a": 200000}, 200000), TestCase({"a": 200000}, 300000)]

@t.mark_test_unit(cases=cases1)
def func1(a):
    n = 0
    for i in range(0, a):
        n += 1
    return n

cases2 = [TestCase({"a": [1, 5, 2, 5]}, [1, 2, 5, 5]), TestCase({"a": [1, 7, 3, 7, 9, 0]}, [0, 1, 3, 7, 7, 9])]

@t.mark_test_unit(cases=cases2)
def func2(a):
    k = 0
    while k < len(a) - 1:
        k = 0
        for j in range(0, len(a)-1):
            if a[j] > a[j+1]:
                a[j] = a[j] + a[j+1]
                a[j+1] = a[j] - a[j+1]
                a[j] = a[j] - a[j+1]
            else:
                k += 1
    return a

@t.mark_test_unit(cases=[TestCase({"a": 1}, 1)], only_errors=True)
def func3(a):
    a = a/0

class A:

    c = 2

    def func4(self, a):
        return a / self.c

a = A()

t.add_test_unit(a.func4, [TestCase({"a": 1}, 0.5)])

cases5 = [TestCase({"a": 5}, 5), TestCase({"a": 15}, 15)]

@t.mark_test_unit(cases=cases5, asynchronous=True)
async def func5(a):
    if a <= 1: return a
    else: return await func5(a - 1) + await func5(a - 2)

t.test_all()

# asyncio.run(t.test_all_async()) async testing way

"""
Output:
****************************************************************************************************
UNIT: func1
----------------------------------------------------------------------------------------------------
CASE 0:
    Agruments: {'a': 100000}
    Correct answer: 100000
    Returned answer: 100000
    Result: PASSED
    Time: 0.012551069259643555 seconds
----------------------------------------------------------------------------------------------------
CASE 1:
    Agruments: {'a': 200000}
    Correct answer: 200000
    Returned answer: 200000
    Result: PASSED
    Time: 0.023479700088500977 seconds
----------------------------------------------------------------------------------------------------
CASE 2:
    Agruments: {'a': 200000}
    Correct answer: 300000
    Returned answer: 200000
    Result: FAILED
    Time: 0.02248382568359375 seconds
----------------------------------------------------------------------------------------------------
****************************************************************************************************
UNIT: func2
----------------------------------------------------------------------------------------------------
CASE 0:
    Agruments: {'a': [1, 2, 5, 5]}
    Correct answer: [1, 2, 5, 5]
    Returned answer: [1, 2, 5, 5]
    Result: PASSED
    Time: 0.0 seconds
----------------------------------------------------------------------------------------------------
CASE 1:
    Agruments: {'a': [0, 1, 3, 7, 7, 9]}
    Correct answer: [0, 1, 3, 7, 7, 9]
    Returned answer: [0, 1, 3, 7, 7, 9]
    Result: PASSED
    Time: 0.0 seconds
----------------------------------------------------------------------------------------------------
****************************************************************************************************
UNIT: func3
----------------------------------------------------------------------------------------------------
CASE 0: ERROR ( division by zero )
----------------------------------------------------------------------------------------------------
****************************************************************************************************
UNIT: func4
----------------------------------------------------------------------------------------------------
CASE 0:
    Agruments: {'a': 1}
    Correct answer: 0.5
    Returned answer: 0.5
    Result: PASSED
    Time: 0.0 seconds
----------------------------------------------------------------------------------------------------
****************************************************************************************************
UNIT: func5
----------------------------------------------------------------------------------------------------
CASE 0:
    Agruments: {'a': 5}
    Correct answer: 5
    Returned answer: 5
    Result: PASSED
    Time: 0.00202178955078125 seconds
----------------------------------------------------------------------------------------------------
CASE 1:
    Agruments: {'a': 15}
    Correct answer: 15
    Returned answer: 610
    Result: FAILED
    Time: 0.010009527206420898 seconds
----------------------------------------------------------------------------------------------------
****************************************************************************************************
NOT ALL TESTS PASSED :(
****************************************************************************************************
"""