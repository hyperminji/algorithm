"연결 리스트 자료구조"

class Node: #연결 리스트를 구성하는 단위 데이터의 모습은 데이터+다음 데이터
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
def init(): #연결리스트를 만든다. node1~node4 & 연결 포인터 구성
    global node1
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node1.next = node2
    node2.next = node3
    node3.next = node4    

def delete(del_data): # 구성된 리스트에서 데이터를 지우고 나머지를 연결한다
    global node1
    pre_node = node1
    next_node = pre_node.next

    if pre_node.data == del_data:
        node1 = next_node
        del pre_node
        return

    while next_node:
        if next_node.data == del_data:
            pre_node.next = next_node.next
            del next_node
            break
        pre_node = next_node
        next_node = next_node.next

def insert(ins_data): #연결리스트에 데이터를 추가한다.
    global node1
    new_node = Node(ins_data)
    new_node.next = node1
    node1 = new_node

def print_list(): #연결 리스트의 데이터를 출력한다.
    global node1
    node = node1
    while node:
        print(node.data)
        node = node.next
    print()

def LinkedList():
    init()
    delete(2)
    insert("9")
    print_list()


LinkedList()


"스택 자료구조[Last in First Out]"

def Stack():
    stack = []

    stack.append(1)
    stack.append(2)
    stack.append(3)
    stack.append(4)
    stack.append(5)
    print(stack)

    while stack:
        print("POP Value is  ", stack.pop())  #나중에 들어온 것부터 out
Stack()

"큐 자료구조[First in First out]/순환 큐(배열),링크트 큐(연결 리스트)"
def Queue():
    queue = []
    queue.append(1)
    queue.append(2)
    queue.append(3)
    queue.append(4)
    queue.append(5)
    print(queue)

    while queue:
        print("Get Value:", queue.pop(0))  #먼저 들어온 것 부터 out
Queue()

"데크(Deque)"
'''
리스트의 양쪽 끝에서 삽입과 삭제가 모두 이루어지는 자료구조
중간에 넣거나 빼는 것은 비허용
스택과 큐를 혼합한 구조
하나의 배열을 선언한 후 2개의 포인터로 양쪽 끝을 가리키고 
양쪽에서 삽입, 삭제 연산을 수행

종류
-입력 제한 데크(스크롤): 삽입이 한쪽에서 만 일어나는 데크
-출력 제한 데크(셀프): 삭제가 한쪽에서만 일어나는 데크

양쪽끝을 end1, end2
'''

"트리"
""":임의의 노드에서 다른 노드로의 경로가 하나 밖에 없는 것
Root Node(루트노드)와 Sub Node(하위노드) 가 연결된 비선형 계층 구조
"이진트리구조"
모든노트가 최대 2개의 자식 노드를 가질 수 있는 구조
"""
"이진트리를 만들고 데이터를 찾아 출력"

class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = self.right = None

class BinarySearchTree(object):
    def __init__(self):
        self.root = None

    def insert(self, data):
        self.root = self._insert_value(self.root, data)
        return self.root is not None
    
    def _insert_value(self, node, data):
        if node is None:
            node = Node(data)
        else:
            if data <= node.data:
                node.left = self._insert_value(node.left, data)
            else:
                node.right = self._insert_value(node.right, data)
        return node

    def find(self, key):
        return self._find_value(self.root, key)

    def _find_value(self, root, key):
        if root is None or root.data ==key:
            return root is not None
        elif key < root.data:
            return self._find_value(root.left, key)
        else:
            return self._find_value(root.right, key)
        
    def delete(self, key):
        self.root, deleted = self._delete_value(self.root, key)
        return deleted
    def _delete_value(self, node, key):
        if node is None:
            return node, False

        deleted= False
        if key == node.data:
            deleted = True
            if node.left and node.right:
                parent, child = node, node.right
                while child.left is not None:
                    parent, shild = child, child.left
                child.left = node.left
                if parent != node:
                    parent.left = child.right
                    child.right = node.right
                node = child
            elif node.left or node.right:
                node = node.left or node.right
            else:
                node = None
        elif key < node.data:
            node.left, deleted = self._delete_value(node.left, key)
        else:
            node.right, deleted = self._delete_value(node.right, key)
        return node, deleted

    def DFTravel(self):
        def _DFTravel(root):
            if root is None:
                pass
            else:
                print(root.data, end=' ')
                _DFTravel(root.left)
                _DFTravel(root.right)
        _DFTravel(self.root)
    
    def LFTravel(self):
        def _LFTravel(root):
            if root is None:
                pass
            else:
               _LFTravel(root.left)
               print(root.data, end=' ')
               _LFTravel(root.right)
        _LFTravel(self.root)

    def LRTravel(self):
        def _LRTravel(root):
            if root is None:
                pass
            else:
                _LRTravel(root.left)
                _LRTravel(root.right)
                print(root.data, end=' ')
        _LRTravel(self.root)

    def layerTravel(self):
        def _layerTravel(root):

            queue = [root]
            while queue :
                root = queue.pop(0)
                if root is not None:
                    print (root.data, end=' ')
                    if root.left:
                        queue.append(root.left)
                    if root.right:
                        queue.append(root.right)
        _layerTravel(self.root)



#데이터 선언
data = [20, 6, 8, 12, 78, 32, 65, 32, 7, 9]
tree = BinarySearchTree()

#트리 구조의 완성
for x in data:
    tree.insert(x)

#트리 안의 데이터 존재에 대한 확인 및 조작
print(tree.find(9))

print(tree.find(3))

print(tree.delete(78))
print(tree.delete(6))
print(tree.delete(11))

#트리 구조의 데이터 출력
print("\n@@@@@@@")
tree.DFTravel()  #전위순회(뿌왼오)
print("\n=====")
tree.LFTravel()  #중위순회(왼뿌오)
print("\n*****")
tree.LRTravel()  #후위순회(왼오뿌)
print("\n&&&&&")
tree.layerTravel() #너비 우선 탐색(뿌리부터 깊이순)


"힙(Heap)"
'''
이진 트리의 일종으로 여러 개의 값 중 가장 큰 값 또는 가장 작은 값을 빠르게 찾을 수 있도록 구성
'''

"그래프 자료구조"
'''
노드(정점) 에지(선)로 어떤 관계를 맺고 있는지 표현
[탐색방법]
깊이우선탐색(DFS: Depth First Search): 시작 정점에서 한 방향으로 갈 수 있는 가장 먼 경로까지 탐색, 다시 부모노드로 돌아와서 다른 방향 탐색
너비우선탐색(BFS: Breadth First Search): 시작 정점에서 인접한 모든 정점들을 우선 방문, 방문했던 정점들을 시작점으로 해서 차례로 방문하는 방법
[신장트리]
모든 정점을 포함하는 트리, 모든 정점이 연결, 사이클 포함 안함
[최소비용신장트리]
-Prim
-Kruskal
[최단경로]
-데이크스트라(Dijkstra)알고리즘
'''

