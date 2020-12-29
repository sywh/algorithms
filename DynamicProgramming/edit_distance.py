
class EditDistance:
    def __init__(self):
        pass

    def distance(self, word1, word2):
        count = [[0] * (len(word2) + 1)] * (len(word1) + 1)
        import ipdb; ipdb.set_trace()
        for i in range(1, len(word1) + 1):
            count[i][0] = i
        print(count)

        for j in range(1, len(word2) + 1):
            count[0][j] = j

