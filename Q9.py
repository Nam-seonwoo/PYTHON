"""2-2"""
num=13
if num//2==0:
    print("짝수입니다.")
else:
    print("홀수입니다.")

"""2-3"""
hong="881120-1068234"
hong_front=hong[0:6]
hong_back=hong[7:]

print(hong_front)
print(hong_back)

"""2-4"""
pin="881120-1068234"
print(pin[7])
"""인덱싱은 0부터 시작하기 때문에 숫자1은 7번째 위치"""

"""2-5"""
a="a:b:c:d"
a.replace('#',':')
print(a)

"""2-6"""
list=[1,3,5,4,2]
list.sort()
list.reverse()
print(list)

"""3-2"""
sum=0
i=1
while i<1000:
    i+=1
    if i%3==0:
        sum=sum+i
print(sum)

"""3-3"""
i=1
while i<=5:
    print('*'*i)
    i=i+1

"""3-4"""
a=range(1,101)
for b in a:
    print(b)

"""3-5"""
i=0
A=[70,60,55,75,95,90,80,80,85,100]
for sum in A:
    i=i+sum
print(i/10)

"""3-6"""
numbers=[1,2,3,4,5]
result=[n*2 for n in numbers if n%2==1]
print(result)

"""4-1"""
k=input("자연수 입력: ")
def is_odd(k):
    if k%2==0
        print("짝수입니다")
    else
        print("홀수입니다.")

""""4-2"""