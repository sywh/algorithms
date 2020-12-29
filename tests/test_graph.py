import sys

from Graph.Graph import Graph
from Graph.DepthFirstSearch import DepthFirstSearch
from Graph.DepthFirstPaths import DepthFirstPaths
from Graph.DepthFirstPaths import DepthFirstPathsIterative
from Graph.BreadthFirstPaths import BreadthFirstPaths
from Graph.CC import CC
from stdlib.StdIn import InStream


def test_graph():
    graph = Graph()
    instream = InStream()
    graph.from_stream(instream)
    print("V of graph: {}".format(graph.V()))  # V
    print("E of graph: {}".format(graph.E()))  # E
    print("graph:", graph)  # str


def test_depth_first_search():
    graph = Graph()
    instream = InStream(sys.argv[1])
    graph.from_stream(instream)
    s = int(sys.argv[2])

    search = DepthFirstSearch(graph, s)
    str_connect = ""
    for v in range(graph.V()):
        if search.marked(v):
            str_connect += str(v) + " "
    print(str_connect)

    if search.count() != graph.V():
        print("NOT connected")


def test_depth_first_path():
    graph = Graph()
    instream = InStream(sys.argv[1])
    graph.from_stream(instream)
    s = int(sys.argv[2])

    search = DepthFirstPaths(graph, s)
    for v in range(graph.V()):
        if search.hasPathTo(v):
            path = search.pathTo(v)
            path = [str(node) for node in path]
            print("V={}: ".format(str(v)), "-".join(path))


def test_depth_first_path_iterative():
    graph = Graph()
    instream = InStream(sys.argv[1])
    graph.from_stream(instream)
    s = int(sys.argv[2])

    search = DepthFirstPathsIterative(graph, s)
    for v in range(graph.V()):
        if search.hasPathTo(v):
            path = search.pathTo(v)
            path = [str(node) for node in path]
            print("V={}: ".format(str(v)), "-".join(path))


def test_breadth_first_path():
    graph = Graph()
    instream = InStream(sys.argv[1])
    graph.from_stream(instream)
    s = int(sys.argv[2])

    search = BreadthFirstPaths(graph, s)
    for v in range(graph.V()):
        if search.hasPathTo(v):
            path = search.pathTo(v)
            path = [str(node) for node in path]
            print("V={}".format(v), "-".join(path))


def test_cc():
    graph = Graph()
    instream = InStream(sys.argv[1])
    graph.from_stream(instream)

    search = CC(graph)
    count = search.count()
    print("{} components".format(count))
    for c in range(count):
        s = ""
        for v in range(graph.V()):
            if search.id(v) == c:
                s += str(v) + " "
        print(s)


if __name__ == "__main__":
    # test_graph()
    # test_depth_first_search()
    # test_depth_first_path()
    # test_depth_first_path_iterative()
    # test_breadth_first_path()
    test_cc()

