from django.db import models

# Create your models here.
from django.db import models


class BinaryTree(models.Model):
    id = models.AutoField(primary_key=True)
    parent_id = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)



    def __str__(self):
        return str(self.id)

class Child(models.Model):
    child = models.CharField(max_length=255,null=True,blank=True)
    parent_id = models.ForeignKey(BinaryTree, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)



class Node(models.Model):
    value = models.IntegerField()
    left_child = models.ForeignKey('self', related_name='left_child_node', null=True, blank=True, on_delete=models.CASCADE)
    right_child = models.ForeignKey('self', related_name='right_child_node', null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.value)

