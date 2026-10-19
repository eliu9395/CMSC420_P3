# AI Usage:
# Write details about how you used AI for this project.





#-----------------------------------------------------------------------------------------------
from __future__ import annotations
from typing import List
import math

# Node class.
# DO NOT MODIFY!

class Node():
    def  __init__(self,
                  keys     : List[int]  = None,
                  children : List[Node] = None,
                  parent   : Node = None):
        self.keys     = keys
        self.children = children
        self.parent   = parent

# Btree class.

class Btree():
    # DO NOT MODIFY!
    def  __init__(self,
                  m    : int  = None,
                  root : Node = None):
        self.m    = m
        self.root = root

    # DO NOT MODIFY!
    def customdump(self):
        def recurse(n,indent):
            print(f"{indent*' '}- keys = {n.keys}")
            if n.parent is not None:
                print(f"{indent*' '}  parent keys = {n.parent.keys}")
            if n.children is not None:
                print(f"{indent*' '}  children = ")
                for c in n.children:
                    recurse(c,indent+2)
            else:
                print(f"{indent*' '}  children = None")
        if self.root is not None:
            recurse(self.root,0)
        else:
            print("No Tree!")

    # Insert
    def insert(self, key: int):
        return

    # Delete
    def delete(self, key:int):
        return

    # Search
    def search(self,key) -> str:
        # What to return?
        return True

    # Draw a picture of the B-tree.
    # You will need to install graphviz to use this.
    # Add the line:
    # draw
    # in the tracefile.
    #
    # Full Disclosure!
    # I had claude write the initial version of this which I modified
    # because claude doesn't know what a b-tree really ought to look like.
    def draw_btree(self, filename='btree', fmt='png', port_width=0):
        if self.root == None:
            return
        try:
            from graphviz import Digraph
        except ImportError:
            graphviz = None
            return
        dot = Digraph()
        dot.attr('node', shape='plaintext', rankdir='TB')
        counter = [0]
        def add_node(node):
            node_id = f'node{counter[0]}'
            counter[0] += 1
            if node.children:
                cells = []
                for i, k in enumerate(node.keys):
                    cells.append(f'<TD PORT="p{i+1}">{k}</TD>')
                row = ''.join(cells)
                label = (
                    '<<TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0">'
                    f'<TR>{row}</TR></TABLE>>'
                )
            else:
                cells = ''.join(f'<TD>{k}</TD>' for k in node.keys)
                label = (
                    '<<TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0">'
                    f'<TR>{cells}</TR></TABLE>>'
                )
            dot.node(node_id, label=label)
            if node.children:
                for i, child in enumerate(node.children):
                    child_id = add_node(child)
                    if i == 0:
                        dot.edge(f'{node_id}:p{i+1}:sw',f'{child_id}:n')
                    else:
                        dot.edge(f'{node_id}:p{i}:se',f'{child_id}:n')

            return node_id
        add_node(self.root)
        dot.render(filename, format=fmt, cleanup=True)
        return f'{filename}.{fmt}'
