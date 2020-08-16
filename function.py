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
    print("-" * 60)
    if language == ["English"]:
        print("1. Defining f(x):")
        print(
            "Type 'fx()', and then type the coefficients for each terms (descending order)"
        )
        print("(Separate by spacing, Scope: rational-number)\n")

        print("2. Getting a value of function")
        print(
            "Type f(x), df(x), 'F(x)' or DF(a, b) with a substitute of some rational-num in x, a, b"
        )
        print(
            "if you wanna type infinitely decimal, attach ' to both sides of the each of x, a, b value."
        )
    elif language == ["Korean"]:
        print("1. f(x) 정의하기")
        print("'f(x)'를 입력한 다음, 각 항의 계수들을 입력해라 (내림차순)")
        print("띄어쓰기로 항 구분, 범위: 유리수\n")

        print("2. 함수값 구하기")
        print("x, a, b 에 유리수를 대입하여 f(x) 또는 df(x), 'F(x)', DF(a, b)를 입력해라")
        print("만약 무한소수를 입력하고 싶다면, x, a, b 각각 양옆에 '를 붙여라")
    print("ex) f('1/3'), df(2), F(x), DF(1.5, 2.5)\n")
    print("commands to help you : 'help()', 'tutorial()'")
    print("language selection: 'English()', '한국어()'")
    print("-" * 60)


def 메세지():
    messege()


messege()
# coefficient: 계수, term: 항, descending order 내림차순, fraction: 분수


### help ###
def help():
    if language == ["English"]:
        print("tutorial : 'tutorial()'")
        print("language selection : 'korean()', 'english()'")
        print("starting messege: 'messege()'\n")
        print("defining function f : 'fx()'\n")
        print("f(x), df(x), 'F(x)', DF(r-n, r-n) :")
        print("f(x), differential, integral(indef) and integral(def)\n")
        print("(x = 'x' or rational-number)\n")
        print("Can define g(x) also (put g in place of f)")
    elif language == ["Korean"]:
        print("튜토리얼 : '튜토리얼()'")
        print("언어 선택 : '한국어()', 'english()'")
        print("시작 메세지: '메세지()'\n")
        print("함수 f 정의 : 'fx()'\n")
        print("f(x), df(x), 'F(x)', DF(유리수, 유리수)) :")
        print("f(x), 미분, 부정적분, 정벅분\n")
        print("x = 'x' or 유리수\n")
        print("함수 g도 정의 가능 (f 자리에 g를 넣어서)\n")
        print("fraction(a, b) 뜻 : a/b")  # fraction 해석


## 함숫값 구하기 ##
def value_of_function(x, coefs):
    for n in range(len(coefs)):  # n : n차항의 계수
        if n == 0:
            y = coefs[0]
        else:
            y += coefs[n] * x ** n
    return y


################################################################################################################################

### 유리 함수 f(x) 추가 ###

f_coefs = []
df_coefs = []
F_coefs = []
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
        x = Change_str_fraction(str(x))
        return value_of_function(x, f_coefs)  # 함숫값 계산, 출력

    except:
        if f_coefs == []:
            if language == ["English"]:
                print("'Error: f(x) is not defined'")
            elif language == ["Korean"]:
                print("'오류: f(x)가 정의되지 않음'")
        elif x == "x":
            print("f(x) =", f_function[0])
        elif isTrue_rational_num(x) == False:
            if language == ["English"]:
                print("'Error: not rational numbers'")
            elif language == ["Korean"]:
                print("'오류: 유리수가 아님'")


## f(x) 미분, 값 ##
def df(x):
    try:
        if len(f_coefs) == 1:
            return 0

        del df_coefs[:]
        for n in range(len(f_coefs)):  # 각 항에서
            df_coefs.append(n * f_coefs[n])  # 새 계수 = 차수 x 계수
        del df_coefs[0]  # 상수항 사라짐

        x = Change_str_fraction(str(x))
        return value_of_function(x, df_coefs)

    except:
        if f_coefs == []:
            if language == ["English"]:
                print("'Error: f(x) is not defined'")
            elif language == ["Korean"]:
                print("'오류: f(x)가 정의되지 않음'")
        elif x == "x":
            print("df(x)/dx =", Change_human_tailored_expression(df_coefs))
        elif isTrue_rational_num(x) == False:
            if language == ["English"]:
                print("'Error: not rational numbers'")
            elif language == ["Korean"]:
                print("'오류: 유리수가 아님'")


