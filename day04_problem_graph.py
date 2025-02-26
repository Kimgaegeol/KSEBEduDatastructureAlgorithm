from collections import deque

class Graph:
	def __init__(self, size) :
		self.SIZE = size
		self.graph = [[0 for _ in range(size)] for _ in range(size)]


def print_graph(g) :
    print(' ', end = ' ')
    for v in range(g.SIZE) :
        print(name_ary[v], end =' ')
    print()
    for row in range(g.SIZE) :
        print(name_ary[row], end =' ')
        for col in range(g.SIZE) :
            #print("%2d" % g.graph[row][col], end = ' ')
            print(f"{g.graph[row][col]:2}", end=' ')
        print()
    print()

def bfs(g, current, find_vtx, visited):
    if current == find_vtx:
        return True
    queue = deque([current])
    visited.append(current)
    while queue:
        current = queue.popleft()
        for vertex in range(g.SIZE):
            if g.graph[current][vertex] != 0 and vertex not in visited:
                if vertex == find_vtx:
                    return True
                queue.append(vertex)
                visited.append(vertex)
    return False

def dfs(g, current, find_vtx, visited):
    if current == find_vtx:
        return True
    visited.append(current)
    for vertex in range(g.SIZE):
        if g.graph[current][vertex] != 0 and vertex not in visited:
            if dfs(g, vertex, find_vtx, visited):
                return True
    return False

def find_vertex(g, find_vtx) -> bool:
    visited = []
    return bfs(g, 0, find_vtx, visited)

def make_edge_ary(g) -> list: # 간선 목록 만들기 [가중치, 시작도시, 도착도시]
    edge_ary = []
    for i in range(g.SIZE) :
        for k in range(g.SIZE) :
            if g.graph[i][k] != 0 :
                edge_ary.append([g.graph[i][k], i, k])

    edge_ary.sort(reverse=True)
    return edge_ary

def duplicate_remove_edge_ary(edge_ary) -> list:# 중복 간선 제거
    new_ary = []
    for i in range(0, len(edge_ary), 2) :
        new_ary.append(edge_ary[i])
    return new_ary

def final_edge_ary(new_ary, g) -> list:
    index = 0
    while len(new_ary) > g.SIZE - 1:	# 간선의 개수가 '정점 개수-1'일 때까지 반복
        start = new_ary[index][1]
        end = new_ary[index][2]
        saveCost = new_ary[index][0]

        g.graph[start][end] = 0
        g.graph[end][start] = 0

        startYN = find_vertex(g, start)
        endYN = find_vertex(g, end)

        if startYN and endYN :
            del new_ary[index]
        else :
            g.graph[start][end] = saveCost
            g.graph[end][start] = saveCost
            index += 1
    return new_ary

if __name__ == '__main__':
    G1 = None
    name_ary = ['춘천', '서울', '속초', '대전', '광주', '부산']
    춘천, 서울, 속초, 대전, 광주, 부산 = 0, 1, 2, 3, 4, 5

    g_size = 6
    G1 = Graph(g_size)

    G1.graph[춘천][서울] = 10;
    G1.graph[춘천][속초] = 15;
    G1.graph[서울][춘천] = 10;
    G1.graph[서울][속초] = 40;
    G1.graph[서울][대전] = 11;
    G1.graph[서울][광주] = 50;
    G1.graph[속초][춘천] = 15;
    G1.graph[속초][서울] = 40;
    G1.graph[속초][대전] = 12;
    G1.graph[대전][서울] = 11;
    G1.graph[대전][속초] = 12;
    G1.graph[대전][광주] = 20;
    G1.graph[대전][부산] = 30;
    G1.graph[광주][서울] = 50;
    G1.graph[광주][대전] = 20;
    G1.graph[광주][부산] = 25;
    G1.graph[부산][대전] = 30;
    G1.graph[부산][광주] = 25;

    edge_ary = make_edge_ary(G1)
    edge_ary = duplicate_remove_edge_ary(edge_ary)
    edge_ary = final_edge_ary(edge_ary, G1)

    print_graph(G1)