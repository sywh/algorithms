
import sys
from Fundamentals.Bag import Bag

def test_bag():
    for line in sys.stdin:
        bag = Bag()
        for item in line.split():
            bag.add(item)  # add
        print("size of bag: {}".format(bag.size()))  # size
        print("items:")
        for item in bag:  # iterator
            print(item)
            import ipdb; ipdb.set_trace()
        print("bag:", bag)  # str


if __name__ == '__main__':
    test_bag()

