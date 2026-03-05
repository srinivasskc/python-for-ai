# Exercise 1: Build an adjacency list for friendships.
"""
A: B,C
B: A,D
C: A,D,E
D: B,C
E: C,F
F: E
"""

# Empty dictionary - GRAPH
graph = {}

# Function to make sure each person has an entry in the dictionary


def add_person(graph, person):
    if person not in graph:
        graph[person] = set()


# Adds friends between two people.


def add_friendship(graph, p1, p2):
    add_person(graph, p1)
    add_person(graph, p2)
    graph[p1].add(p2)
    graph[p2].add(p1)


# Build graph with add_friendship
print(graph)
add_friendship(graph, "A", "B")
add_friendship(graph, "A", "C")
add_friendship(graph, "B", "A")
add_friendship(graph, "B", "D")
add_friendship(graph, "C", "A")
add_friendship(graph, "C", "D")
add_friendship(graph, "C", "E")
add_friendship(graph, "D", "B")
add_friendship(graph, "D", "C")
add_friendship(graph, "E", "C")
add_friendship(graph, "E", "F")
add_friendship(graph, "F", "E")
print(graph)


# Pretty Print
# print(graph.keys())
# print(type(graph.keys()))  # Dict

# print(sorted(graph.keys()))
# print(type(sorted(graph.keys())))  # List

print("\n Pretty Printing.....\n")

for person in sorted(graph.keys()):
    print(f"{person}: {sorted(graph[person])}")

    # print(type(graph[person]))
    # print(type(sorted(graph[person])))


# Assertions

assert graph["A"] == {"B", "C"}
assert graph["B"] == {"A", "D"}
assert graph["C"] == {"A", "D", "E"}
assert graph["D"] == {"B", "C"}
assert graph["E"] == {"C", "F"}
assert graph["F"] == {"E"}
print("\n Assertions: All Checks Passed!!")
