# '('와 ')'라는 두 가지 유형의 문자로만 구성된 문자열이 주어집니다,
# '(' 또는 ')'를 필요한 만큼 삽입하여 괄호의 균형을 맞춥니다.
# 삽입하여 괄호의 균형을 맞춥니다. 삽입해야 하는 최소 문자 수를 결정합니다.
# 삽입해야 하는 최소 문자 수를 결정합니다.

# Example

# s = '(()))'
# 유효한 시퀀스로 만들려면 문자열의 시작 부분에 '('를 삽입합니다,
# '((()))'가 됩니다. 문자열은 한 번 삽입된 후 균형을 맞춥니다.

# 1. 여는 괄호를 만나면 스택에 집어넣는다
# 2. 닫는 괄호를 만나면 스택에서 제거한다
# except
#     1. 문자열이 끝났는데 스택에 여는 괄호가 남아있으면 그 갯수만큼 괄호가 필요
#     2. 닫는 괄호를 하여 스택에서 제거하려하였지만 스택이 비어있다면 그 갯수만큼 괄호가 필요

def solution(statement):
    stack = []
    res = 0
    for s in statement:
        if s == '(':
            stack.append(s)
        else:
            try:
                stack.pop()
            except:
                res+=1
    res+=len(stack)

    return res

print(solution(')))))))(((((((((()()(((()()(()()()))()()()()))()()())))'))
