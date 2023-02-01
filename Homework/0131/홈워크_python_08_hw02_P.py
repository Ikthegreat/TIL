class Stack:

    def __init__(self):
        self.items = []

    def empty(self):
        return len(self.items) == 0

    def top(self):
        if self.empty() == False:
            top_object = self.items[-1]
        else:
            return None
        return top_object

    def pop(self):
        pop_object = None
        if self.empty() == False:
            pop_object = self.items.pop()
        elif self.empty() == True:
            return None
        return pop_object
    
    def push(self, data):
        self.items.append(data)
        pass

    def __repr__(self):
        print(self.items)
        

Data = Stack()

Data.__repr__() # 기본 상태 확인
Data.push(1) # 1을 Data에 추가
print(Data.empty()) # 비어있는지 확인
Data.__repr__() # 1이 들어간 상태 확인
print(Data.top()) # 1이 들어간 경우 마지막 데이터 반환
print(Data.pop()) # 데이터가 있을 경우 데이터 삭제 및 반환
print(Data.pop()) # 데이터가 없을 경우 None 반환
print(Data.top()) # 데이터가 없을 경우 None 반환
Data.__repr__() # 마지막 상태 확인
print(Data.empty()) # 비어있는지 확인