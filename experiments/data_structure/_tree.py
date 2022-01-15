class TreeNode():
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self #-------------------parent treenode
        self.children.append(child)

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

    def print_tree(self):
        spaces = ' ' * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ""
        print(prefix + self.data)
        if len(self.children) > 0:
            for child in self.children:
                child.print_tree()

def build_product_tree():
    root = TreeNode("Electronics")

    laptop = TreeNode("laptops")
    laptop.add_child(TreeNode("macbook"))
    laptop.add_child(TreeNode("microsoft"))
    laptop.add_child(TreeNode("Thinkpad"))

    cellphone = TreeNode("cellphones")
    cellphone.add_child(TreeNode("iphone"))
    cellphone.add_child(TreeNode("Google"))
    cellphone.add_child(TreeNode("vivo"))

    television = TreeNode("televisions")
    television.add_child(TreeNode("thomson"))
    television.add_child(TreeNode("LG"))
    television.add_child(TreeNode("sumsung"))

    root.add_child(laptop)
    root.add_child(cellphone)
    root.add_child(television)

    return root

if __name__ == "__main__":
    root = build_product_tree()
    root.print_tree()
    pass