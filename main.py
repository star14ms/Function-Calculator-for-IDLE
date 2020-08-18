from .functions import *

x = "x"
################################################################################################################################

### 언어 변경 ###
language = ["English"]


def Korean():
    del language[:]
    language.append("Korean")
    print("언어선택 : 한국어")


def korean():
    Korean()


def 한국어():
    Korean()


def English():
    del language[:]
    language.append("English")
    print("language selection : English")


def english():
    English()


### start messege ###
def messege():
    print("messege()")
    print("-" * 60)

    if language == ["English"]:
        print("1. Defining function:")
        print("Type 'fx()' or 'gx()', and then type the coefficients for each terms (descending order)")
        print("(Separate by spacing, Scope: rational-number)\n")

        print("2. Getting a value of function")
        print("funcion f, derivative, integral(indef) and integral(def) :")
        print("f(x), d('f(x)', x), ii('f(x)'), di('f(x)', r-num, r-num) (or 'g(x)')\n")

        print("(x = 'x' or rational-number or function)")
        print("(if you wanna type infinitely decimal, attach ' to both sides of the each of x, a, b value)")
        print("ex) f('1/3'), d(g(x), 2), d(f(x), g(x)), ii(f(x)), di(g(x),1.5,2.5)\n")

        print("3. Calculating between functions")
        print("sum/difference/multiplication/composite_function of f(x), g(x) :\nxs(a,b) / xd(a,b) / xm(a,b) / xc(a,b)")
        print("(a, b = function)")
        print("xc(f(x),g(x)) = f(g(x))\n")
        
    elif language == ["Korean"]:
        print("1. 함수 정의하기")
        print("'f(x)' or 'gx()'를 입력한 다음, 각 항의 계수들을 입력해라 (내림차순)")
        print("띄어쓰기로 항 구분, 범위: 유리수\n")

        print("2. 함수값 구하기")
        print("함수 f, 미분, 부정적분, 정적분 :")
        print("f(x), d('f(x)', x), ii('f(x)'), di('f(x)',유리수,유리수) (or 'g(x)')\n")

        print("(x = 'x' or 유리수 or 함수)")
        print("(만약 무한소수를 입력하고 싶다면, x, a, b 각각 양옆에 '를 붙여라)")
        print("ex) f('1/3'), d(g(x), 2), d(f(x), g(x)), ii(f(x)), di('g(x)',1.5,2.5)\n")

        print("3. 함수끼리 연산하기")
        print("f(x), g(x)의 합/차/곱/합성 : xs(a,b) / xd(a,b) / xm(a,b) / xc(a,b)")
        print("(a, b = function)")
        print("xc(f(x),g(x)) = f(g(x))\n")

    print("fraction(a, b) : a / b")  # fraction 해석
    print("commands to help you : 'help()', 'tutorial()'")
    print("language selection: 'English()', '한국어()'")
    print("-" * 60)


def 메세지():
    messege()


messege()
# coefficient: 계수, term: 항, descending order 내림차순, fraction: 분수


### help ###
def help():
    print("-" * 60)
    if language == ["English"]:
        print("tutorial : 'tutorial()'")
        print("language selection : 'korean()', 'english()'")
        print("starting messege: 'messege()'\n")

        print("defining function : 'fx()' or 'gx()'\n")

        print("funcion f, derivative, integral(indef) and integral(def) :")
        print("f(x), d('f(x)', x), ii('f(x)'), di('f(x)', r-num, r-num) (or 'g(x)')")
        print("(x = 'x' or rational-number or function)\n")

        print("sum/difference/multiplication/composite_function of f(x), g(x) : xs(a,b) / xd(a,b) / xm(a,b) / xc(a,b)")
        print("(a, b = function)")
    elif language == ["Korean"]:
        print("튜토리얼 : '튜토리얼()'")
        print("언어 선택 : '한국어()', 'english()'")
        print("시작 메세지: '메세지()'\n")

        print("함수 정의 : 'fx()' or 'gx()'\n")

        print("함수 f, 미분, 부정적분, 정적분 :")
        print("f(x), d('f(x)', x), ii('f(x)'), di('f(x)',유리수,유리수)) (or 'g(x)')")
        print("(x = 'x' or 유리수 or function)\n")

        print("f(x), g(x)의 합/차/곱/합성 : xs(a,b) / xd(a,b) / xm(a,b) / xc(a,b)")
        print("(a, b = function)")
    print("-" * 60)


