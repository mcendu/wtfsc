#!/usr/bin/env python3
"""
An s-expression based calculator engine
"""
import math
import re

fnmap = {}
constmap = {
        "e": math.e,
        "inf": math.inf,
        "nan": math.nan,
        "pi": math.pi,
        "tau": math.tau
        }

def reg(s, f):
    fnmap[s] = f

def add(a, b):
    return a+b
def sub(a, b):
    return a-b
def mul(a, b):
    return a*b
def div(a, b):
    try:
        return a/b
    except ZeroDivisionError as err:
        raise InterpreterError('Division by 0')
def mod(a, b):
    return a%b
def neg(a):
    return -a
def q():
    raise SystemExit

reg("+", add)
reg("-", sub)
reg("*", mul)
reg("/", div)
reg("neg", neg)
reg("q", q)
reg("quit", q)

reg("abs", math.fabs)
reg("acos", math.acos)
reg("asin", math.asin)
reg("atan", math.atan)
reg("atan2", math.atan2)
reg("ceil", math.ceil)
reg("cos", math.cos)
reg("exp", math.exp)
reg("fac", math.factorial)
reg("factorial", math.factorial)
reg("floor", math.floor)
reg("gcd", math.gcd)
reg("hypot", math.hypot)
reg("lg", math.log10)
reg("ln", math.log)
reg("log", math.log)
reg("log2", math.log2)
reg("mod", math.fmod)
reg("pow", math.pow)
reg("sin", math.sin)
reg("sqrt", math.sqrt)
reg("tan", math.tan)
# Import extensions at here
#import ext_ext
#...

IDENT = re.compile('^[^ \t\r\n()]+$')
NUM   = re.compile('^[0-9]+(\.[0-9]+)?([eE][+-][0-9]+)?$')

class InterpreterError(Exception):
    '''All interpreter errors'''
    def __init__(self, message):
        self.message = message

def interpret(exp, cstack=[[None]]):
    # Lexical analysis
    tmp = ''
    for i in iter(exp):
        if i=='(':
            cstack.append([])
        elif IDENT.match(i):
            tmp += i;
        else:
            if tmp == '':
                'do nothing'
            elif NUM.match(tmp):
                cstack[-1].append(float(tmp))
                tmp = ''
            elif tmp in constmap:
                cstack[-1].append(constmap[tmp])
                tmp = ''
            else:
                cstack[-1].append(tmp)
                tmp = ''
            if i==')':
                if cstack[-1][0] in fnmap:
                    try:
                        ret = fnmap[cstack[-1][0]](
                                *cstack[-1][1:len(cstack[-1])])
                    except TypeError:
                        raise InterpreterError('Too few/many arguments')
                    except Exception:
                        raise InterpreterError('Error')
                    cstack[-2].append(ret)
                    cstack.pop()
                else:
                    raise InterpreterError('No such operation')
                if cstack[0][-1] != None:
                    print(cstack[0][-1])
                    cstack = [[None]]
    return cstack

if __name__ == "__main__":
    cstack = [[None]]
    try:
        while 1:
            if cstack[-1][0] == None:
                ps = 'wtfsc> '
            else:
                ps = '... '
            try:
                cstack = interpret(input(ps) + '\n', cstack)
            except InterpreterError as err:
                print(err.message)
                cstack = [[None]]
    except EOFError:
        print('\n')
        exit(0)
    except KeyboardInterrupt:
        print('\n')
        exit(0)
