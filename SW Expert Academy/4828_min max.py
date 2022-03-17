
# https://swexpertacademy.com/main/learn/course/subjectDetail.do?courseId=AVuPDN86AAXw5UW6&subjectId=AWOVFCzaqeUDFAWg
# 4828.min max
T = int(input())

for test_case in range(1, T + 1):
    n = int(input())
    a= list(map(int, input().split()))
    diff = max(a)-min(a)
    
    print("#{} {}".format(test_case, diff))