## 함숫값 구하기 ##
def value_of_function(x, coefs):
    for n in range(len(coefs)):  # n : n차항의 계수
        if n == 0:
            y = coefs[0]
        else:
            y += coefs[n] * x ** n
    return y


################################################################################################################################

### f(x) 추가 ###

f_coefs = []
f_function = []

## 함수 f(x) 정의 ## (각 항의 계수를 입력받아 위에 list 형태로 저장)
def fx():
    try:
        if language == ["English"]:
            list = input("coefficients: ").split()
        elif language == ["Korean"]:
            list = input("계수들: ").split()

        if list == []:
            raise
        if isTrue_rational_nums(list) == False:
            raise

        del f_coefs[:]
        f_coefs.extend(Change_strs_fractions(list))
        f_coefs.reverse()  # 오름차순 (계산, 출력에 용이)

        del f_function[:]
        f_function.append(Change_human_tailored_expression(f_coefs))
        print("f(x) =", f_function[0])  # 함수식 출력

    except:
        if list == []:
            if language == ["English"]:
                print("'Error: nothing inputed'")
            elif language == ["Korean"]:
                print("'오류: 입력 없음'")
        elif isTrue_rational_nums(list) == False:
            if language == ["English"]:
                print("'Error: not rational numbers'")
            elif language == ["Korean"]:
                print("'오류: 유리수가 아님'")


## f(x) 함숫값 ##
def f(x):
    try:
        if f_coefs == []:
            raise

        if x == "x": # 함수식 출력
            print("f(x) =", f_function[0])
            return f_coefs

        elif str(type(x)) == "<class 'list'>": # 합성함수
            composite = xc(f_coefs, x)
            if x == f_coefs:
                print("f(f(x)) =", end=' ')
            elif x == g_coefs:
                print("f(g(x)) =", end=' ')
            else: 
                print("f(func2(x)) =", end=' ')
            print(Change_human_tailored_expression(composite))
            return composite

        else: 
            x = Change_str_fraction(str(x))
            return value_of_function(x, f_coefs) # 함숫값 계산, 출력

    except:
        if f_coefs == []:
            if language == ["English"]:
                print("'Error: f(x) is not defined' in f(x)")
            elif language == ["Korean"]:
                print("'오류: f(x)가 정의되지 않음'")
        elif isTrue_rational_num(x) == False:
            if language == ["English"]:
                print("'Error: not rational numbers' in f(x)")
            elif language == ["Korean"]:
                print("'오류: 유리수가 아님'")
        else: print("알 수 없는 오류")


################################################################################################################################

### 함수 g(x) 추가 ### (함수 f(x)와 똑같은 코드, g(x) 버전)

g_coefs = []
g_function = []

## 함수 g(x) 정의 ##
def gx():
    try:
        if language == ["English"]:
            list = input("coefficients: ").split()
        elif language == ["Korean"]:
            list = input("계수들: ").split()

        if list == []:
            raise
        if isTrue_rational_nums(list) == False:
            raise

        del g_coefs[:]
        g_coefs.extend(Change_strs_fractions(list))
        g_coefs.reverse()

        del g_function[:]
        g_function.append(Change_human_tailored_expression(g_coefs))
        print("g(x) =", g_function[0])

    except:
        if list == []:
            if language == ["English"]:
                print("'Error: nothing inputed'")
            elif language == ["Korean"]:
                print("'오류: 입력 없음'")
        elif isTrue_rational_nums(list) == False:
            if language == ["English"]:
                print("'Error: not rational numbers'")
            elif language == ["Korean"]:
                print("'오류: 유리수가 아님'")


