class Edge:

    def __init__(self, begin, end, weight):
        self.begin = begin
        self.end = end
        self.weight = weight

    def __str__(self):
        return "" + str(self.begin) + "-- " + self.weight + " -->" + str(self.end) + "\n"
