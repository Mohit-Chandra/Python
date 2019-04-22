import time
import sys
class Test:
    def __init__(self):
        print('Object initialization...')
    def __del__(self):
        print('Object cleanup activities...')

t1 = Test()
time.sleep(10)
t2=t1
t3=t2
del t3,t2,t1
print('Ref count is: ',sys.getrefcount(t1))
