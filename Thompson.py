from Graph import *
from Edge import *
from Stack import *


def debug(teller):
    print(teller)


class Thompson:


    def __init__(self, str):
        self.stack = Stack()
        self.graph = Graph()
        self.add_endnode = False
        self.end_position = -1
        for c in str:
            if c != '(' and c != ')' and c != '|' and c != '*':
                if c in self.graph.characters:
                    pass
                else:
                    self.graph.characters.append(c)
            self.stack.push(c)
        if self.stack.front() == ')' and self.stack.front() == '*':
            self.add_endnode = True
        self.graph.get_new_state()

    def link(self, weight):
        node = self.graph.get_new_state()
        return Edge(node, node - 1, weight)

    def scan(self, begin):
        begin = begin
        connect_point = begin
        while bool(1 - self.stack.is_empty()):
            scaner = self.stack.front()
            self.stack.pop()
            if scaner == '|':
                # 保存目前分支状态
                save_state = self.graph.get_now_state()
                # 创建分支节点（结束点）
                end_node = self.graph.get_new_state()
                connect_point = end_node
                # debug("创建结束分支节点" + str(end_node))

                # 保存结束状态(整体)
                if self.add_endnode and self.end_position != -1:
                    self.end_position = end_node

                # 原分支结束连接分支结束点
                edge = Edge(begin, end_node, '@')
                self.graph.add_edge(edge)
                # 新分支开始节点
                node_new = self.graph.get_new_state()
                edge = Edge(node_new, end_node, '@')
                self.graph.add_edge(edge)
                # 进入分支
                self.scan(begin=end_node)
                # 结束分支
                end_node = self.graph.get_new_state()
                edge = Edge(end_node, end_node - 1, weight='@')
                self.graph.add_edge(edge)
                edge = Edge(end_node, save_state, weight='@')
                self.graph.add_edge(edge)

            elif scaner == '(':
                return connect_point
            elif scaner == ')':
                self.scan(connect_point)
                # pass
            elif scaner == '*':
                # 保存开始状态
                save_state = self.graph.get_now_state()

                # 保存结束状态(整体)
                if self.add_endnode and self.end_position != -1:
                    self.end_position = save_state
                # 内部连接
                if self.stack.front() == ')':
                    self.stack.pop()  # 在这里进入循环免得多进一次
                inner_end = self.scan(self.graph.get_new_state())  # (创建一个新的开始节点)
                # debug("得到的连接点" + str(inner_end))
                inner_begin = self.graph.get_now_state()  # 保存内部开始节点
                # 内部附加连接
                # edge = Edge(inner_end, inner_begin, weight="内部附加连接")
                edge = Edge(inner_end, inner_begin, weight="@")
                self.graph.add_edge(edge)
                # 内部节点连接结束节点
                # edge = Edge(inner_end, save_state, weight="内部节点连接结束节点")
                edge = Edge(inner_end, save_state, weight="@")
                self.graph.add_edge(edge)
                # 初始节点连接结束节点
                new_node = self.graph.get_new_state()
                edge = Edge(new_node, save_state, "@")
                # edge = Edge(new_node, save_state, "初始节点连接结束节点")
                self.graph.add_edge(edge)
                # 初始连接连接内部开始节点
                edge = Edge(new_node, inner_begin, "@")
                # edge = Edge(new_node, inner_begin, "初始连接连接内部开始节点")
                self.graph.add_edge(edge)
            else:
                edge = Edge(self.graph.get_new_state(), self.graph.get_now_state() - 1, scaner)
                self.graph.add_edge(edge)
        return connect_point

    def get_nfa(self):
        self.scan(0)
        # 添加开始状态
        first_node = self.graph.get_now_state()
        # edge = Edge(self.graph.get_new_state(), first_node, 's')
        # self.graph.add_edge(edge)
        self.graph.start_state = first_node
        # 需要的话添加结束状态
        # if self.add_endnode and self.end_position != -1:
        #     print("test")
        #     end_state = self.graph.get_new_state()
        #     edge = Edge(self.end_position, end_state, '@')
        #     self.graph.add_edge(edge)
        return self.graph
