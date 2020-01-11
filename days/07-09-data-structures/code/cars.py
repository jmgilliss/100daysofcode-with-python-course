cars = {
    'Ford': ['Falcon', 'Focus', 'Festiva', 'Fairlane'],
    'Holden': ['Commodore', 'Captiva', 'Barina', 'Trailblazer'],
    'Nissan': ['Maxima', 'Pulsar', '350Z', 'Navara'],
    'Honda': ['Civic', 'Accord', 'Odyssey', 'Jazz'],
    'Jeep': ['Grand Cherokee', 'Cherokee', 'Trailhawk', 'Trackhawk']
}


def get_all_jeeps(cars=cars):
    """return a comma  + space (', ') separated string of jeep models
       (original order)"""
    for key, value in cars.items():
        if key =='Jeep':
            value = (str(value))
            print(type(value), value)
            return value




def get_first_model_each_manufacturer(cars=cars):
    """return a list of matching models (original ordering)"""
    stuff = list()
    for key, value in cars.items():
        stuff.append(value[0])
    return stuff


def get_all_matching_models(cars=cars, grep='trail'):
    """return a list of all models containing the case insensitive
       'grep' string which defaults to 'trail' for this exercise,
       sort the resulting sequence alphabetically"""
    matches = ()
    for key, value in cars.items():
        if grep in value:
            matches.append(value)

    return matches


def sort_car_models(cars=cars):
    """return a copy of the cars dict with the car models (values)
       sorted alphabetically"""
    pass

get_all_jeeps()