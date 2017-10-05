import tablib

headers = ('first_name', 'last_name')

data = [
        ('John', 'Adams'),
        ('George', 'Washington')
    ]
data1=[
    ('Zhiqian','Xue'),
    ('Guorong','Zhang'),
    ('Jay','Zhou'),
    ('Xueyou','Zhang')
]
if __name__ == '__main__':

    data = tablib.Dataset(*data, headers=headers)
    data= tablib.Dataset(*data1,headers=headers)
    data.append(('Henry', 'Ford'))
    # data.append_col((90, 67, 83), header='age')
    # print(data[:2])
    # print(data['first_name'])
    # print(data.transpose())
    # print(data.stack_cols(data1))
    data2=data.stack(data1)
    # print(data)
    print(data.subset(rows=[0,3,4],cols=['first_name']))
    # del data[1]
    # print(data.export('json'))
    # print(data.export('yaml'))
    # print(data.export('csv'))
    # with open('people.xls', 'wb') as f:
    #     f.write(data.export('xls'))
    #
    # with open('people.dbf', 'wb') as f:
    #     f.write(data.export('dbf'))
    #
    # print(data.export('df'))