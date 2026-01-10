import time

# 시간 측정 데코레이터
def time_check(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Execution time of {func.__name__}: {end - start} seconds")
        return result
    return wrapper

# 인덱싱 vs 슬라이싱 vs 이터레이터 성능 비교
## 1. 인덱싱
@time_check
def find_max(numbers):
    max_num = numbers[0]
    for i in range(1, len(numbers)):
        if numbers[i] > max_num:
            max_num = numbers[i]
    return max_num
# 매 반복마다 numbers[i] 인덱싱 수행
# CPython에서 인덱싱은 “C 함수 호출 + bounds check + 포인터 fetch”가 반복됨
# range 반복 + 인덱싱 조합이 생각보다 오버헤드 큼

## 2. 슬라이싱
@time_check
def find_max_slicing(numbers):
    max_num = numbers[0]
    for num in numbers[1:]:
        if num > max_num:
            max_num = num
    return max_num
# 시간만 보면 슬라이싱이 인덱싱보다 빠를 수 있음
# 하지만 슬라이싱은 메모리/GC 비용이 치명적임
# numbers[1:]에서 리스트 포인터 배열을 한 번에 memcpy 수준으로 복사(원소 객체 자체 복사 아님)하지만, 그 포인터 배열 자체가 매우 큼.
# “실무 관점(메모리/안정성 포함)”에선 슬라이싱은 보통 회피 대상임
# 이후 for x in tmp는 리스트 iterator가 연속 메모리를 순차 접근 → 반복 오버헤드가 더 작음/캐시 친화적
# 100,000,000개면 포인터만 대략 8바이트 * 1e8 = 800MB 수준(64-bit 기준) 추가 필요

## 3. 이터레이터
@time_check
def find_max_iter(numbers):
    it = iter(numbers)
    max_num = next(it)
    for num in it:
        if num > max_num:
            max_num = num
    return max_num
# 슬라이싱의 장점(빠른 iterator)을 살리고, 복사 비용을 제거하는 방식.
# 추가 리스트 생성 없음, 인덱싱 없음, CPython에서 보통 가장 합리적인 형태

# 테스트
input = list(range(100000000))
print(find_max(input))
print(find_max_slicing(input))
print(find_max_iter(input))

# 연산 횟수 계산식
# 비교 연산: n-1회 -> 총 연산 횟수: n-1
# bigO: O(n)