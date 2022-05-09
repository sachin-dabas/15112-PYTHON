#randomly select elements in the set
# a = int(-1.2)
# print(a)


# s = { 1,2,3 }
# a = { 4,5,6 }
# d = {}
# print(type(d))
# for elem in a:
#     s.add(elem)
# print(s)


# Note: almostEqual(x, y) and roundHalfUp(n) are both supplied for you. On all
#   quizzes, you may write additional helper functions if you wish.
def almostEqual(d1, d2, epsilon=10**-7): #helper-fn
    return (abs(d2 - d1) < epsilon)

import decimal
def roundHalfUp(d): #helper-fn
    # Round to nearest with ties going away from zero.
    rounding = decimal.ROUND_HALF_UP
    return int(decimal.Decimal(d).to_integral_value(rounding=rounding))
#---------------

#Write your function here:
def isNearlyFactorish(n):
    if n < 100 or n > 999:
        return False
    if isFactor(n):
        return True
    return False

def isFactor(n):
    pass



# We have provided these test cases:
def testIsNearlyFactorish():
    print('Testing isNearlyFactorish()...', end='')
    assert(isNearlyFactorish(152) == True)
    assert(isNearlyFactorish(264) == False)
    assert(isNearlyFactorish(130) == False)   # 0 is not positive
    assert(isNearlyFactorish(1234) == False)  # too big
    assert(isNearlyFactorish(12) == False)    # too small
    assert(isNearlyFactorish(-124) == False)  # ditto
    assert(isNearlyFactorish(124.0) == False) # not an integer
    assert(isNearlyFactorish('ack') == False) # ditto

    # we added a few more test cases after the quiz
    # to help with your Fix-It Friday submission:
    assert(isNearlyFactorish(153) == False)
    assert(isNearlyFactorish(-152) == False)
    assert(isNearlyFactorish(140) == False)
    assert(isNearlyFactorish(-140) == False)

    print('Passed!')

testIsNearlyFactorish()