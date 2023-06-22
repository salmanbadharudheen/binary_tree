from django.shortcuts import render, redirect

from .models import BinaryTree, Child, Node
from .forms import BinaryTreeForm, ChildForm


def create_account(request):
    binary_tree_form = BinaryTreeForm()
    child_form = ChildForm()

    if request.method == 'POST':
        binary_tree_form = BinaryTreeForm(request.POST)
        child_form = ChildForm(request.POST)
        # if binary_tree_form.is_valid() and child_form.is_valid():
        #     # Process the form data
        #     form.save()
        #     return redirect('indusapp:view_page')
        #     # pass
        if binary_tree_form.is_valid() and child_form.is_valid():
            binary_tree = binary_tree_form.save()  # Save the binary tree instance
            child = child_form.save(commit=False)
            child.parent_id = binary_tree
            child.save()
            return redirect('indusapp:view_page')
    #         if form.is_valid():
    #             form.save()
    #             return redirect('indusapp:view_page')
    context = {
        'binary_tree_form': binary_tree_form,
        'child_form': child_form
    }


    return render(request, 'create_account.html', context)





def build_tree(node):
    children = Child.objects.filter(parent_id=node)
    return {
        'id': node.id,
        'children': [build_tree(child) for child in children]
    }

def view_page(request):
    binary_trees = BinaryTree.objects.filter(parent_id__isnull=True)

    tree_data = [build_tree(root) for root in binary_trees]


    return render(request, 'view_page.html', {'tree_data': tree_data})

# def view_page(request):
#     binary_trees = BinaryTree.objects.filter(parent_id__isnull=True)
#
#     def build_tree(node):
#         children = node.children.all()
#         return {
#             'id': node.id,
#             'children': [build_tree(child) for child in children]
#         }
#
#     tree_data = [build_tree(root) for root in binary_trees]
#
#     return render(request, 'view_page.html', {'tree_data': tree_data})


    # return render(request, 'view_page.html', {'tree_data': tree_data})

#
# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.left = None
#         self.right = None
#
# class BinaryTree:
#     def __init__(self):
#         self.root = None
#
#     def insert(self, value):
#         if self.root is None:
#             self.root = Node(value)
#         else:
#             self._insert_recursive(self.root, value)
#
#     def _insert_recursive(self, node, value):
#         if value < node.value:
#             if node.left is None:
#                 node.left = Node(value)
#             else:
#                 self._insert_recursive(node.left, value)
#         else:
#             if node.right is None:
#                 node.right = Node(value)
#             else:
#                 self._insert_recursive(node.right, value)
#
#     def search(self, value):
#         return self._search_recursive(self.root, value)
#
#     def _search_recursive(self, node, value):
#         if node is None or node.value == value:
#             return node
#         elif value < node.value:
#             return self._search_recursive(node.left, value)
#         else:
#             return self._search_recursive(node.right, value)
#
#     def inorder_traversal(self):
#         self._inorder_recursive(self.root)
#
#     def _inorder_recursive(self, node):
#         if node is not None:
#             self._inorder_recursive(node.left)
#             print(node.value)
#             self._inorder_recursive(node.right)
#
# tree = BinaryTree()
# tree.insert(5)
# tree.insert(3)
# tree.insert(2)
# tree.insert(4)
# tree.insert(13)
# tree.insert(0)
# print(tree.search(4))


# tree.inorder_traversal()# Output: <__main__.Node object at 0x00000123ABCD1234>

#
# def create_account(request):
#     root_node = Node.objects.first()  # Assuming the first node is the root node
#
#     def traverse(node):
#         if node is None:
#             return None
#
#         return {
#             'value': node.value,
#             'left_child': traverse(node.left_child),
#             'right_child': traverse(node.right_child)
#         }
#
#     binary_tree = traverse(root_node)
#
#     return render(request, 'binary_tree.html', {'binary_tree': binary_tree})