## g(x) 함숫값 ##
def g(x):
    try:
        if g_coefs == []:
            raise
        if x == "x":
            print("g(x) =", g_function[0])
            return g_coefs

        elif str(type(x)) == "<class 'list'>":
            composite = xc(g_coefs, x)
            if x == f_coefs:
                print("g(f(x)) =", end=' ')
            elif x == g_coefs:
                print("g(g(x)) =", end=' ')
            else: 
                print("g(func2(x)) =", end=' ')
            print(Change_human_tailored_expression(composite))
            return composite
            
        else:
            x = Change_str_fraction(str(x))
            return value_of_function(x, g_coefs)  # 함숫값 계산, 출력

    except:
        if g_coefs == []:
            if language == ["English"]:
                print("'Error: g(x) is not defined' in g(x)")
            elif language == ["Korean"]:
                print("'오류: g(x)가 정의되지 않음'")
        elif isTrue_rational_num(x) == False:
            if language == ["English"]:
                print("'Error: not rational numbers' in g(x)")
            elif language == ["Korean"]:
                print("오류: 유리수가 아님")


################################################################################################################################

### 미적분 추가 ###

## 미분 ##
def d(function, x): 
    try:
        if str(type(function)) == "<class 'list'>":
            dx_coefs = []
            for n in range(len(function)):  # 각 항에서
                dx_coefs.append(n * function[n])  # 새 계수 = 차수 x 계수
            del dx_coefs[0]  # 상수항 사라짐

            if str(type(x)) == "<class 'list'>":
                d_c_function = xm(  d( xc(function, x), 'x' ), d(x, 'x')  )
                print("-" * 60)
                if function == f_coefs:
                    if x == f_coefs:
                        print("df(f(x))/dx =", end=' ')
                    elif x == g_coefs:
                        print("df(g(x))/dx =", end=' ')
                    else:
                        print("df(func2(x))/dx =", end=' ')
                elif function == g_coefs:
                    if x == f_coefs:
                        print("dg(f(x))/dx =", end=' ')
                    elif x == g_coefs:
                        print("dg(g(x))/dx =", end=' ')
                    else: 
                        print("dg(func2(x))/dx =", end=' ')
                else:
                    if x == f_coefs:
                        print("dfunc1(f(x))/dx =", end=' ')
                    elif x == g_coefs:
                        print("dfunc1(g(x))/dx =", end=' ')
                    else:
                        print("dfunc1(func2(x))/dx =", end=' ')
                print(Change_human_tailored_expression(d_c_function))
                return d_c_function

            elif function == f_coefs:
                print("df(x)/dx =", Change_human_tailored_expression(dx_coefs))
            elif function == g_coefs:
                print("dg(x)/dx =", Change_human_tailored_expression(dx_coefs))
            else:
                print("dfunc(x)/dx =", Change_human_tailored_expression(dx_coefs))
            
            if x == 'x':
                return dx_coefs
            else:
                x = Change_str_fraction(str(x))
                if function == f_coefs:
                    print(f"df({x})/dx =", end=' ')
                elif function == g_coefs:
                    print(f"dg({x})/dx =", end=' ')
                else:
                    print(f"dfunc({x})/dx =", end=' ')
                print(value_of_function(x, dx_coefs))
                return value_of_function(x, dx_coefs)
        else:
            if isTrue_rational_num(str(x)) == True:
                return 0
            else: 
                raise
    except:
        if str(type(function)) != "<class 'list'>" and isTrue_rational_num(x) == False:
            if language == ["English"]:
                print("'Error: x is not rational number' in d(func, x)")
            elif language == ["Korean"]:
                print("'오류: x가 유리수가 아님' d(func, x)에서")
        elif function == None:
            if language == ["English"]:
                print("'Error: not defined function' in d(func, x)")
            elif language == ["Korean"]:
                print("'오류: 정의되지 않은 함수' d(func, x)에서")
        else: print("알 수 없는 오류")


