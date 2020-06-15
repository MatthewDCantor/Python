""" ------ Problem ------

Pip has N strings. Each string consists only of letters from A to Z. Pip would
like to bundle their strings into group sizes of group size K. Each string must
belong to exactly one group.

The score of a group is equal to the length of the longest prefix shared by all
the strings in that group. For example:

The group {RAINBOW, RANK, RANDOM, RANK} has a score of 2 ('RA')

Help pip bundle the strings into groups of size K, such that the sum of the
scores of the groups is maximized.

------------Input & Output---------

'2'
'2 2'
'KICK'
'START'
'8 2'
'G'
'G'
'GO'
'GO'
'GOO'
'GOO'
'GOOO'
'GOOO'


"""




"""
Trie is an efficient information reTrieval data structure. Using Trie,
search complexities can be brought to optimal limit (key length).
If we store keys in binary search tree, a well balanced BST will need time
proportional to M * log N, where M is maximum string length
and N is number of keys in tree. Using Trie, we can search the key in O(M) time.
However the penalty is on Trie storage requirements.
(Please refer Applications of Trie for more details)


Algorithm to make Trie:
1. Create root node as null.
2. Insert key 'example'
3. I. If root node doesnt have e as a key, then we add a new node with which
    contains a dictionary with all words which begin with e.
   II. If e is already a key of the root node then the root node will have a
   child which contains a TrieNode with e as its key. {'e' : TrieNode}. Make the
   current node equal to the vale of the key 'e'.
4. This process continues with 'ex', 'exa', etc.
"""
class  TrieNode:
    """Node in a Trie which contains a dict of all prefixes"""

    def __init__(self):


        self.children = {}

class Trie:


    def __init__(self):

        self.root = TrieNode()
        self.occurences = {}

    def insert(self,char):

        #create current node tracker
        node = self.root

        for i in range(len(char)):
            # 'e', 'ex', 'exa',..., 'example'
            key = char[0:i+1]

            # if the key is not in the current nodes dict, make a new node
            # where {key: new Trie Node}
            if not key in node.children:
                node.children[key] = TrieNode()
                self.occurences[key] = 0
            # make the current node equal to the value of
            node = node.children[key]
            self.occurences[key] += 1

    def find(self,char):

        node = self.root

        for i in range(len(char)):
            key = char[0:i+1]

            if not key in node.children:
                return False
            node = node.children[key]

        return True

    def solve(self,K):

        answer = 0
        for key in self.occurences:
            answer += self.occurences[key]//K

        return answer


rr = lambda: input().strip()
rri = lambda: int(rr())
rrm = lambda: list(map(int, rr().split( )))

test_cases = rri()

for t in range(1,test_cases+1):

    trie = Trie()
    n,k = rrm()

    for i in range(n):

        trie.insert(input())

    print("Case #{}: {}".format(t,trie.solve(k)))
