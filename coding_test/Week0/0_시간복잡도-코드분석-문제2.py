# 아래 Python 코드의 시간 복잡도를 빅오(Big-O) 표기법으로 표현하고, 왜 그렇게 생각하는지 근거를 서술
# 시간 복잡도는 입력의 크기, 즉 리스트 numbers의 길이(원소의 개수)를 n이라고 가정하고 n에 대한 함수로 분석
def has_duplicates(numbers):
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] == numbers[j]:
                return True
    return False

input = [1, 2, 3, 4, 5, 1]
print(has_duplicates(input))
# (n-1) + (n-2) + ... + 1 = n(n-1)/2 = (n^2 - n)/2
# 빅오 표기법에서는 상수 계수와 낮은 차수 항을 무시하므로, 시간 복잡도는 O(n^2).
