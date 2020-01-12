from itertools import chain

cars = {
    'Ford': ['Falcon', 'Focus', 'Festiva', 'Fairlane'],
    'Holden': ['Commodore', 'Captiva', 'Barina', 'Trailblazer'],
    'Nissan': ['Maxima', 'Pulsar', '350Z', 'Navara'],
    'Honda': ['Civic', 'Accord', 'Odyssey', 'Jazz'],
    'Jeep': ['Grand Cherokee', 'Cherokee', 'Trailhawk', 'Trackhawk']
}


def get_all_jeeps():
    """return a comma  + space (', ') separated string of jeep models
       (original order)"""
    print(', '.join(cars['Jeep']))
    return ', '.join(cars['Jeep'])


def get_first_model_each_manufacturer():
    """return a list of matching models (original ordering)"""
    print([models[0] for models in cars.values()])
    return [models[0] for models in cars.values()]


def get_all_matching_models(cars, grep='trail'):
    """return a list of all models containing the case insensitive
       'grep' string which defaults to 'trail' for this exercise,
       sort the resulting sequence alphabetically"""
    grep = grep.lower()
    # flatten list of lists (less obvious way: "sum(cars.values(), [])")
    models = list(chain.from_iterable(cars.values()))
    matching_models = [model for model in models
                       if grep in model.lower()]
    print(sorted(matching_models))
    return sorted(matching_models)


def sort_car_models():
    """return a copy of the cars dict with the car models (values)
       sorted alphabetically"""
    print({manufacturer: sorted(models) for
            manufacturer, models in cars.items()})
    return {manufacturer: sorted(models) for
            manufacturer, models in cars.items()}
def main():
    get_all_jeeps()
    get_first_model_each_manufacturer()
    get_first_model_each_manufacturer()
    sort_car_models()

if __name__ == "__main__":
    main()
