def is_queue_full() :
    global queue, front, rear
    if front == rear and queue[rear] is not None:
        return True
    return False

def is_queue_empty() :
    global queue, front, rear
    if front == rear and queue[front] is None:
        return True
    return False

def en_queue(data) :
    global size, queue, front, rear
    if is_queue_full():
        print("큐가 꽉 찼습니다.")
        return
    rear = (rear + 1) % size
    queue[rear] = data
    print(rear)

def de_queue() :
    global size, queue, front, rear
    if is_queue_empty():
        print("큐가 비었습니다.")
        return None
    front = (front + 1) % size
    data = queue[front]
    queue[front] = None
    print(front)
    return data

def peek() :
    global size, queue, front, rear
    if is_queue_empty():
        print("큐가 비었습니다.")
        return None
    return queue[(front+1)%size]

size = int(input("큐의 크기를 입력 : "))
queue = [None for _ in range(size)]
front = rear = 0

if __name__ == "__main__" :
    while True:
        menu = input("삽입(E)/삭제(D)/확인(P)/종료(X) : ")
        if menu == 'X' or menu == 'x':
            break
        elif menu== 'E' or menu == 'e' :
            data = input("입력할 데이터 : ")
            en_queue(data)
            print(queue)
        elif menu== 'D' or menu == 'd' :
            print("삭제된 데이터 : ", de_queue())
            print(queue)
        elif menu== 'P' or menu == 'p' :
            print("확인된 데이터 : ", peek())
            print(queue)
        else:
            print("입력이 잘못됨")
    print("프로그램 종료!")