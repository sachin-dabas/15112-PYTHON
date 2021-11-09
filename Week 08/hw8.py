#################################################
# hw8.py:
#
# Your name: sachin dabas
# Your andrew id: sdabas
#################################################

import cs112_f21_week8_linter
from cmu_112_graphics import *

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

#import library
import math
from dataclasses import make_dataclass
import random

#################################################
# Midterm1 Free Responses
#################################################

##reference = midterm sol
def firstNAcceptedValues(n, rules):
    found = []
    guess = 0
    while (len(found) < n):
        guess += 1
        if isAcceptedValue(guess,rules):
            found.append(guess)
    return found

def isAcceptedValue(x,rules):
    for line in rules:
        parts = line.split()
        if '%' in line:
            factor = int(parts[0][2:])
            check = x % factor
        else: check = x
        findIndex = int(parts[-1])
        if 'equal' in line:
            acceptedValue = (check == findIndex)
        else: acceptedValue = (check % findIndex == 0)
        if 'not' in line:
            acceptedValue = not acceptedValue
        if not acceptedValue: return False 
    return True

##reference = midterm sol
#make dataclass
Dot = make_dataclass('Dot',['cx','cy','r','dx','dy','color'])

def appStarted(app):
    app.dots = []

def distance(x0,y0,x1,y1):
    return math.sqrt((x0-x1)**2 + (y0-y1)**2)

def mousePressed(app, event):
    isClicked = False
    for i in range(len(app.dots)):
        if (distance(event.x,event.y,app.dots[i].cx,
                        app.dots[i].cy) < app.dots[i].r):
            if (app.dots[i].color == 'red'):
                app.dots[i].color ='green' 
            else: app.dots[i].color ='red'
            isClicked = True
    if isClicked == False:
        newDot = Dot(event.x,event.y,20,random.randint(-3,3), 
                    random.randint(-3,3), 'green')
        app.dots.append(newDot)

def timerFired(app):
    i = 0
    while i < len(app.dots):
        if app.dots[i].color == 'green':
            app.dots[i].cx += app.dots[i].dx
            app.dots[i].cy += app.dots[i].dy
        if (app.dots[i].cx < 0 or app.dots[i].cx > app.width or 
            app.dots[i].cy < 0 or app.dots[i].cy > app.height):
            app.dots.pop(i)
        else: i += 1

def redrawAll(app, canvas):
    canvas.create_text(app.width/2, app.height/2,
                       text=f'{len(app.dots)} Dot(s)', font='Arial 30 bold')
    for dot in app.dots:
        canvas.create_oval(dot.cx-dot.r,dot.cy-dot.r,dot.cx+dot.r,dot.cy+dot.r,
                             fill = dot.color)

def midterm1Animation():
    runApp(width=400, height=400)

#################################################
# Other Classes and Functions for you to write
#################################################

class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.friendsList = []
        self.friendsNames = []

    def getName(self):
        return self.name

    def getAge(self):
        return self.age

    def getFriends(self):
        print(self.friendsList)
        return self.friendsList

    def getFriendsNames(self):
        return sorted(self.friendsNames)

    def addFriend(self, friend):
        if friend not in self.friendsList: 
            self.friendsList.append(friend) # add friend
            friend.friendsList.append(self) #friends are mutual
            friend.friendsNames.append(self.name) #get friendsnames
            self.friendsNames.append(friend.name) #get friend name

    def addFriends(self, friend):
        for friend in friend.friendsList:
                self.addFriend(friend)
        


def getPairSum(L, target):
    #initialize result = empty set
    s = set(L)
    dict={}
    for ele in s: #O(n)
        dict[ele] = 0
    for ele in L: #O(n)
        dict[ele] += 1
    #loop in set
    for num1 in L: #O(n)
        #find the required num
        num2 = target - num1
        
        #if found, return tuple
        if num2 in s and num1 != num2: #condition to avoid half of num1
            return (num1,num2)
        elif num1 == num2 and dict[num1] > 1:
            return (num1,num1)
    return None   

def containsPythagoreanTriple(L):
    #initialize result = empty set
    s = set(L)
    #loop in List
    for num1 in L:
        #loop in set
        for num2 in s:
            num3 = math.sqrt((num1**2) + (num2**2))
            #find third value in set
            if num3 in s:
                return True
    return False

def movieAwards(oscarResults):
    #initialize result = empty dictionary
    result = dict()
    #loop through set of tuples
    for cat,keys in oscarResults: #O(n)
        #assign keys to dict and count
        result[keys] = result.get(keys,0) + 1
    return result

def friendsOfFriends(friends):
    #initialize result = empty dictionary
    result = dict()
    #loop through keys
    for key in friends:
        #initialize empty set
        s = set()
        values = friends[key]
        #access values in key 
        for friend in values:
            for fof in friends.get(friend):
                #if not person or friend of person
                if fof!= key and fof not in values:
                    # add to set
                    s.add(fof)
        result[key] = s
    return result #O(N2)

#################################################
# Bonus Animation
#################################################

def bonus_appStarted(app):
    app.counter = 0