## 부정적분 ##
def ii(function): 
    try:
        if str(type(function)) == "<class 'list'>":
            iix_coefs = []
            for n in range(len(function)):  # 각 항에서
                iix_coefs.append(function[n] / (n + 1))  # 새 계수 = 계수 / (차수+1)
            iix_coefs.reverse()
            iix_coefs.append("C")  # 적분상수 C 추가
            iix_coefs.reverse()
            
            if function == f_coefs:
                print("∫f(x)dx =", Change_human_tailored_expression(iix_coefs)) # s = ∫
            elif function == g_coefs:
                print("∫g(x)dx =", Change_human_tailored_expression(iix_coefs))
        else:
            raise
    except:
        if function == None:
            if language == ["English"]:
                print("'Error: not defined function' in ii(func)")
            elif language == ["Korean"]:
                print("'오류: 정의되지 않은 함수' ii(func))에서")  
        elif str(type(function)) != "<class 'list'>": 
            if language == ["English"]:
                print("'Error: indefinite integral cannot obtain function value' in ii(func)")
            elif language == ["Korean"]:
                print("'오류: 부정적분은 함수값을 구할 수 없음' ii(func))에서")
        else: print("알 수 없는 오류")


## 정적분 ##
def di(function, range_a, range_b):
    try:
        a = Change_str_fraction(str(range_a))  # a, b를 분수꼴로 바꾸기
        b = Change_str_fraction(str(range_b))

        value = 0
        dix_coefs = []
        for n in range(len(function)):
            dix_coefs.append(function[n] / (n + 1))
            dix_coefs[n] = dix_coefs[n] * (b ** (n + 1) - a ** (n + 1))
            value += dix_coefs[n]  # value = 각 항을 정적분하여 모두 더한 값

        if function == f_coefs:
            print(f"∫{a},{b} f(x)dx =", value)
        elif function == g_coefs:
            print(f"∫{a},{b} g(x)dx =", value)
        return value
    except:
        if function == None:
            if language == ["English"]:
                print("'Error: not defined function' in di(func, a, b)")
            elif language == ["Korean"]:
                print("'오류: 정의되지 않은 함수' di(func, a, b))에서")  
        elif isTrue_rational_nums([str(range_a), str(range_a)]) == False:
            if language == ["English"]:
                print("'Error: not rational numbers' in di(func, a, b)")
            elif language == ["Korean"]:
                print("'오류: 유리수가 아님' di(func, a, b))에서")
        else: print("알 수 없는 오류")


################################################################################################################################

### x에 관한 식(함수)의 연산 추가 ###

## 오류 메세지 ##
def error_messege_not_expression_for_x():
    if language == ["English"]:
        print("'Error: at least one is not expression for x'")
    elif language == ["Korean"]:
        print("'오류: 적어도 하나가 x에 관한 식이 아님'")


## x에 관한 식(함수)끼리 더하기 ##
def xs(a, b):
    try:
        sum_x = []
        if len(a) >= len(b):
            full_a, full_b = a, b + [0]*(len(a)-len(b))
        else:
            full_a, full_b = a + [0]*(len(b)-len(a)), b

        for n in range(len(full_a)):
            sum_x.append(full_a[n] + full_b[n])

        print("sum(x) =", Change_human_tailored_expression(sum_x))
        return sum_x
    except:
        error_messege_not_expression_for_x()


## x에 관한 식(함수)끼리 빼기 ##
def xd(a, b):
    try:
        difference_x = []
        if len(a) >= len(b):
            full_a, full_b = a, b + [0]*(len(a)-len(b))
        else:
            full_a, full_b = a + [0]*(len(b)-len(a)), b

        for n in range(len(full_a)):
            difference_x.append(full_a[n] - full_b[n])

        print("difference(x) =", Change_human_tailored_expression(difference_x))
        return difference_x
    except:
        error_messege_not_expression_for_x()


## x에 관한 식(함수)끼리 곱하기(전개) ##
def xm(a, b): # Multiplication
    try:
        expansion_x = []
        for l in range(len(a)+len(b)-1):
            expansion_x.append(0)
    
        for n in range(len(a)):
            for m in range(len(b)):
                expansion_x[n+m] = expansion_x[n+m] + a[n] * b[m]

        if language == ["English"]:
            print("expansion(x) =", Change_human_tailored_expression(expansion_x))
        elif language == ["Korean"]:
            print("전개식(x) =", Change_human_tailored_expression(expansion_x))    
        return expansion_x
    except:
        error_messege_not_expression_for_x()


