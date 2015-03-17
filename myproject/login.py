# -*- coding: utf8 -*-
#
# 查找字符串中最长的字串（要求字串按字母顺序递增），如"abcdxpq" 最长字串为abcd
#
# 按字典序，获得从字符串首位开始最长的字串
#
# 用循环和递归分别实现


def getfirststr(s):
    end = 0
    sindex = 1
    for character in s:
        if sindex >= len(s):
            break
        if ord(character) - ord(s[sindex]) <= 0:
            sindex += 1
            continue
        else:
            break
    return s[:sindex]


def getlongeststr(s):
    length = len(s)
    strlist = [getfirststr(s[i:]) for i in range(length)]
    lenlist = [len(l) for l in strlist]
    maxlen = max(lenlist)
    for i in strlist:
        if maxlen == len(i):
            return i


def printinfo(month, minipay, remain):
    print "Month:", month
    print "Minimum monthly payment: %.2f" % minipay
    print "Remaining balance: %.2f" % remain


def showminpaying(balance, annualInterestRate, monthlyPaymentRate):
    month = 0
    minipayment = balance * monthlyPaymentRate
    remainbalance = balance - minipayment
    totalpay = 0
    print minipayment, remainbalance
    for i in range(1, 13):
        month = i
        printinfo(month, minipayment, remainbalance)
        totalpay += minipayment
        balance = remainbalance + (annualInterestRate/12.0) * remainbalance
        minipayment = balance * monthlyPaymentRate
        remainbalance = balance - minipayment
    print "Total paid: %.2f" % totalpay
    print "Remaining balance: %.2f" % remainbalance


def minimumpayment(balance, annualInterestRate):
    monthlyrate = annualInterestRate / 12.0
    fixedpayment = 10
    while True:
        ub = balance
        for i in range(0, 12):
            ub -= fixedpayment
            ub += ub * monthlyrate
        if ub <= 0:
            break
        else:
            fixedpayment += 10
            continue
    print "Lowest Payment:", fixedpayment


def bisectminipay(balance, annualInterestRate):
    monthlyrate = annualInterestRate / 12.0
    lowerbound, upperbound = balance / 12, (balance * (1 + monthlyrate)**12) / 12
    ub = balance
    mid = (lowerbound + upperbound) / 2.0
    while abs(0 - ub) >= 0.01:
        for i in range(0, 12):
            ub -= mid
            ub += ub * monthlyrate
            break
        if ub >= 0:
            lowerbound = mid
        else:
            upperbound = mid
        ub = balance
        mid = (lowerbound + upperbound) / 2
    print "Lowest Payment: %.2f" % mid


if __name__ == "__main__":
    bisectminipay(999999, 0.18)
    # balance = 999999
    # annualInterestRate = 0.18
    #
    # updatedBalance = balance
    # monthlyInterestRate = (annualInterestRate) / 12
    # epsilon = 0.01
    # numGuesses = 0
    # lowerBound = balance / 12
    # upperBound = (balance * (1 + monthlyInterestRate)**12) / 12
    # ans = (upperBound + lowerBound)/2.0
    #
    # while abs(0 - updatedBalance) >= epsilon:
    # 	print('low = ' + str(lowerBound) + ' high = ' + str(upperBound) + ' ans = ' + str(ans))
    # 	updatedBalance = balance
    # 	numGuesses += 1
    # 	for i in range(0, 12):
    # 		updatedBalance = round(((updatedBalance - ans) * (1 + monthlyInterestRate)), 2)
    # 	if updatedBalance >= 0:
    # 		lowerBound = ans
    # 	else:
    # 		upperBound = ans
    # 	ans = (upperBound + lowerBound)/2.0
    # print('numGuesses = ' + str(numGuesses))
    # print("Lowest Payment: " + str(round(ans, 2)))