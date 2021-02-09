from stdlib import stdio

from Graph.BreadthFirstPaths import BreadthFirstPaths
from Graph.SymbolGraph import SymbolGraph


def degreeOfSeparation(args):
    sg = SymbolGraph(args[0], args[1])

    g = sg.G()
    source = args[2]
    if not sg.contains(source):
        print(source, "not in database")
        return

    s = sg.index(source)
    bfs = BreadthFirstPaths(g, s)

    while not stdio.isEmpty():
        sink = stdio.readLine()
        if sg.contains(sink):
            t = sg.index(sink)
            if bfs.hasPathTo(t):
                for v in bfs.pathTo(t):
                    print("   " + sg.name(v))
            else:
                print("Not connected")
        else:
            print("Not in database")
