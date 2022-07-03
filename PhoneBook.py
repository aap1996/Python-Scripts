class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False
        self.number = ""

class Trie:
    def __init__(self):
        self.root = TrieNode()



    def insert(self, name, number):
        node = self.root

        for char in name:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        
        node.end = True
        node.number = number


    def search(self,name):

        node = self.root

        for char in name:
            if char not in node.children:
                return False
            node = node.children[char]
        
        return node.end


    def __printcontacts(self,node, name):

        if not node:
            return
        
        if node.end:
            print(name, node.number)

        
        for char in node.children.keys():
                temp = node.children[char]
                self.__printcontacts(temp,name + char)

    def display(self, prefix):

        node = self.root
        for char in prefix:
            if char not in node.children:
                print("No contacts found")
                return
            node = node.children[char]

        if node:
            for char in node.children.keys():
                temp = node.children[char]
                self.__printcontacts(temp,prefix + char)







phoneBook = Trie()
phoneBook.insert("Anuj","712345")
phoneBook.insert("Anuja","123123")
phoneBook.insert("Raj","6213123")
phoneBook.insert("Rajesk","90909090")

phoneBook.display("An")