def bonus_keyPressed(app, event):
    pass

def bonus_mousePressed(app, event):
    pass

def bonus_timerFired(app):
    app.counter += 1

def bonus_redrawAll(app, canvas):
    canvas.create_text(app.width/2, app.height/2,
                       text=f'bonusAnimation', font='Arial 30 bold')
    canvas.create_text(app.width-20, app.height-20, text=str(app.counter))

def bonusAnimation():
    runApp(width=400, height=400, fnPrefix='bonus_')

#################################################
# Test Functions
#################################################


def testFirstNAcceptedValues():
    print('Testing firstNAcceptedValues...', end='')
    oneRule = [ 'x must be a multiple of 3' ]
    assert(firstNAcceptedValues(6, oneRule) == [3, 6, 9, 12, 15, 18])
    twoRules = [ 'x must be a multiple of 3',
                 'x must not be a multiple of 9' ]
    assert(firstNAcceptedValues(6, twoRules) == [3, 6, 12, 15, 21, 24])
    fourRules = [ 'x must be a multiple of 3',
                  'x must not be a multiple of 9',
                  'x%2 must be a multiple of 2',
                  'x%10 must not be equal to 4' ]
    assert(firstNAcceptedValues(6, fourRules) == [6, 12, 30, 42, 48, 60])
    print("Passed!")
    

def testMidterm1Animation():
    print('Note: You must visually inspect your midterm1 animation to test it.')
    midterm1Animation()

def testPersonClass():
    print('Testing Person Class...', end='')
    fred = Person('fred', 32)
    assert(isinstance(fred, Person))
    assert(fred.getName() == 'fred')
    assert(fred.getAge() == 32)
    # Note: person.getFriends() returns a list of Person objects who
    #       are the friends of this person, listed in the order that
    #       they were added.
    # Note: person.getFriendNames() returns a list of strings, the
    #       names of the friends of this person.  This list is sorted!
    assert(fred.getFriends() == [ ])
    assert(fred.getFriendsNames() == [ ])

    wilma = Person('wilma', 35)
    assert(wilma.getName() == 'wilma')
    assert(wilma.getAge() == 35)
    assert(wilma.getFriends() == [ ])

    wilma.addFriend(fred)
    assert(wilma.getFriends() == [fred])
    assert(wilma.getFriendsNames() == ['fred'])
    assert(fred.getFriends() == [wilma]) # friends are mutual!
    assert(fred.getFriendsNames() == ['wilma'])

    wilma.addFriend(fred)
    assert(wilma.getFriends() == [fred]) # don't add twice!

    betty = Person('betty', 29)
    fred.addFriend(betty)
    assert(fred.getFriendsNames() == ['betty', 'wilma'])

    pebbles = Person('pebbles', 4)
    betty.addFriend(pebbles)
    assert(betty.getFriendsNames() == ['fred', 'pebbles'])

    barney = Person('barney', 28)
    barney.addFriend(pebbles)
    barney.addFriend(betty)
    barney.addFriends(fred) # add ALL of Fred's friends as Barney's friends
    assert(barney.getFriends() == [pebbles, betty, wilma])
    assert(barney.getFriendsNames() == ['betty', 'pebbles', 'wilma'])
    fred.addFriend(wilma)
    fred.addFriend(barney)
    assert(fred.getFriends() == [wilma, betty, barney])
    assert(fred.getFriendsNames() == ['barney', 'betty', 'wilma']) # sorted!
    assert(barney.getFriends() == [pebbles, betty, wilma, fred])
    assert(barney.getFriendsNames() == ['betty', 'fred', 'pebbles', 'wilma'])
    print('Passed!')

def testGetPairSum():
    print("Testing getPairSum()...", end="")
    # assert(getPairSum([1], 1) == None)
    # assert(getPairSum([5, 2], 7) in [ (5, 2), (2, 5) ])
    # assert(getPairSum([10, -1, 1, -8, 3, 1], 2) in
    #                   [ (10, -8), (-8, 10),(-1, 3), (3, -1), (1, 1) ])
    # assert(getPairSum([10, -1, 1, -8, 3, 1], 10) == None)
    # assert(getPairSum([10, -1, 1, -8, 3, 1, 8, 19, 0, 5], 10) in
    #                   [ (10, 0), (0, 10)] )
    assert(getPairSum([10, -1, 1, -8, 3, 1, 8, 19, -9, 5], 10) in
                      [ (19, -9), (-9, 19)] )
    assert(getPairSum([1, 4, 3], 2) == None) # catches reusing values! 1+1...
    print("Passed!")

def testContainsPythagoreanTriple():
    print("Testing containsPythagoreanTriple()...", end="")
    assert(containsPythagoreanTriple([1,3,6,2,5,1,4]) == True)
    assert(containsPythagoreanTriple([1,3,6,2,8,1,4]) == False)
    assert(containsPythagoreanTriple([1,730,3,6,54,2,8,1,728,4])
                                      == True) # 54, 728, 730
    assert(containsPythagoreanTriple([1,730,3,6,54,2,8,1,729,4]) == False)
    assert(containsPythagoreanTriple([1,731,3,6,54,2,8,1,728,4]) == False)
    assert(containsPythagoreanTriple([1,731,3,6,54,2,8,1,728,4,
                                6253, 7800, 9997]) == True) # 6253, 7800, 9997
    assert(containsPythagoreanTriple([1,731,3,6,54,2,8,1,728,4,
                                      6253, 7800, 9998]) == False)
    assert(containsPythagoreanTriple([1,731,3,6,54,2,8,1,728,4,
                                      6253, 7800, 9996]) == False)
    print("Passed!")

