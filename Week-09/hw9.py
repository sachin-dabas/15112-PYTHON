#################################################
# hw9.py
#
# Your name: sachin dabas
# Your andrew id: sdabas
#################################################

import cs112_f21_week9_linter
import math, copy, os


#################################################
# Helper functions
#################################################

def almostEqual(d1, d2, epsilon=10**-7):
    # note: use math.isclose() outside 15-112 with Python version 3.5 or later
    return (abs(d2 - d1) < epsilon)

import decimal
def roundHalfUp(d):
    # Round to nearest with ties going away from zero.
    rounding = decimal.ROUND_HALF_UP
    # See other rounding options here:
    # https://docs.python.org/3/library/decimal.html#rounding-modes
    return int(decimal.Decimal(d).to_integral_value(rounding=rounding))

#################################################
# Functions for you to write
#################################################

def oddCount(L,depth=0):
    #print(depth* '|   ', f'offCount({L})')
    if len(L) == 0:
        result = 0
    else:
        result = L[0]%2 + oddCount(L[1:],depth+1)
    #print(depth* '|   ',f'---> {result}')
    return result

def oddSum(L,depth=0):
    #print(depth* '|   ', f'oddSum({L})')
    if len(L) == 0:
        result = 0
    elif L[0]%2 == 0:
        result = oddSum(L[1:],depth+1)
    else:
        result = L[0] + oddSum(L[1:],depth+1)
    #print(depth* '|   ',f'---> {result}')
    return result

def oddsOnly(L,depth = 0):
    # print(depth* '|   ', f'oddsOnly({L})')
    # newList = [ ] not required since append wont work
    if L == [ ]: result = [ ]
    elif L[0]%2 == 0:
        result = oddsOnly(L[1:],depth+1)
    else:
        result = [L[0]] + oddsOnly(L[1:],depth+1)
    # print(depth* '|   ',f'---> {result}')
    return result

def maxOdd(L,depth=0):
    # print(depth* '|   ', f'oddsOnly({L})')
    if L == [ ]: return None
    val = L[0]
    rest = maxOdd(L[1:], depth+1)  #run function again i.e skip
    if val%2 == 0: # evens
        result = rest
    else:
        if rest == None:
            result = val
        else:
            #comparitive statements since cant use max function
            if val < rest :
                result = rest
            else:
                result = val
    # print(depth* '|   ',f'---> {result}')
    return result

