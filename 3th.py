#구구단
def GuGu(n):
    result=[]
    i=1
    while i<10:
        result.append(2*i)
        i=i+1
    return result
print(GuGu(2))

#더하기
sum=0
i=1
while i<1000:
    if i%3==0:
        sum=sum+i
    elif i%5==0:
        sum=sum+i
    elif i%15==0:
        sum=sum-i
    i=i+1
print(sum)

#게시판 페이징하기

def getTotalPage(m,n):
    result=m//n
    if m%n==0:
        totalpage=result
    else:
        totalpage=result+1
    return totalpage
m=input("게시물의 총 건수")
n=input("한 페이지에 보여줄 게시물 수")

print(getTotalPage(*m,*n))