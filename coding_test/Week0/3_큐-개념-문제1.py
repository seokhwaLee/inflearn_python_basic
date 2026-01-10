# 문제1
# 배열을 사용하여 큐를 구현하는 가장 간단한 방법을 '선형 큐'라고 합니다. 
# 이 방식에서는 front와 rear 두 개의 포인터(또는 인덱스)를 사용하여 큐의 시작과 끝을 관리합니다. 
# Dequeue 연산이 반복적으로 수행될 때, front 포인터가 계속 증가하면서 배열 앞부분에 사용되지 않는 공간이 누적됩니다. 
# 이러한 메모리 비효율성 문제를 무엇이라고 하며, 이 문제를 해결하기 위한 큐의 개선된 형태는 무엇인가요? 
# 그리고 그 개선된 방식이 어떻게 메모리를 효율적으로 재사용하는지 그 동작 원리를 설명하세요.

# 답변:
# 배열을 사용하여 큐를 구현할 때, Dequeue 연산이 반복적으로 수행되면서 front 포인터가 계속 증가하여 
# 배열 앞부분에 사용되지 않는 공간이 누적되는 문제를 '메모리 낭비' 또는 '공간 낭비'라고 한다. 
# 이 문제를 해결하기 위한 큐의 개선된 형태는 '원형 큐'이다. 
# 원형 큐는 배열의 끝이 다시 시작으로 연결되어 있는 구조로, rear 포인터가 배열의 끝에 도달하면 다시 배열의 처음으로 돌아가며,
# 사용되지 않은 공간을 재사용할 수 있다. 이 방식은 큐의 공간을 효율적으로 활용하여 메모리 낭비를 줄일 수 있다.
# 원형 큐의 동작 원리는 다음과 같다:
# 1. Enqueue 연산 시, rear 포인터가 배열의 끝에 도달하면, rear를 배열의 처음으로 이동시킨다.
# 2. Dequeue 연산 시, front 포인터가 배열의 끝에 도달하면, front를 배열의 처음으로 이동시킨다.
# 3. 이렇게 함으로써, 배열의 앞부분에 비어 있는 공간이 생기더라도, rear 포인터가 그 공간을 다시 사용할 수 있게 된다.
# 4. 원형 큐는 front와 rear 포인터가 서로 겹치지 않도록 관리하여, 큐가 가득 찼는지 또는 비어 있는지를 판단할 수 있다.
# 이러한 원형 큐의 구조는 메모리를 효율적으로 재사용할 수 있게 하여, 큐의 성능을 향상시킨다.

# 원형 큐 함수
class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.rear = 0 # 큐의 가장 왼쪽 부분을 가리키는 포인터
        self.front = 0 # 큐의 가장 오른쪽 부분을 가리키는 포인터
        self.count = 0 # 큐에 들어있는 원소의 개수

    def is_full(self):
        return self.count == self.size

    def is_empty(self):
        return self.count == 0

    def enqueue(self, item):
        if self.is_full():
            raise Exception("Queue is full")
        self.queue[self.front] = item
        self.front = (self.front + 1) % self.size
        self.count += 1

    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        item = self.queue[self.rear]
        self.queue[self.rear] = None
        self.rear = (self.rear + 1) % self.size
        self.count -= 1
        return item

# 테스트 예시
cq = CircularQueue(5)
cq.enqueue(1)
cq.enqueue(2)
cq.enqueue(3)
print(cq.rear, cq.front)  # 출력: 0 3
print(cq.dequeue())  # 출력: 1
print(cq.rear, cq.front)  # 출력: 1 3
cq.enqueue(4)
print(cq.rear, cq.front)  # 출력: 1 4
cq.enqueue(5)
print(cq.rear, cq.front)  # 출력: 1 0 (front가 배열의 처음으로 돌아감)
print(cq.queue)  # 출력: [None, 2, 3, 4, 5]
cq.enqueue(6)
print(cq.queue)  # 출력: [6, 2, 3, 4, 5]
print(cq.rear, cq.front)  # 출력: 1 1
