from django import forms
from .models import BinaryTree, Child


# class BinaryTreeForm(forms.ModelForm):
#     class Meta:
#         model = BinaryTree
#         fields = ['id', 'parent_id','child']


class BinaryTreeForm(forms.ModelForm):
    class Meta:
        model = BinaryTree
        fields = ['id', 'parent_id']

class ChildForm(forms.ModelForm):
    class Meta:
        model = Child
        fields = ['child']