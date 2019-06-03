from Thompson import *
from Draw import *
from NfaToDfa import *

# stack = Stack()


# def link(weight):
#     node = graph.get_new_state()
#     return Edge(node, node - 1, weight)
#
#
# def scan(begin):
#     begin = begin
#     while bool(1 - stack.is_empty()):
#         scaner = stack.front()
#         stack.pop()
#         if scaner == '|':
#             # 获得分支节点
#             node = graph.get_new_state()
#             # 保存目前分支状态
#             save_state = node - 1
#             # 创建分支
#             edge = Edge(begin, node, '@')
#             graph.add_edge(edge)
#             node_new = graph.get_new_state()
#             edge = Edge(node_new, node, '@')
#             graph.add_edge(edge)
#             # 进入分支
#             scan(begin=node)
#             # 结束分支
#             end_node = graph.get_new_state()
#             edge = Edge(end_node, end_node - 1, weight='@')
#             graph.add_edge(edge)
#             edge = Edge(end_node, save_state, weight='@')
#             graph.add_edge(edge)
#         elif scaner == '(':
#             return begin
#         elif scaner == ')':
#             pass
#         elif scaner == '*':
#             # 保存开始状态
#             save_state = graph.get_now_state()
#             inner_end = graph.get_new_state()  # 内部结束节点
#             # 内部连接
#             scan(inner_end)
#             inner_begin = graph.get_now_state()  # 保存内部开始节点
#             # 内部附加连接
#             edge = Edge(inner_end, inner_begin, weight='内部附加连接')
#             graph.add_edge(edge)
#             # 内部节点连接结束节点
#             edge = Edge(inner_end, save_state, weight='结束节点连接内部')
#             graph.add_edge(edge)
#             # 初始节点连接结束节点
#             new_node = graph.get_new_state()
#             edge = Edge(new_node, save_state, "初始节点连接结束节点")
#             graph.add_edge(edge)
#             # 初始连接连接内部开始节点
#             edge = Edge(new_node, inner_begin, "初始连接连接内部开始节点")
#             graph.add_edge(edge)
#         else:
#             edge = link(scaner)
#             graph.add_edge(edge)
#
#     return begin


if __name__ == '__main__':

    str = input("请输入正规式：\n")

    # graph = Graph()
    thom = Thompson(str)
    g = thom.get_nfa()
    print(g)
    print(g.start_state)
    draw()
    dfa_graph = NfaToDfa(g).get_dfa()
    print(dfa_graph)
    # if stack.front() != '|' != '(' != ')':
    #     graph.get_new_state()
    # scan(0)
    # print(graph)



