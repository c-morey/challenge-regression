from utils.a_import_raw_data import raw_and_add_admin
import numpy as np


def preprocess():
    '''
    Basic preprocessing of the raw dataset:
    a) dropping rows without price or area
    b) dropping duplicates
    c) computing few new features
    :return:
    '''
    ds = raw_and_add_admin()
    print('Raw data has been merged with administrative info')
    print(ds.shape)

    ds.dropna(subset=['price', 'area'], inplace=True)
    print('Data after discarding row where prices or area are unavailable')
    print(ds.shape)

    # Keeping only last row for rows having same city, price, #rooms and area
    ds.drop_duplicates(['location', 'price', 'area', 'room_number'], keep='last', inplace=True, ignore_index=True)
    print('Data after dropping duplicates zip/price/area/bedrooms)')
    print(ds.shape)

    # price/square meter new feature
    ds['priceSqMeter'] = ds.price/ds.area
    print('Data with additional feature')
    print(ds.shape)

    return ds


'''
ds = preprocess()
print(ds.iloc[:, [8, 9, 26]].head(30).to_markdown())
ds.info()
'''