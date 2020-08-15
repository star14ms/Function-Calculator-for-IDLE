# coefs : 식의 각 항의 계수들 (오름차순, list) (coefficients)

항정보 = []  # 출력을 위해 변환시킨 항을 저장할 곳
식 = []

def 계수1_생략(coefs):
  for n in range(len(coefs)):
    if n!=0 and (coefs[n] == 1 or coefs[n] == -1):
      항정보.append(str(coefs[n]).replace('1',''))
    else:
      항정보.append(str(coefs[n]))
      
def x기호_지수_추가(coefs):
  for n in range(len(coefs)):
    항정보[n] = 항정보[n] + 'x^' + str(n)

def 제곱01_생략(coefs):
  항정보[0] = 항정보[0].replace('x^0','')
  if len(coefs)>1:
    항정보[1] = 항정보[1].replace('^1','')
  
def 계수0_생략(coefs):
  for n in range(len(coefs)):
    if 항정보[len(coefs)-1-n].find('0')==0:
      del 항정보[len(coefs)-1-n]

def Change_human_tailored_expression(coefs): # 인간맞춤형 식 출력
  계수1_생략(coefs)
  x기호_지수_추가(coefs)
  제곱01_생략(coefs)
  계수0_생략(coefs)
  항정보.reverse()
  del 식[:]
  식.extend(항정보)
  del 항정보[:]
  return '+'.join(식).replace('+-','-').replace('-',' - ').replace('+',' + ').lstrip(' ')