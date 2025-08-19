import sys
sys.stdin = open('sample_input.txt')

def find_set(x):
    if parent[x] != x:
        