def hasConsecutiveDigits(n):
    if n == 0: return False
    if n%10 == (n//10)%10:
        return True
    else:
        return hasConsecutiveDigits(n//10)

def alternatingSum(L,depth=0):
    # print(depth* '|   ', f'alternatingSum({L})')
    if len(L) == 0: 
        result = 0
    else: 
        result =  L[0] - alternatingSum(L[1:],depth+1)
    # print(depth* '|   ',f'---> {result}')
    return result

#################################################
# Freddy Fractal Viewer
#################################################

from cmu_112_graphics import *

def appStarted(app):
    app.level = 0 

def keyPressed(app, event): #referred from 112 notes
    if event.key in ['Up','Right']:
        app.level += 1
    elif (event.key in ['Down','Left']) and (app.level > 0):
        app.level -= 1

def drawFractal(app,canvas,level, cx, cy, r):
    if level == 0:
        # face of freddy
        canvas.create_oval(cx-r,cy-r,cx+r,cy+r,fill= 'brown',width=r//10)
        # eyes of freddy
        r1 = r//5
        x1,y1 = cx-(r1*2),cy-(r1*2)
        canvas.create_oval(x1-r1,y1-r1,x1+r1,y1+r1,fill= 'black')
        x2,y2 = cx+(r1*2),cy-(r1*2)
        canvas.create_oval(x2-r1,y2-r1,x2+r1,y2+r1,fill= 'black')
        # mouth of Freddy
        r2 = r//2
        canvas.create_oval(cx-r2,(cy+(0.75*r2))-r2,cx+r2,(cy+(0.75*r2))+r2,
                                fill='bisque',width=r//20)
        # nose of Freddy
        r3 = r//6 #eyes are bigger than nose :D
        canvas.create_oval(cx-r3,(cy+(0.75*r3))-r3,cx+r3,(cy+(0.75*r3))+r3,
                                fill='black',width=r//20)
        # smile of Freddy
        ''' #doesnt work for fractal freddy's
        r4 = r//4
        canvas.create_arc(cx,cy+30,cx+(r4),cy+(r4+30),extent=-180,
                             style=ARC)
        canvas.create_arc(cx-r4,cy+30,cx,cy+(r4+30),extent=-180,
                             style=ARC)
        '''
        r4= r*0.3
        canvas.create_arc(cx,(cy+r4*1.1),cx+r4,cy+(r4*2),
                            extent=-180,style=ARC,width=r4//5)
        canvas.create_arc(cx-r4,(cy+r4*1.1),cx,cy+(r4*2),
                            extent=-180,style=ARC,width=r4//5)
    else:
        # recursive case
        drawFractal(app,canvas,level-1,cx,cy,r)
        '''drawFractal(app,canvas,level-1,cx-(r+5),cy-(r+5),r/2)
        need to multiply with r to get right recursive distance'''
        drawFractal(app,canvas,level-1,cx-(r*1.1),cy-(r*1.1),r//2)
        drawFractal(app,canvas,level-1,cx+(r*1.1),cy-(r*1.1),r//2)

def drawLevel(app,canvas,level):
    margin = min(app.width, app.height)//10
    x, y = app.width//2, app.height//2
    r = app.width/5 #5 is approx value
    drawFractal(app, canvas, level, x, y, r)

def redrawAll(app, canvas):
    canvas.create_text(app.width/2, 100 + app.height/2,
                        text='Hey its our Freddy Fractals!',
                        font='Arial 12 bold')
    canvas.create_text(app.width/2, 120 + app.height/2,
                        text=f'Level {app.level} Fractal',
                        font='Arial 10 bold')
    canvas.create_text(app.width/2, 140 + app.height/2,
                        text='Use arrows to change level',
                        font='Arial 8 bold')
    drawLevel(app,canvas,app.level)

def runFreddyFractalViewer():
    print('Running Freddy Fractal Viewer!')
    runApp(width=400, height=400)

#################################################
# Test Functions
#################################################

def testOddCount():
    print('Testing oddCount()...', end='')
    assert(oddCount([ ]) == 0)
    assert(oddCount([ 2, 4, 6 ]) == 0) 
    assert(oddCount([ 2, 4, 6, 7 ]) == 1)
    assert(oddCount([ -1, -2, -3 ]) == 2)
    assert(oddCount([ 1,2,3,4,5,6,7,8,9,10,0,0,0,11,12 ]) == 6)
    print('Passed!')

def testOddSum():
    print('Testing oddSum()...', end='')
    assert(oddSum([ ]) == 0)
    assert(oddSum([ 2, 4, 6 ]) == 0) 
    assert(oddSum([ 2, 4, 6, 7 ]) == 7)
    assert(oddSum([ -1, -2, -3 ]) == -4)
    assert(oddSum([ 1,2,3,4,5,6,7,8,9,10,0,0,0,11,12 ]) == 1+3+5+7+9+11)
    print('Passed!')

def testOddsOnly():
    print('Testing oddsOnly()...', end='')
    assert(oddsOnly([ ]) == [ ])
    assert(oddsOnly([ 2, 4, 6 ]) == [ ]) 
    assert(oddsOnly([ 2, 4, 6, 7 ]) == [ 7 ])
    assert(oddsOnly([ -1, -2, -3 ]) == [-1, -3])
    assert(oddsOnly([ 1,2,3,4,5,6,7,8,9,10,0,0,0,11,12 ]) == [1,3,5,7,9,11])
    print('Passed!')

def testMaxOdd():
    print('Testing maxOdd()...', end='')
    assert(maxOdd([ ]) == None)
    assert(maxOdd([ 2, 4, 6 ]) == None) 
    assert(maxOdd([ 2, 4, 6, 7 ]) == 7)
    assert(maxOdd([ -1, -2, -3 ]) == -1)
    assert(maxOdd([ 1,2,3,4,5,6,7,8,9,10,0,0,0,11,12 ]) == 11)
    print('Passed!')

def testHasConsecutiveDigits():
  print('Testing hasConsecutiveDigits()...', end='')
  assert(hasConsecutiveDigits(1123) == True)
  assert(hasConsecutiveDigits(-1123) == True)
  assert(hasConsecutiveDigits(1234) == False)
  assert(hasConsecutiveDigits(0) == False)
  assert(hasConsecutiveDigits(1233) == True)
  print("Passed!")

def testAlternatingSum():
    print('Testing alternatingSum()...', end='')
    assert(alternatingSum([1,2,3,4,5]) == 1-2+3-4+5)
    assert(alternatingSum([ ]) == 0)
    print('Passed!')

#################################################
# testAll and main
#################################################

def testAll():
    testOddCount()
    testOddSum()
    testOddsOnly()
    testMaxOdd()
    testHasConsecutiveDigits()
    testAlternatingSum()
    runFreddyFractalViewer()

def main():
    cs112_f21_week9_linter.lint()
    testAll()

if (__name__ == '__main__'):
    main()