## f(x) 부정적분 ##
def F(x):
    try:
        if f_coefs == []:
            raise
        if x != "x" and isTrue_rational_num(str(x)) == False:
            raise

        if f_coefs[0] == 0 and len(f_coefs) == 1:  # 항이 0 하나면 0 출력
            return 0

        del F_coefs[:]
        for n in range(len(f_coefs)):  # 각 항에서
            F_coefs.append(f_coefs[n] / (n + 1))  # 새 계수 = 계수 / (차수+1)

        F_coefs.reverse()
        F_coefs.append("C")  # 적분상수 C 추가
        F_coefs.reverse()
        print("F(x) = " + Change_human_tailored_expression(F_coefs))

    except:
        if f_coefs == []:
            if language == ["English"]:
                print("'Error: f(x) is not defined'")
            elif language == ["Korean"]:
                print("'오류: f(x)가 정의되지 않음'")
        elif x != "x" and isTrue_rational_num(x) == False:
            if language == ["English"]:
                print("'Error: not 'x' or rational numbers'")
            elif language == ["Korean"]:
                print("'오류: 'x' 또는 유리수가 아님'")


## f(x) 정적분 ##
def DF(range_a, range_b):
    try:
        if f_coefs == []:
            raise
        if isTrue_rational_nums([str(range_a), str(range_b)]) == False:
            raise  # 유리수가 아니면 예외

        a = Change_str_fraction(str(range_a))  # a, b를 분수꼴로 바꾸기
        b = Change_str_fraction(str(range_b))

        value = 0
        del F_coefs[:]
        for n in range(len(f_coefs)):
            F_coefs.append(f_coefs[n] / (n + 1))
            F_coefs[n] = F_coefs[n] * (b ** (n + 1) - a ** (n + 1))
            value += F_coefs[n]  # value = 각 항을 정적분하여 모두 더한 값
        return value

    except:
        if f_coefs == []:
            if language == ["English"]:
                print("'Error: f(x) is not defined'")
            elif language == ["Korean"]:
                print("'오류: f(x)가 정의되지 않음'")
        elif isTrue_rational_nums([str(range_a), str(range_a)]) == False:
            if language == ["English"]:
                print("'Error: not rational numbers'")
            elif language == ["Korean"]:
                print("'오류: 유리수가 아님'")


################################################################################################################################

### 유리 함수 g(x) 추가 ### (함수 f(x)와 똑같은 코드, g(x) 버전)

g_coefs = []
dg_coefs = []
G_coefs = []
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
        x = Change_str_fraction(str(x))
        return value_of_function(x, g_coefs)

    except:
        if g_coefs == []:
            if language == ["English"]:
                print("'Error: g(x) is not defined'")
            elif language == ["Korean"]:
                print("'오류: g(x)가 정의되지 않음'")
        elif x == "x":
            print("g(x) =", g_function[0])
        elif isTrue_rational_num(x) == False:
            if language == ["English"]:
                print("'Error: not rational numbers'")
            elif language == ["Korean"]:
                print("오류: 유리수가 아님")


## g(x) 미분, 값 ##
def dg(x):
    try:
        if len(g_coefs) == 1:
            return 0

        del dg_coefs[:]
        for n in range(len(g_coefs)):  # 각 항에서
            dg_coefs.append(n * g_coefs[n])  # 새 계수 = 차수 x 계수
        del dg_coefs[0]  # 상수항 사라짐

        x = Change_str_fraction(str(x))
        return value_of_function(x, dg_coefs)

    except:
        if g_coefs == []:
            if language == ["English"]:
                print("'Error: g(x) is not defined'")
            elif language == ["Korean"]:
                print("'오류: g(x)가 정의되지 않음'")
        elif x == "x":
            print("dg(x)/dx =", Change_human_tailored_expression(dg_coefs))
        elif isTrue_rational_num(x) == False:
            if language == ["English"]:
                print("'Error: not rational numbers'")
            elif language == ["Korean"]:
                print("'오류: 유리수가 아님'")


