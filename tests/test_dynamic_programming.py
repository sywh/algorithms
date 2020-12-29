
from DynamicProgramming.edit_distance import EditDistance

def test_edit_distance():
    edit_distance = EditDistance()
    edit_distance.distance("horse", "ros")


if __name__ == "__main__":
    test_edit_distance()