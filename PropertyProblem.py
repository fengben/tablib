class Exp(object):
    def __init__(self,*args,**kwargs):
        '''bound to _set_headers'''
        self.headers=kwargs.get('headers')
        '''bound to _get headers'''
        # print(self.headers)

    def _get_headers(self):
        pass
    """:param: abc"""
    def _set_headers(self,abc):
        print(abc)

    headers = property(_get_headers, _set_headers)



class Shuxing():
    def __init__(self, size = 10):
        self.size = size
    def getSize(self):
        return self.size
    def setSize(self, value):
        self.size = value
    def delSize(self):
        del self.size
    x = property(getSize, setSize, delSize)


if __name__ == '__main__':
    headers = ('first_name', 'last_name')
    dic = {'headers': headers, 'others': ''}
    exp=Exp(**dic)
    print(exp.headers)
    # print(exp.headersabc)
    # print(Exp.headers)
    # print(Shuxing.x)
    # sx=Shuxing(100)