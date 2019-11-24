def unitest():
    assert(compare("0.1", "1.1") == -1)
    assert(compare("1.0.1", "1") == 1)
    assert(compare("7.5.2.4", "7.5.3") == -1)
    assert(compare("1.01", "1.001") == 0)
    assert(compare("1.0", "1.0.0") == 0)
    print('pass')

def compare(v1, v2):
    l1 = v1.split('.')
    l2 = v2.split('.')
    flag = 0
    while True:
        if flag == len(l1) and flag == len(l2):
            return 0
        if len(l1) == flag:
            l1.append(0)
        if len(l2) == flag:
            l2.append(0)
        if int(l1[flag]) > int(l2[flag]):
            return 1
        elif int(l1[flag]) < int(l2[flag]):
            return -1
        flag += 1

if __name__ == "__main__":
    unitest()
