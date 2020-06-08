class LinkedList:

    """ init - Initalize a linked list. Payload will be
    set to value of the link, which can later be used for searching
    """
    def __init__(self, payload):
        self.pl = payload
        self.next = None

    """ Add - create a new node and it to the list.

    The new node should be added to the front of the list.

    """
    def add(self, payload):
        new_node = LinkedList(payload)
        new_node.next = self.next
        self.next = new_node




    """ Remove - Remove the node from the list that equals query """

    def remove(self, query):
        cur = self.next
        next_cur = cur.next

        if cur.pl == query:
            self.next = cur.next
            return True


        while(cur.next != None):

            if cur.pl == query:
                cur.next = next_cur.next
                return True
            elif next_cur.pl == query and next_cur.next == None:
                cur.next = None
                return True

            cur = cur.next
            next_cur = cur.next

        return False





    """ Search - Search for query in the list.

    If query is found, then the item that was added to the node, if it isn't
    then False will be returned
    """
    def search(self, query):
        cur = self.next
        next_cur = cur.next

        while(cur.next != query):
            if cur.pl == query:
                return cur.pl
            elif next_cur.pl == query and next_cur.next == None:
                return next_cur.pl

            cur = cur.next
            next_cur = cur.next
        return False
    """ isEmpty - Return True if the list is Empty, False otherwise

    """
    def isEmpty(self):
        if self.next == None:
            return True
        else:
            return False
    """ Print a linked list """
    def print_list(self):
        i=0
        cur = self.next
        while(cur.next != None):
            print(i, ":", cur.pl)
            i += 1
            cur = cur.next
        print(i, ":", cur.pl)

def init_list():
    return LinkedList(None)
