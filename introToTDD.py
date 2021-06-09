import unittest

def reverseList(arr):
    for i in range(len(arr)//2):
        arr[i],arr[len(arr)-1-i]=arr[len(arr)-1-i],arr[i]
    return arr

class reverseListTests(unittest.TestCase):
    def testOne(self):
        self.assertEqual(reverseList([2,5,6,7,9,1,6,1]), [1,6,1,9,7,6,5,2], 'test one not passed')
    def testTwo(self):
        self.assertEqual(reverseList(['h','e','l','l','o',' ','w','o','r','l','d']), ['d','l','r','o','w',' ','o','l','l','e','h'], 'test two not passed')
    def testThree(self):
        self.assertEqual(reverseList(['h','i',9,8,7,5,'b','y','e']), ['e','y','b',5,7,8,9,'i','h'], 'test three not passed')
    def setUp(self):
        print("running setUp for reverseTests")
    def tearDown(self):
        print("running tearDown tasks for reverseTests")

def isPalindrome(str):
    str=str.lower()
    for i in range(len(str)//2):
        if str[i]!=str[len(str)-1-i]:
            return False
    return True

class isPalindromeTests(unittest.TestCase):
    def testOne(self):
        self.assertTrue(isPalindrome('racecar'))
    def testTwo(self):
        self.assertFalse(isPalindrome('supercalifragilistic'))
    def testThree(self):
        self.assertTrue(isPalindrome('Ward Draw'))
    def testFour(self):
        self.assertFalse(isPalindrome("this one shouldn't work"))
    def testFive(self):
        self.assertTrue(isPalindrome('Rotator'))
    def setUp(self):
        print("running setUp for palindrome tests")
    def tearDown(self):
        print("running tearDown tasks for palindrome tests")


def coins(num):
    coins={
        'quarter':25,
        'dime':10,
        'nickel':5,
        'penny':1
    }
    for key in coins:
        result=num//coins[key]
        num=num%coins[key]
        coins[key]=result
    return coins

class coinTests(unittest.TestCase):
    def testOne(self):
        self.assertEqual(coins(99),{'quarter':3,'dime':2,'nickel':0,'penny':4})
    def testTwo(self):
        self.assertEqual(coins(43),{'quarter':1,'dime':1,'nickel':1,'penny':3})
    def testThree(self):
        self.assertEqual(coins(87),{'quarter':3,'dime':1,'nickel':0,'penny':2})
    def testFour(self):
        self.assertEqual(coins(84),{'quarter':3,'dime':0,'nickel':1,'penny':4})
    def testFive(self):
        self.assertEqual(coins(72),{'quarter':2,'dime':2,'nickel':0,'penny':2})
    def setUp(self):
        print("running setUp for coin tests")
    def tearDown(self):
        print("running tearDown tasks for coin tests")


def factorial(num):
    for i in range(num-1, 0, -1):
        num=num*i
    return num

class factorialTests(unittest.TestCase):
    def testOne(self):
        self.assertEqual(factorial(5),120)
    def testTwo(self):
        self.assertEqual(factorial(4),24)
    def setUp(self):
        print("running setUp for factorial tests")
    def tearDown(self):
        print("running tearDown tasks for factorial tests")

def fibonacci(num):
    seq=[0,1]
    if num>2:
        for i in range(2,num+1):
            seq=seq+[seq[i-1]+seq[i-2]]
        return seq
    elif num==1:
        return seq
    else:
        return seq[0]

class fibonacciTests(unittest.TestCase):
    def testOne(self):
        self.assertEqual(fibonacci(5),[0,1,1,2,3,5])
    def testTwo(self):
        self.assertEqual(fibonacci(4),[0,1,1,2,3])
    def testThree(self):
        self.assertEqual(fibonacci(8),[0,1,1,2,3,5,8,13,21])
    def setUp(self):
        print("running setUp for fibonacci tests")
    def tearDown(self):
        print("running tearDown tasks for fibonacci tests")


if __name__ == '__main__':
    unittest.main()