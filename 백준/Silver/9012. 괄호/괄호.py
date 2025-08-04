# 스택(Stack)
# Last In First Out (LIFO)
# 가장 마지막으로 들어간 데이터가 
# 먼저 나온다!! (후입선출)

# Python에서 스택 구현하기 2가지 방법
# 1) List 활용하여 간편하게 구현!!

class Casually_Stack:
    def __init__(self):
        self.s = []
        
    def push(self,data):
        self.s.append(data)
        
    def pop(self):
        return self.s.pop()
        
    def is_empty(self):
        return len(self.s) ==0 
    def peek(self):
        # 비어 있으면 "비어 있습니다" 
        # 비어 있지 않으면 가장 윗 값 
        if self.is_empty() == 1: # 클래스 내에 있는 is_empty호출
            return "비어 있습니다."
        else :
            return self.s[-1]
        
    def __str__(self):
        return str(self.s)

T = int(input())  #숫자 몇개 넣을 지 
b_list = [] #빈 리스트 만들어주고
for i in range(T): # 숫자까지 i입력 받음
    b_list.append(input()) #입력받은거 추가함. 

for test_case in b_list: #입력받은 리스트만들어진거 까지 testcase로 실행함. 
    b_stack = Casually_Stack() #b_stack에서 class 실행함. 
    
    is_valid = True # 여닫이 잘 매칭이 되는지 검증하는 것
    
    for b in test_case:
        if b == "(": #여는 거면
            b_stack.push(b)
        else : #닫는 거면
            if b_stack.is_empty(): #비어있으면 False하고 멈춤
                is_valid = False
                break
            else :  # 비어있지 않았을 떄 
                if b_stack.pop() == "(": # 닫는 거면 꺼내온 것이 여는 것이면 매칭해서 continue하고 있음 
                    continue
                else :
                    is_valid =False #닫는 게 나오면 잘 매칭이 안 되니까 빠져나온것
                    break
    
    if not b_stack.is_empty():
        is_valid = False
    
    print("YES" if is_valid else "NO")          