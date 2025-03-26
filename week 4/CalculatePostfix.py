'''*******************************************************************
  - Project          : algorithm_0326
  - File name        : CalculatePostfix.py
  - Description      : Calculate Postfix Expression
  - Owner            : Seokmin Kang
  - Revision history : 1) 2025.03.26 : Initial release
*******************************************************************'''
import stack 

#후위 표기 수식 계산 알고리즘
def CalculatePostfix(expr):
    operators = ['+','-','*','/']
    s = stack.stack()
    
    for token in expr:
        try:
            operator_idx = operators.index(token)
        except ValueError:
            s.push(float(token))
            continue

        operand2 = s.pull()
        operand1 = s.pull()

        match operator_idx:
            case 0:
                s.push(operand1 + operand2)
            case 1:
                s.push(operand1 - operand2)
            case 2:
                s.push(operand1 * operand2)
            case 3:
                s.push(operand1 / operand2)
        
    return s.pull()

if __name__ == "__main__":
    expr1= ['30','2','-','2','/','12','3','*','+'] # (30-2) / 2 + 12*3
    expr2= ['1','2','/','4','*','1','4','/','*'] # (1 / 2 * 4) * (1 / 4)

    result_expr1 = CalculatePostfix(expr1)
    result_expr2 = CalculatePostfix(expr2)

    print(f"(30-2) / 2 + 12*3 = {result_expr1}")
    print(f"(1 / 2 * 4) * (1 / 4) = {result_expr2}")

