from Graph import *


def get_set_brand(s):
    l = []
    for i in s:
        l.append(i)
    l.sort()
    re_str = ""
    for i in l:
        re_str += str(i)
    return re_str


def debug(states, inc):
    print("====================" + inc)
    for i in states.items():
        print(i)
        print(" ")


class NfaToDfa:

    def __init__(self, graph):
        self.graph = graph
        self.dfa_graph = Graph()
        self.new_states = {}
        self.new_edges = []
        self.edges = self.graph.edges
        self.inputs = self.graph.characters
        self.new_state_label = 'A'

    def make_edges(self, now_states, inc):
        debug(self.new_states, inc)
        new_state = set()
        # c-closure(move(now,new),inc)
        for i_state in now_states:
            for edge in self.edges:
                if edge.begin == i_state and edge.weight == inc:
                    new_state.add(edge.end)

        l_new_state = list(new_state)
        # c-closure(空)
        for i_state in l_new_state:
            for edge in self.edges:
                if edge.begin == i_state and edge.weight == '@':
                    if edge.end in l_new_state:
                        new_state.add(edge.end)
                    else:
                        l_new_state.append(edge.end)

        if len(new_state) != 0:
            try:
                self.new_states[get_set_brand(new_state)]
                self.new_edges.append(
                    Edge(self.new_states[get_set_brand(now_states)], self.new_states[get_set_brand(new_state)],
                         weight=inc))
            except KeyError:
                self.new_states[get_set_brand(new_state)] = self.new_state_label
                self.new_state_label = chr(ord(self.new_state_label) + 1)
                self.new_edges.append(
                    Edge(self.new_states[get_set_brand(now_states)], self.new_states[get_set_brand(new_state)],
                         weight=inc))
                for inc in self.graph.characters:
                    self.make_edges(new_state, inc)

    def get_dfa(self):
        # c-closure(空)
        begin_state = set()
        begin_state.add(self.graph.start_state)
        for edge in self.edges:
            if edge.begin == self.graph.start_state and edge.weight == '@':
                begin_state.add(edge.end)
        self.new_states[get_set_brand(begin_state)] = self.new_state_label
        self.dfa_graph.start_state = self.new_states[get_set_brand(begin_state)]
        self.new_state_label = chr(ord(self.new_state_label) + 1)
        for inc in self.graph.characters:
            self.make_edges(begin_state, inc)
        for new_edge in self.new_edges:
            self.dfa_graph.add_edge(new_edge)
        return self.dfa_graph