## 합성함수 ## 
def xc(f, g): # Composite function    
    try:
        print("-" * 60)
        expansion_x = []
        for n in range(len(f)): # 각 항에서
            if n == 0:
                expansion_x.append([f[0]])
            else:
                x_part = g
                for m in range(n-1):
                    x_part = xm(x_part, g) # x^n
                expansion_x.append(xm([f[n]], x_part)) # a*(x^n)

        for n in range(len(expansion_x)-1): # 각 항들 합쳐서 간단하게
            expansion_x.insert(2, xs(expansion_x[0], expansion_x[1]))
            del expansion_x[0:2]
        
        print("-" * 60)
        if language == ["English"]:
            print("composite(x) =", Change_human_tailored_expression(expansion_x[0]))
        elif language == ["Korean"]:
            print("합성함수(x) =", Change_human_tailored_expression(expansion_x[0]))

        return expansion_x[0]
    except:
        error_messege_not_expression_for_x()


################################################################################################################################

## Tutorial ##
def tutorial():
    print("-" * 60)
    if language == ["English"]:
        print("if you wanna exit tutorial, type 'exit'")
        print("Tutorial: Usage of 'fx()', f(x) command")
        print(
            "Try to type 'fx()' and to type the coefficients for each terms (descending order)"
        )
    elif language == ["Korean"]:
        print("튜토리얼에서 나가길 원하면 'exit'를 쳐라")
        print("튜토리얼: 'fx()', f(x) 명령어의 사용법")
        print("'fx()'를 치고, 각 항의 계수들을 입력해 보아라 (내림차순)")

    while True:
        print("-" * 60)
        if f_coefs != []:
            if language == ["English"]:
                print(
                    "Try to Type f(rational-number), 'f(x)', or 'fx()' again to redefine"
                )
            elif language == ["Korean"]:
                print("f(유리수), 'f(x)'를 쳐봐라, 또는 함수 재정의를 위해 'fx()'를 다시 쳐라")

        a = input()

        if a == "break" or a == "break()" or a == "exit" or a == "exit()":
            break

        elif a == "English()" or a == "english()":
            English()
            print("if you wanna exit tutorial, type 'break'")
            print("Try to type 'fx()' and to type the coefficients for each terms (descending order)")

        elif a == "Korean()" or a == "korean()" or a == "한국어()":
            Korean()
            print("튜토리얼에서 나가길 원하면 'break'를 쳐라")
            print("'fx()'를 치고, 각 항의 계수들을 입력해 보아라 (내림차순)")

        elif a == "fx":
            if language == ["English"]:
                print("Type '()' too!")
            elif language == ["Korean"]:
                print("'()'도 쳐라!")
            
        ## 함수 정의 명령어 'fx()'를 입력 ##
        elif a == "fx()":

            # fx() 실행
            fx()
        
        ## 함수 정의를 먼저 했는지 검사 ##
        elif f_coefs == []:
            if language == ["English"]:
                print("'Error: f(x) is not defined'")
                print("Type 'fx()' first!")
            elif language == ["Korean"]:
                print("'오류: f(x)가 정의되지 않음'")
                print("'fx()'를 먼저 쳐라!")

        ## x값 대입 명령어 f(x)를 쳤을 때 ##
        elif (
            "f(" in a and ")" in a and a.index("f(") == 0 and a.index(")") == len(a) - 1
        ):

            # x값만 추출 #
            x = a.replace("f(", "").replace(")", "")

            # "f(x)"라고 쳤을 때:
            if x == "x":
                print("f(x) =", f_function[0])

            else:  # f(x) 값 출력 #
                print(f(x))

    if language == ["English"]:
        print("Tutorial exit")
    elif language == ["Korean"]:
        print("튜토리얼 나가기")
    print("-" * 60)


def 튜토리얼():
    tutorial()
