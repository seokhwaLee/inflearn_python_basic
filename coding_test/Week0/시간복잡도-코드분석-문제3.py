# 아래 Python 코드의 시간 복잡도를 빅오(Big-O) 표기법으로 표현하고, 왜 그렇게 생각하는지 근거를 서술
# 시간 복잡도는 입력의 크기, 즉 리스트 sorted_list의 길이(원소의 개수)를 n이라고 가정하고 n에 대한 함수로 분석
def binary_search(sorted_list, target):
    left, right = 0, len(sorted_list) - 1
    while left <= right:
        mid = (left + right) // 2
        if sorted_list[mid] == target:
            return True
        elif sorted_list[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return False

input = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(binary_search(input, 1))
# 이진탐색이란? "정렬된 리스트"에서 특정 값을 찾기 위해 중간 값을 계속 비교하며 탐색 범위를 절반씩 줄여나가는 알고리즘.
# 1. 처음에 리스트의 중간 값을 확인.
# 2. 중간 값이 찾고자 하는 값과 같으면 탐색을 종료.
# 3. 중간 값이 찾고자 하는 값보다 작으면, 중간 값의 오른쪽 절반을 탐색 대상으로 설정.
# 4. 중간 값이 찾고자 하는 값보다 크면, 중간 값의 왼쪽 절반을 탐색 대상으로 설정.
# 5. 이 과정을 반복하여 탐색 범위를 계속 절반으로 줄여나감.

# 매 반복마다 탐색 범위가 절반으로 줄어듦.
# 수식: n -> n/2 -> n/4 -> n/8 ... -> 1 
# 이 과정이 k번 반복될 때, n / (2^k) = 1이 되므로, 양변에 로그를 취하면 k = log2(n).
# 따라서 n개의 원소가 있을 때, 최대 log2(n)번의 비교만으로 원하는 값을 찾을 수 있다.