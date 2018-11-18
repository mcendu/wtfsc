#/usr/bin/env python3 -O
"""
An s-expression based calculator engine
"""
import math
import re

fnmap = {}
const = {
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
    return a/b
def mod(a, b):
    return a%b
def neg(a):
    return -a;

reg("+", add)
reg("-", sub)
reg("*", mul)
reg("/", div)
reg("neg", neg)

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

def intepret(exp, cstack=[[]]):
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
            else:
                cstack[-1].append(tmp)
                tmp = ''
            if i==')':
                if cstack[-1][0] in fnmap:
                    ret = fnmap[cstack[-1][0]](*cstack[-1][1:len(cstack[-1])])
                    cstack[-2].append(ret)
                    cstack.pop()
    return 0;
