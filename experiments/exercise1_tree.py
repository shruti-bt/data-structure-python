# class TreeNode():
#     def __init__(self, data):
#         self.data = data
#         self.children = []
#         self.parent = None

#     def add_child(self, child):
#         child.parent = self
#         self.children.append(child)

#     def get_level(self):
#         level = 0
#         p = self.parent
#         while p:
#             level += 1
#             p = p.parent
#         return level

#     def print_tree(self):
#         spaces = ' ' * self.get_level() * 3
#         prefix = spaces + "|__" if self.parent else ""
#         print(prefix + self.data)
#         if len(self.children) > 0:
#             for child in self.children:
#                 child.print_tree()

# def build_management_tree():
#     root0 = TreeNode("Nilapul (CEO)")
#     chinmay = TreeNode("chinmay (CTO)")
#     vishal = TreeNode("Vishal (Infrastructure Head)")
#     vishal.add_child(TreeNode("Dhaval (Cloud Manager"))
#     vishal.add_child(TreeNode("Abhijit (App Manager"))
#     aamir = TreeNode("Aamir (Application Head)")
#     gels = TreeNode("Gels (HR Head)")
#     gels.add_child(TreeNode("Peter (Recuitment Manager)"))
#     gels.add_child(TreeNode("Waqas (Policy Manager)"))

#     root0.add_child(chinmay)
#     root0.add_child(gels)

#     chinmay.add_child(vishal)
#     chinmay.add_child(aamir)

#     return root0

# if __name__ == "__main__":
#     root0 = build_management_tree()
#     root0.print_tree()
#     pass

# class TreeNode():
#     def __init__(self, name, destination):
#         self.name = name
#         self.destination = destination
#         self.children = []
#         self.parent = None

#     def add_child(self, child):
#         child.parent = self
#         self.children.append(child)

#     def get_level(self):
#         level = 0
#         p = self.parent
#         while p:
#             level += 1
#             p = p.parent
#         return level

#     def print_tree(self, property_name):
#         if property_name == "both":
#             value = self.name + " (" + self.destination + ")"
#         elif property_name =="name":
#             value = self.name
#         else:
#             value = self.destination

#         spaces = ' ' * self.get_level() * 3
#         prefix = spaces + "|__" if self.parent else ""
#         print(prefix + value)
#         if self.children:
#             for child in self.children:
#                 child.print_tree(property_name)
        
# def build_management_tree():
    
#     infra_head = TreeNode("Vishal", "Infrastructure Head")
#     infra_head.add_child(TreeNode("Dhaval", "Cloud Manager"))
#     infra_head.add_child(TreeNode("Abhijit", "App Manager"))

#     hr_head = TreeNode("Gels", "HR Head")
#     hr_head.add_child(TreeNode("Peter", "Recuitment Manager"))
#     hr_head.add_child(TreeNode("Waqas", "Policy Manager"))

#     cto = TreeNode("Chinmay", "CTO")
#     cto.add_child(infra_head)
#     cto.add_child(TreeNode("Aamir", "Application Head"))

#     ceo = TreeNode("Nilupal", "CEO")
#     ceo.add_child(cto)
#     ceo.add_child(hr_head)

#     return ceo

# if __name__ == "__main__":
#     root_node = build_management_tree()
#     root_node.print_tree("name")
#     root_node.print_tree("designation")
#     root_node.print_tree("both")

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
        spaces = ' ' * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ""
        print(prefix + value)
        if self.children:
            for child in self.children:
                child.print_tree(property_name)
        
def build_management_tree():
    
    infra_head = TreeNode("Vishal", "Infrastructure Head")
    infra_head.add_child(TreeNode("Dhaval", "Cloud Manager"))
    infra_head.add_child(TreeNode("Abhijit", "App Manager"))

    hr_head = TreeNode("Gels", "HR Head")
    hr_head.add_child(TreeNode("Peter", "Recuitment Manager"))
    hr_head.add_child(TreeNode("Waqas", "Policy Manager"))

    cto = TreeNode("Chinmay", "CTO")
    cto.add_child(infra_head)
    cto.add_child(TreeNode("Aamir", "Application Head"))

    ceo = TreeNode("Nilupal", "CEO")
    ceo.add_child(cto)
    ceo.add_child(hr_head)

    return ceo

if __name__ == "__main__":
    root_node = build_management_tree()
    root_node.print_tree("name")
    root_node.print_tree("designation")
    root_node.print_tree("both")









