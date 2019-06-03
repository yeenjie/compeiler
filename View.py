import tkinter as tk
from Thompson import *
from Draw import *
from NfaToDfa import *


def run():
    str_ = e.get()
    # graph = Graph()
    thom = Thompson(str_)
    g = thom.get_nfa()
    # nfa显示窗口
    nfa_win = tk.Tk("算法构造nfa")
    nfa_win.title("算法构造nfa")
    # nfa_win.geometry()
    t_nfa = tk.Text(nfa_win)
    for edge in g.edges:
        t_nfa.insert("end", edge.__str__())
        # t_nfa.insert("end","testts")
    t_nfa.pack()
    # nfa_win.mainloop()

    dfa_graph, chart = NfaToDfa(g).get_dfa()
    # 转移表
    tran_win = tk.Tk("转移表")
    tran_win.title("转移表")
    # nfa_win.geometry()
    t_chart = tk.Text(tran_win)
    t_chart.insert("end", chart)
    # t_nfa.insert("end","testts")
    t_chart.pack()

    # dfa显示窗口
    dfa_win = tk.Tk("nfa转dfa")
    dfa_win.title("nfa转dfa")
    # nfa_win.geometry()
    t_dfa = tk.Text(dfa_win)
    for edge in dfa_graph.edges:
        t_dfa.insert("end", edge.__str__())
        # t_nfa.insert("end","testts")
    t_dfa.pack()
    print(g)
    # draw(g)
    draw(dfa_graph)
    print(dfa_graph)


if __name__ == '__main__':
    # 界面
    window = tk.Tk()
    window.title('my window')
    # 窗口尺寸
    window.geometry('200x200')
    e = tk.Entry(window)
    e.pack()
    b1 = tk.Button(window, text="insert point", width=15, height=2, command=run)
    b1.pack()
    # 显示出来
    window.mainloop()
