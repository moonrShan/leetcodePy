from typing import List


class TrieNode:
    def __init__(self):
        self.children = {}
        self.isFile = False
        self.content = ""

    def setChild(self, token):
        self.children[token] = TrieNode()


class FileSystem:

    def __init__(self):
        self.root = TrieNode()

    def ls(self, path: str) -> List[str]:
        cur = self.root
        for token in path.split('/'):
            if token: cur = cur.children[token]
        if cur.isFile:
            return path.split('/')[-1:]
        return sorted(cur.children.keys())

    def mkdir(self, path: str) -> None:
        cur = self.root
        for token in path.split('/'):
            if token:
                if not token in cur.children:
                    cur.setChild(token)
                cur = cur.children[token]

    def addContentToFile(self, filePath: str, content: str) -> None:
        cur = self.root
        for token in filePath.split('/'):
            if token:
                if not token in cur.children:
                    cur.setChild(token)
                cur = cur.children[token]
        cur.isFile = True
        cur.content += content

    def readContentFromFile(self, filePath: str) -> str:
        cur = self.root
        for token in filePath.split('/'):
            if token:
                if not token in cur.children:
                    cur.setChild(token)
                cur = cur.children[token]
        return cur.content

# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)