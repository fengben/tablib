import  tablib
class Abc:
    def __init__(self):
        pass
    def __getitem__(self, item):
        pass



if __name__ == '__main__':
    data = [
        ('John', 'Adams'),
        ('George', 'Washington')
    ]
    headers = ('first_name', 'last_name')

    # data = tablib.Dataset(*data)
    # da=(row for row in data)
    # print(list(da))
    # list1=[1,2,3,4,5]
    # a=(str(i) for i in list1)
    # print(a)
