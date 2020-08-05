class Node:
    

    def __init__(self,left=None,right=None,val=None):
        self.left=left
        self.right=right
        self.val=val
    
    def toString(self):
        print(self.left,self.right,self.val)


class BST:
    def __init__(self):
        self.root=None
        self.count=0

    def insert(self,val,node):
        if not self.root:
            self.root=Node(val=val)
        else:
            if val<=node.val and node.left==None:
                node.left=Node(val=val)
            elif val>node.val and node.right==None:
                node.right=Node(val=val)
            else:
                if val<=node.val:
                    self.insert(val,node.left)
                elif val>node.val:
                    self.insert(val,node.right)
                
                
    def inOrder(self,node):
        if node:
            self.inOrder(node.left)
            print(node.val)
            self.inOrder(node.right)

    def preOrder(self,node):
        if node:
            print(node.val)
            self.preOrder(node.left)
            self.preOrder(node.right)

    def search(self,val,node):
        if node:
            if val==node.val:
                return True,node
            elif val<node.val:
                return self.search(val,node.left)
            elif val>node.val:
                return self.search(val,node.right)
        return False,None
    
    def update(self,val,val2,node):
        if node:
            if val==node.val:
                node.val=val2
            elif val<node.val:
                self.update(val,val2,node.left)
            elif val>node.val:
                self.update(val,val2,node.right)

    def go_to_end(self,node):
        if node.right:
            while True:
                if node.right.right:
                    node=node.right
                    self.count+=1
                else:
                    break
        return node

    def deletion(self,val,node):
        search,node=self.search(val,node)
        if search:
            returned_node=self.go_to_end(node.left)
            if self.count==0:
                node.val=returned_node.val
                node.left=None
            elif self.count>0:
                node.val=returned_node.right.val
                returned_node.right=None

            


if __name__ == "__main__":
    obj=BST()
    obj.insert(5,obj.root)
    obj.insert(4,obj.root)
    obj.insert(3,obj.root)
    obj.insert(30,obj.root)
    obj.insert(20,obj.root)
    obj.insert(22,obj.root)
    obj.insert(24,obj.root)
    obj.insert(34,obj.root)
    obj.preOrder(obj.root)
    search,_=obj.search(1,obj.root)
    obj.deletion(30,obj.root)
    obj.preOrder(obj.root)


