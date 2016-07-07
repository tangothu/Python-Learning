# # # # -*- coding: utf-8 -*-
# Note: need to switch project interpreter to anaconda python 2.7.11
import pandas as pd
from pandas import Series, DataFrame

if __name__ == '__main__':
    # Series is a one dimensional labeled array capable of holding any data type (integer,string,python objects, etc.)
    obj = pd.Series([4, 7, -5, 3],index=[25,'b','c','d'])
    print obj
    # Series is dict-like where one can get and set values by index label
    print obj['b']

    data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada'],
        'year': [2000, 2001, 2002, 2001, 2002],
        'pop': [1.5, 1.7, 3.6, 2.4, 2.9]}
    # DataFrame is a d-D labeled tabular like data structure with columns
    frame = DataFrame(data)
    print frame
    print DataFrame(data, columns=['year', 'state', 'pop'])
    print frame.columns
    print frame['year'][0]
    # print frame[0]['year'] -- this is invalid!

    print frame.ix[0] # This is fine, to locate data by row (index)
    del frame['state']
    print frame

