class TreeNode:
	def __init__(self):
		self.left = None
		self.data = None
		self.right = None

def make_tree(groups, root):
	for groups in groups[1:]:
		node = TreeNode()
		node.data = groups
		current = root
		while True:
			if groups < current.data:
				if current.left is None:
					current.left = node
					break
				current = current.left
			else:
				if current.right is None:
					current.right = node
					break
				current = current.right

	print("BST 구성 완료")

def search_group(find_group, root):
	current = root
	while True:
		if find_group == current.data:
			print(f"{find_group}을(를) 찾았습니다.")
			break
		elif find_group < current.data:
			if current.left is None:
				print(f"{find_group}이(가) 존재하지 않습니다.")
				break
			current = current.left
		else:
			if current.right is None:
				print(f"{find_group}이(가) 존재하지 않습니다.")
				break
			current = current.right

def delete_group(deleteName, root):
	current = root
	parent = None
	while True:
		if deleteName == current.data:
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
				current.data = search_change_node(current, current.right)
			break
		elif deleteName < current.data:
			if current.left is None:
				print(f"{deleteName}이(가) 트리에 없음")
				break
			parent = current
			current = current.left
		else:
			if current.right is None:
				print(f"{deleteName}이(가) 트리에 없음")
				break
			parent = current
			current = current.right

def search_change_node(parent, current):
	if current.left is None:
		data = current.data
		delete_group(current.data, parent)
		return data
	else:
		return search_change_node(current, current.left)

def in_order(node):
    if node is None:
        return
    in_order(node.left)
    print(node.data, end='->')
    in_order(node.right)

if __name__ == '__main__':
	groups = [40,20,60,10,30,50,70,5,15,25,35,45,55,65,75]
	root = None

	node = TreeNode()
	node.data = groups[0]
	root = node

	make_tree(groups,root)

	delete_group(30,root)
	in_order(root)

