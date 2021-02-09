import sys

from Graph.BreadthFirstPaths import BreadthFirstPaths
from Graph.CC import CC
from Graph.Cycle import Cycle
from Graph.DegreeOfSeparation import degreeOfSeparation
from Graph.DepthFirstPaths import DepthFirstPaths, DepthFirstPathsIterative
from Graph.DepthFirstSearch import DepthFirstSearch
from Graph.EdgeWeightedGraph import EdgeWeightedGraph
from Graph.Graph import Graph
from Graph.LazyPrimMST import LazyPrimMST
from Graph.PrimMST import PrimMST
from Graph.SymbolGraph import SymbolGraph
from Graph.TwoColor import TwoColor
from stdlib import stdio
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


def test_cycle():
    graph = Graph()
    instream = InStream(sys.argv[1])
    graph.from_stream(instream)

    cycle = Cycle(graph)
    print("graph", graph)
    print("graph hasCycle is {}".format(cycle.hasCycle()))


def test_twoColor():
    graph = Graph()
    instream = InStream(sys.argv[1])
    graph.from_stream(instream)

    color = TwoColor(graph)
    print("graph", graph)
    print("graph isTwoColorable is {}".format(color.isBipartite()))


def test_symbolGraph():
    filename = sys.argv[1]
    delim = sys.argv[2]
    sg = SymbolGraph(filename, delim)
    G = sg.G()

    while stdio.hasNextLine():
        source = stdio.readLine()
        for w in G.adj(sg.index(source)):
            print("   " + sg.name(w))


def test_degreeOfSeparation():
    degreeOfSeparation(sys.argv[1:])


def test_mst():
    graph = EdgeWeightedGraph()
    inStream = InStream(sys.argv[1])
    graph.from_stream(inStream)

    # mst = LazyPrimMST(graph)
    mst = PrimMST(graph)
    for e in mst.edges():
        print(e)
    print(mst.weight())


if __name__ == "__main__":
    # test_graph()
    # test_depth_first_search()
    # test_depth_first_path()
    # test_depth_first_path_iterative()
    # test_breadth_first_path()
    # test_cc()
    # test_cycle()
    # test_twoColor()
    # test_symbolGraph()
    test_degreeOfSeparation()
    # test_mst()
