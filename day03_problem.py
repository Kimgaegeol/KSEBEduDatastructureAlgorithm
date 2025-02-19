class TreeNode:
	def __init__(self):
		self.left = None
		self.data = None
		self.right = None

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

def add(data, root):
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

def in_order(node):
    if node is None:
        return
    in_order(node.left)
    print(node.data, end='->')
    in_order(node.right)

if __name__ == '__main__':
	datas = [40,20,60,10,30,50,70,5,15,25,35,45,55,65,75]
	root = None

	node = TreeNode()
	node.data = datas[0]
	root = node
	make_tree(datas, root)
	in_order(root)
	print()
	add(80, root)
	in_order(root)
	print()
	delete(30,root)
	in_order(root)
	print()