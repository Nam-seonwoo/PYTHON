# PYTHON

"""Q2"""
num=13
if num//2==0:
    print("짝수입니다.")
else:
    print("홀수입니다.")
    
"""Q3"""
hong="881120-1068234"
hong_front=hong[0:6]
hong_back=hong[7:]

print(hong_front)
print(hong_back)

"""Q4"""
pin="881120-1068234"
print(pin[7])
"""인덱싱은 0부터 시작하기 때문에 숫자1은 7번째 위치"""

"""Q9"""
"""답 3번. value값에는 리스트를 사용할 수 있지만 key값에는 리스트를 사용할 수 없다.

"""Q10"""
a={'A':90,'B':80,'C':70}
print(a['B'])
