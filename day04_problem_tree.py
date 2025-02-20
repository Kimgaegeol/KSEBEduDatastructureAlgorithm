# v4.4) v4.3 버전의 출력 방식을 너비 우선 탐색으로 수정하시오.
# tree에 너비우선탐색을 적용시키자
from collections import deque

class TreeNode:
	def __init__(self):
		self.left = None
		self.data = None
		self.right = None

def bfs(root):
	print(root.data, end='->')
	queue = deque([root])
	while queue:
		node = queue.popleft()
		if node.left is None and node.right is None:
			pass
		elif node.left is not None and node.right is None:
			print(node.left.data, end='->')
			queue.append(node.left)
		elif node.left is None and node.right is not None:
			print(node.right.data, end='->')
			queue.append(node.right)
		else:
			print(node.left.data, end='->')
			print(node.right.data, end='->')
			queue.append(node.left)
			queue.append(node.right)

def make_tree(datas, root):
	for data in datas[1:]:
		node = TreeNode()
		node.data = data
		current = root
		while True:
			if data < current.data:
				if current.left is None:
					current.left = node
					break
				current = current.left
			else:
				if current.right is None:
					current.right = node
					break
				current = current.right

def insert(data, root):
    node = TreeNode()
    node.data = data
    current = root
    while True:
        if data < current.data:
            if current.left is None:
                current.left = node
                break
            current = current.left
        else:
            if current.right is None:
                current.right = node
                break
            current = current.right

def search(data, root):
	current = root
	while True:
		if data == current.data:
			print(f"{data}을(를) 찾았습니다.")
			break
		elif data < current.data:
			if current.left is None:
				print(f"{data}이(가) 존재하지 않습니다.")
				break
			current = current.left
		else:
			if current.right is None:
				print(f"{data}이(가) 존재하지 않습니다.")
				break
			current = current.right

def delete(data, root):
	current = root
	parent = None
	while True:
		if data == current.data:
			if current.left is None and current.right is None:
				if parent.left == current:
					parent.left = None
				else:
					parent.right = None
				del (current)
			elif current.left is not None and current.right is None:
				if parent.left == current:
					parent.left = current.left
				else:
					parent.right = current.left
			elif current.left is None and current.right is not None:
				if parent.left == current:
					parent.left = current.right
				else:
					parent.right = current.right
			else: #자식이 두 개 있는 경우
				current.data = search_delete_node(current, current.right)
			break
		elif data < current.data:
			if current.left is None:
				print(f"{data}이(가) 트리에 없음")
				break
			parent = current
			current = current.left
		else:
			if current.right is None:
				print(f"{data}이(가) 트리에 없음")
				break
			parent = current
			current = current.right
def search_delete_node(parent, current):
    if current.left is None:
        data = current.data
        delete(current.data, parent)
        return data
    else:
        return search_delete_node(current, current.left)



if __name__ == '__main__':
	datas = [40,20,60,10,30,50,70,5,15,25,35,45,55,65,75]
	root = None

	node = TreeNode()
	node.data = datas[0]
	root = node
	make_tree(datas, root)

	insert(3,root)
	insert(7,root)
	insert(13,root)
	insert(17,root)
	insert(23,root)
	insert(27,root)
	insert(33,root)
	insert(37,root)
	insert(43,root)
	insert(47,root)
	insert(53,root)
	insert(57,root)
	insert(63,root)
	insert(67,root)
	insert(73,root)
	insert(77,root)

	bfs(root)

