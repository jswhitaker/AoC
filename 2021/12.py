import copy
import itertools
from dataclasses import dataclass
from functools import cache
from typing import List, Dict, Set, Optional
import hashlib
import json

import parse


@dataclass
class Node(object):
    name: str
    connected: Set[str]

    def __hash__(self):
        return hash(self.name)


@dataclass
class Graph(object):
    nodes: Dict[str, Node]

    def __hash__(self):
        return 1

    @cache
    def find_path(self, start: str, end: str, visited: frozenset[str] = frozenset(),
                  allow_small_twice: bool = False) -> List[List[str]]:
        paths = []
        if start == end:
            paths.append([end])
        next_nodes = [c for c in self.nodes[start].connected if c not in visited]
        if len(next_nodes) > 0:
            for n in next_nodes:
                new_visited = set(visited)
                next_paths = []
                if start.islower():
                    new_visited.add(start)
                next_paths.extend(self.find_path(n, end, frozenset(new_visited), allow_small_twice))
                if start.islower() and (start not in ['start', 'end']) and allow_small_twice:
                    next_paths.extend(self.find_path(n, end, visited, False))
                if len(next_paths) > 0:
                    paths.extend([[start] + p for p in next_paths])
        uniq_paths = []
        [uniq_paths.append(p) for p in paths if p not in uniq_paths]
        return paths

    def task_1(self):
        return self.find_path('start', 'end', frozenset())

    def task_2(self):
        return self.find_path('start', 'end', allow_small_twice=True)


def main():
    rows = []
    graph = Graph({})
    with open('inputs/12.txt') as input_file:
        for line in input_file:
            parsed = parse.parse("{}-{}", line.strip())
            node_1_name = parsed[0]
            node_2_name = parsed[1]
            node_1 = graph.nodes.get(node_1_name)
            node_2 = graph.nodes.get(node_2_name)
            if node_1 is None:
                node_1 = Node(node_1_name, set())
                graph.nodes[node_1_name] = node_1
            node_1.connected.add(node_2_name)
            if node_2 is None:
                node_2 = Node(node_2_name, set())
                graph.nodes[node_2_name] = node_2
            node_2.connected.add(node_1_name)
    return graph.task_2()


if __name__ == '__main__':
    result = main()
    for x in result:
        print(x)
    print('Task 1: ' + str(len(result)))
