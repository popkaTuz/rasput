def func7(arg19, arg20):
    var25 = func8(arg19, arg20)
    var29 = func9(arg20, arg19)
    var30 = arg19 | var25
    var31 = 1867496838 + (var29 & -169) | 1449641919
    var32 = var30 ^ var25 & -667781437 + arg19
    var33 = var32 - (779 + arg19) - -1846868394
    var34 = var29 & var25 & (var33 & arg19)
    var35 = var33 + var33
    var36 = var25 - (var31 + 1292980820)
    var37 = var30 | var33 & arg19
    var38 = var36 - var34 - var33
    var39 = var31 ^ var37 & arg19 ^ 897
    var40 = var38 - var36
    var41 = var33 - arg19 ^ var33 - var36
    result = var41 ^ var34
    return result
def func9(arg26, arg27):
    var28 = (366992434 | arg26) & 208 ^ (arg26 - 1510814164 ^ (arg27 - (461 ^ -1436163574 & ((arg26 + arg26) & ((arg26 | arg27 | arg26 | arg27) - arg27 + arg26))) - ((arg26 + 94) + arg26 + -2137481212)) - arg27) - arg27
    result = (-669 | var28 - ((((arg27 ^ (-301 & var28 | arg26) + arg26) ^ arg27) & -154670098) - arg26) ^ arg26) + 388
    return result
def func8(arg21, arg22):
    var23 = 0
    for var24 in xrange(48):
        var23 += (7 | -7) & var24
    return var23
def func1(arg1, arg2):
    var6 = func2(arg1, arg2)
    def func4(arg7, arg8):
        var9 = arg8 - arg2
        var10 = arg8 & var9
        var11 = 155 & (var10 & var10)
        if var6 < arg1:
            var12 = arg1 - (arg7 ^ (arg8 + -151611362)) & (((arg8 & (arg7 | arg2 + (arg1 | 1355158214 + (-955 & (arg7 - arg7 - arg1))) + (arg1 - -1226264030 | ((var11 - var6 | var10) | arg7)))) + var6) | var10) ^ arg2
        else:
            var12 = var9 - var10 + (arg7 - (arg7 + var10 + (arg8 + (arg2 | arg2))) - arg8 ^ (var10 & arg8)) - var9
        var13 = var10 ^ arg7 - (-762 & (1731662493 - arg7 - arg7 | var10)) + arg1
        result = arg2 ^ var6
        return result
    var14 = func4(arg1, arg2)
    var18 = func5(arg1, var6)
    result = arg2 - 1160082355
    return result
def func2(arg3, arg4):
    def func3(acc, rest):
        var5 = rest + -10 - acc
        if acc == 0:
            return var5
        else:
            result = func3(acc - 1, var5)
            return result
    result = func3(10, 0)
    return result
def func5(arg15, arg16):
    def func6(acc, rest):
        var17 = -5 + (-5 | -8)
        if acc == 0:
            return var17
        else:
            result = func6(acc - 1, var17)
            return result
    result = func6(10, 0)
    return result
if __name__ == "__main__":
    print 'prog_size: 3'
    print 'func_number: 7'
    print 'arg_number: 19'
    for i in xrange(25000):
        x = 5
        x = func1(x, i)
        print x,
    print 'prog_size: 5'
    print 'func_number: 10'
    print 'arg_number: 42'
    for i in xrange(25000):
        x = 5
        x = func7(x, i)
        print x,
