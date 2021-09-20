
class Stack:
    def __init__(self):
       self.myStack = []

    def isEmpty(self):
        return self.myStack == []

    def push(self, item):
        self.myStack.append(item)

    def pop(self):
        return self.myStack.pop()

    def peek(self):
        return self.myStack[len(self.myStack) - 1]

    def size(self):
        return len(self.myStack)

def parChecker(symbolString):

    if len(symbolString) % 2 == 1:
        return False

    openings = set('({[')
    matches = set([('{', '}'), ('(', ')'), ('[', ']')])

    for paren in symbolString:
        if paren in openings:
            s.push(paren)
        else:
            if s.size() == 0:
                return False
            last_open = s.pop()
            if (last_open, paren) not in matches:
                return False

    return s.size() == 0

if __name__ == '__main__':
    s = Stack()
    print(parChecker('(((([{}]))))'))
    print(parChecker('[([])((([[[]]])))]{()}'))
    print(parChecker('{{[()]}}'))

    print(parChecker('}{}'))
    print(parChecker('{{[(])]}}'))
    print(parChecker('[[{())}]'))

