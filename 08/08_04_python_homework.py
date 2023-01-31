'''
스택(Stack)은 LIFO(Last in First Out)으로 구조화된 자료구조를 의미한다. 
아래 구성요소를 포함하는 Stack class를 생성하라.

구성 요소(메서드)      
i.  __init__(): 인스턴스가 생성될 때 빈 리스트를 각 인스턴스의 이름 공간에 넣는다.      
ii. empty(): 스택이 비었다면 True을 반환하고, 그렇지 않다면 False를 반환한다.      
iii.top(): 스택의 가장 마지막 데이터를 반환한다. 스택이 비었다면 None을 반환한다.      
iv. pop(): 스택의 가장 마지막 데이터의 값을 반환하고, 해당 데이터를 삭제한다. 스택이 비었다면 None을 반환한다.
v.  push(): 스택의 가장 마지막 데이터 뒤에 값을 추가한다. 반환값은 없다.      
vi. __repr__: 현재 스택의 요소들을 보여준다.
'''

class Stack:

    def __init__(self):
        self.stack = []

    def empty(self):
        # if self.stack == []:
        #     return True
        # else:
        #     return False


        # if self.stack:
        #     return True
        # else:
        #     return False

        return not bool(self.stack)



    def top(self):
        if self.stack:
            return None
        else:
            return self.stack[-1]

    def pop(self):
        # if self.stack:
        #     return None
        # else:
        #     return self.stack.pop()

        if not self.empty():
            return self.stack.pop()

    def push(self, n):
        self.stack.append(n)

    def __repr__(self):
        # return repr(self.stack)
        return ''.join(self.stack)      

    def __str__(self): # 프린트하면서 할 때 사용
        return ''.join(self.stack)

ls = Stack()
print(ls.empty())
ls.push(1)
ls.push(2)
print(ls)
print(ls.empty())
print(ls.top())
print(ls)
print(ls.pop())
print(ls)
print(ls.empty())

        