def testMovieAwards():
    print('Testing movieAwards()...', end='')
    tests = [
      (({ ("Best Picture", "The Shape of Water"), 
          ("Best Actor", "Darkest Hour"),
          ("Best Actress", "Three Billboards Outside Ebbing, Missouri"),
          ("Best Director", "The Shape of Water") },),
        { "Darkest Hour" : 1,
          "Three Billboards Outside Ebbing, Missouri" : 1,
          "The Shape of Water" : 2 }),
      (({ ("Best Picture", "Moonlight"),
          ("Best Director", "La La Land"),
          ("Best Actor", "Manchester by the Sea"),
          ("Best Actress", "La La Land") },),
        { "Moonlight" : 1,
          "La La Land" : 2,
          "Manchester by the Sea" : 1 }),
      (({ ("Best Picture", "12 Years a Slave"),
          ("Best Director", "Gravity"),
          ("Best Actor", "Dallas Buyers Club"),
          ("Best Actress", "Blue Jasmine") },),
        { "12 Years a Slave" : 1,
          "Gravity" : 1,
          "Dallas Buyers Club" : 1,
          "Blue Jasmine" : 1 }),
      (({ ("Best Picture", "The King's Speech"),
          ("Best Director", "The King's Speech"),
          ("Best Actor", "The King's Speech") },),
        { "The King's Speech" : 3}),
      (({ ("Best Picture", "Spotlight"), ("Best Director", "The Revenant"),
          ("Best Actor", "The Revenant"), ("Best Actress", "Room"),
          ("Best Supporting Actor", "Bridge of Spies"),
          ("Best Supporting Actress", "The Danish Girl"),
          ("Best Original Screenplay", "Spotlight"),
          ("Best Adapted Screenplay", "The Big Short"),
          ("Best Production Design", "Mad Max: Fury Road"),
          ("Best Cinematography", "The Revenant") },),
        { "Spotlight" : 2,
          "The Revenant" : 3,
          "Room" : 1,
          "Bridge of Spies" : 1,
          "The Danish Girl" : 1,
          "The Big Short" : 1,
          "Mad Max: Fury Road" : 1 }),
       ((set(),), { }),
            ]
    for args,result in tests:
        if (movieAwards(*args) != result):
            print('movieAwards failed:')
            print(args)
            print(result)
            assert(False)
    print('Passed!')

def testFriendsOfFriends():
    print("Testing friendsOfFriends()...", end="")
    d = dict()
    d["fred"] = set(["wilma", "betty", "barney", "bam-bam"])
    d["wilma"] = set(["fred", "betty", "dino"])
    d["betty"] = d["barney"] = d["bam-bam"] = d["dino"] = set()
    fof = friendsOfFriends(d)
    assert(fof["fred"] == set(["dino"]))
    assert(fof["wilma"] == set(["barney", "bam-bam"]))
    result = { "fred":set(["dino"]),
               "wilma":set(["barney", "bam-bam"]),
               "betty":set(),
               "barney":set(),
               "dino":set(),
               "bam-bam":set()
             }
    assert(fof == result)
    d = dict()
    #                A    B    C    D     E     F
    d["A"]  = set([      "B",      "D",        "F" ])
    d["B"]  = set([ "A",      "C", "D",  "E",      ])
    d["C"]  = set([                                ])
    d["D"]  = set([      "B",            "E",  "F" ])
    d["E"]  = set([           "C", "D"             ])
    d["F"]  = set([                "D"             ])
    fof = friendsOfFriends(d)
    assert(fof["A"] == set(["C", "E"]))
    assert(fof["B"] == set(["F"]))
    assert(fof["C"] == set([]))
    assert(fof["D"] == set(["A", "C"]))
    assert(fof["E"] == set(["B", "F"]))
    assert(fof["F"] == set(["B", "E"]))
    result = { "A":set(["C", "E"]),
               "B":set(["F"]),
               "C":set([]),
               "D":set(["A", "C"]),
               "E":set(["B", "F"]),
               "F":set(["B", "E"])
              }
    assert(fof == result)
    print("Passed!")

def testBonusAnimation():
    print('Note: You must visually inspect your bonus animation to test it.')
    bonusAnimation()

def testAll():
    testFirstNAcceptedValues()
    testMidterm1Animation()
    testPersonClass()
    testGetPairSum()
    testContainsPythagoreanTriple()
    testMovieAwards()
    testFriendsOfFriends()
    testBonusAnimation()

#################################################
# main
#################################################

def main():
    cs112_f21_week8_linter.lint()
    testAll()

if __name__ == '__main__':
    main()
