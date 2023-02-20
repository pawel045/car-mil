import json
import pickle
import numpy as np

__brands = []
__engines = None
__data_columns = None
__model = None


def get_prediction(brand: str, prod_year: int, engine: str, transmission: int, engine_cap: float):
    # transmission -> 0 - mechanical, 1 - automatic

    try:
        brand_index = __data_columns.index(brand.lower())

    except:
        brand_index = -1

    x = np.zeros(len(__data_columns))

    x[0] = prod_year
    x[1] = 1 if engine == 'Diesel' else 0
    x[2] = transmission
    x[3] = engine_cap

    if brand_index >= 5:
        x[brand_index] = 1

    return round(__model.predict([x])[0])


def get_brands():
    return __brands


def get_engines():
    return __engines


def load_saved_components():
    print('loading components')
    global __data_columns
    global __brands
    global __engines
    global __model

    # check directory
    with open('./components/values.json', 'r') as f:
        __engines = json.load(f)['engines']

    with open('./components/columns.json', 'r') as f:
        columns = json.load(f)['data_columns']
        __data_columns = columns
        lower_brand = columns[4:]

        for brand in lower_brand:
            __brands.append(brand.title())

    with open('./components/cars.pickle', 'rb') as f:
        __model = pickle.load(f)

    print('loading complete')


if __name__ == '__main__':
    load_saved_components()
    print(get_brands())
    print(get_prediction('acura', 2015, 'Diesel', 1, 1.6))