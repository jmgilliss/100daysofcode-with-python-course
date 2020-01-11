from data import us_state_abbrev as usab
from data import states_list as slist


def load_stuff():
    print(usab)
    print(slist)
    return


def tenth_each():

    for key, value in enumerate(usab.items()):
        if key == 10:
            print(key, value)
        if key == 45:
            print(key)
        if key == 27:
            print(value[0])
    for item in enumerate(slist):
         pass
    return

def main():
    #load_stuff()
    tenth_each()


if __name__ == "__main__":
    main()
