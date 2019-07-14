class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        def prefix_tree(words):
            root={}
            for word in words:
                node=root
                for w in word:
                    if w not in node:
                        node[w]={}
                    node=node[w]
            return root
        
        def search_tree(board, pt):
            h=len(board)
            w=len(board[0])
            
            finded=[[False for i in range(w)] for j in range(h)]
            root=dict()
            
            for i in range(h):
                for j in range(w):
                    dfs(board, finded, (i, j), root, pt)
            return root
        
        def dfs(board, finded, idx, node, pt):
            y,x=idx
            h=len(board)
            w=len(board[0])
            c=board[y][x]
            if c not in pt:
                return
            if finded[y][x]==False:
                if c not in node:
                    node[c]=dict()
                finded[y][x]=True
                if y<h-1:
                    dfs(board, finded, (y+1, x), node[c], pt[c])
                if y>0:
                    dfs(board, finded, (y-1, x), node[c], pt[c])
                if x>0:
                    dfs(board, finded, (y, x-1), node[c], pt[c])
                if x<w-1:
                    dfs(board, finded, (y, x+1), node[c], pt[c])
                finded[y][x]=False
            return
        
        pt=prefix_tree(words)
        st=search_tree(board, pt)
        re=list()
        for w in words:
            lw=list(w)
            node=st
            add_in=True
            for c in lw:
                if c not in node:
                    add_in=False
                    break
                else:
                    node=node[c]
            if add_in:
                re.append(w)
        return re
