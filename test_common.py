def assert_eq(a, b):
    if not a == b:
        print '**  expected: ', a
        print '**  actual  : ', b
        raise AssertionError('two objects does not equal')

def assert_ne(a, b):
    if a == b:
        print '**  both are: ', a
        raise AssertionError('two objects equals')

def assert_list_eq(a, b):
    errmsg = ''
    if len(a) != len(b):
        errmsg = 'two list has different length\n'
        errmsg += '**  expected: ' + str(len(a)) + '\n'
        errmsg += '**  actual  : ' + str(len(b)) + '\n'

    length = min((len(a), len(b)))
    for i in range(0, length):
        if not a[i] == b[i]:
            errmsg += '\nat ' + str(i) + '\n'
            errmsg += '**  expected: ' + str(a[i]) + '\n'
            errmsg += '**  actual  : ' + str(b[i]) + '\n'

    if len(errmsg):
        raise AssertionError(errmsg)
