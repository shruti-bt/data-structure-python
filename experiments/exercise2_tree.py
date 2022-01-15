class TreeNode():
    def __init__(self, name):
        self.name = name
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

    def print_tree(self, level):
        if self.get_level() > level:
            return 
        space = ' ' * self.get_level() * 3
        prefix = space + "|__" if self.parent else ""
        print(prefix + self.name)
        if self.children:
            for child in self.children:
                child.print_tree(level)

def build_location_tree():
    root = TreeNode("Global")
    
    india = TreeNode("India")
    gujarat = TreeNode("Gujarat")
    gujarat.add_child(TreeNode("Ahmedabad"))
    gujarat.add_child(TreeNode("Baroda"))

    karnataka = TreeNode("Karnataka")
    karnataka.add_child(TreeNode("Bangluru"))
    karnataka.add_child(TreeNode("Mysore"))

    usa = TreeNode("USA")
    new_jersey = TreeNode("New Jersey")
    new_jersey.add_child(TreeNode("Princeton"))
    new_jersey.add_child(TreeNode("Trenton"))

    california = TreeNode("California")
    california.add_child(TreeNode("San Francisco"))
    california.add_child(TreeNode("Mountain View"))
    california.add_child(TreeNode("Palo Alto"))

    india.add_child(gujarat)
    india.add_child(karnataka)

    usa.add_child(new_jersey)
    usa.add_child(california)

    root.add_child(india)
    root.add_child(usa)

    return root

if __name__ == "__main__":
    root_node = build_location_tree()
    # root_node.print_tree(1)
    # root_node.print_tree(2)
    root_node.print_tree(3)
    pass




        
