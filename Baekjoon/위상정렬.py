from collections import deque

v, e = map(int, input().split())  #노드 간선 개수 

indegree = [0] * (v+1) #모든 노드에 대한 진입차수는 0으로 초기화
graph = [[] for _ in range(v+1)] #각 노드에 연결된 간선 정보를 담기 위한 연결리스트 초기화

# 방향 그래프의 모든 간선 정보를 입력받기
for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b) # 정점 A에서 B로 이동가능
    indegree[b] += 1 # 진입 차수를 1 증가

# 위상 정렬 함수
def topology_sort():
    result = []
    q = deque() #처음 시작할 때 진입차수가 0인 노드를 큐에 삽입

    for i in range(1, v+1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        result.append(now)

        for i in graph[now]:   #해당 원소와 연결된 노드들의 진입차수에서 1빼기
            indegree[i] -= 1

            # 새롭게 진입차수가 0이 되는 노드를 쿠에 삽입
            if indegree[i] == 0:
                q.append(i)

    #위상 ㅈ어렬 수행한 결과 출력
    for i in result:
        print(i, end=' ')

topology_sort()