## g(x) 부정적분 ##
def G(x):
    try:
        if g_coefs == []:
            raise
        if x != "x" and isTrue_rational_num(str(x)) == False:
            raise

        if g_coefs[0] == 0 and len(g_coefs) == 1:
            return 0

        del G_coefs[:]
        for n in range(len(g_coefs)):
            G_coefs.append(g_coefs[n] / (n + 1))

        G_coefs.reverse()
        G_coefs.append("C")
        G_coefs.reverse()
        print("G(x) = " + Change_human_tailored_expression(G_coefs))

    except:
        if g_coefs == []:
            if language == ["English"]:
                print("'Error: g(x) is not defined'")
            elif language == ["Korean"]:
                print("'오류: g(x)가 정의되지 않음'")
        elif x != "x" and isTrue_rational_num(x) == False:
            if language == ["English"]:
                print("'Error: not 'x' or rational numbers'")
            elif language == ["Korean"]:
                print("'오류: 'x' 또는 유리수가 아님'")


## g(x) 정적분 ##
def DG(range_a, range_b):
    try:
        if g_coefs == []:
            raise
        if isTrue_rational_nums([str(range_a), str(range_b)]) == False:
            raise  # 유리수가 아니면 예외

        a = Change_str_fraction(str(range_a))  # a, b를 분수꼴로 바꾸기
        b = Change_str_fraction(str(range_b))

        value = 0
        del G_coefs[:]
        for n in range(len(g_coefs)):
            G_coefs.append(g_coefs[n] / (n + 1))
            G_coefs[n] = G_coefs[n] * (b ** (n + 1) - a ** (n + 1))
            value += G_coefs[n]  # value = 각 항을 정적분하여 모두 더한 값
        return value

    except:
        if g_coefs == []:
            if language == ["English"]:
                print("'Error: g(x) is not defined'")
            elif language == ["Korean"]:
                print("'오류: g(x)가 정의되지 않음'")
        elif isTrue_rational_nums([str(range_a), str(range_a)]) == False:
            if language == ["English"]:
                print("'Error: not rational numbers'")
            elif language == ["Korean"]:
                print("'오류: 유리수가 아님'")


################################################################################################################################

## Tutorial ##
def tutorial():
    if language == ["English"]:
        print("if you wanna exit tutorial, type 'break'")
        print(
            "Try to type 'fx()' and to type the coefficients for each terms (descending order)"
        )
    elif language == ["Korean"]:
        print("튜토리얼에서 나가길 원하면 'break'를 쳐라")
        print("'fx()'를 치고, 각 항의 계수들을 입력해 보아라 (내림차순)")

    while True:
        print("-" * 60)
        if f_coefs != []:
            if language == ["English"]:
                print(
                    "Try to Type f(rational-number), 'f(x)', or 'fx()' again to redefine"
                )
            elif language == ["Korean"]:
                print("f(유리수), 'f(x)'를 쳐봐라, 아니면 함수 재정의를 위해 'fx()'를 다시 쳐라")

        a = input()

        if a == "break" or a == "break()":
            break

        elif a == "english" or a == "english()" or a == "English" or a == "English()":
            English()
            print("if you wanna exit tutorial, type 'break'")
            print(
                "Try to type 'fx()' and to type the coefficients for each terms (descending order)"
            )

        elif a == "korean" or a == "korean()" or a == "Korean" or a == "Korean()" or a == "한국어" or a == "한국어()":
            Korean()
            print("튜토리얼에서 나가길 원하면 'break'를 쳐라")
            print("'fx()'를 치고, 각 항의 계수들을 입력해 보아라 (내림차순)")

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
                    if f(x) == None:
                        print("try again")
                    else:
                        print("great!")
                elif language == ["Korean"]:
                    if f(x) == None:
                        print("다시 해 봐요")
                    else:
                        print("잘했어요!")


def 튜토리얼():
    tutorial()
