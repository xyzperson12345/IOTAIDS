/* A double-ended queue (deque) is a linear list in which additions and deletions may be
made at either end. Obtain a data representation mapping a deque into a one dimensional
array. Write C++ program to simulate deque with functions to add and delete elements from
either end of the deque*/
#include <iostream>
#define MAX 10

class Deque {
private:
    int arr[MAX];
    int front;
    int rear;
    int size;

public:
    Deque() 
	{
        front = -1;
        rear = 0;
        size = 0;
    }

    bool isFull() 
	{
        return (size == MAX);
    }

    bool isEmpty() 
	{
        return (size == 0);
    }

    void insertFront(int element) 
	{
        if (isFull()) 
		{
            std::cout << "Deque is full\n";
            return;
        }
        if (front == -1) 
		{
            front = 0;
            rear = 0;
        } else if (front == 0) 
		{
            front = MAX - 1;
        } else {
            front--;
        }
        arr[front] = element;
        size++;
    }

    void insertRear(int element) {
        if (isFull()) {
            std::cout << "Deque is full\n";
            return;
        }
        if (front == -1) {
            front = 0;
            rear = 0;
        } else if (rear == MAX - 1) {
            rear = 0;
        } else {
            rear++;
        }
        arr[rear] = element;
        size++;
    }

    void deleteFront() {
        if (isEmpty()) {
            std::cout << "Deque is empty\n";
            return;
        }
        if (front == rear) {
            front = -1;
            rear = -1;
        } else if (front == MAX - 1) {
            front = 0;
        } else {
            front++;
        }
        size--;
    }

    void deleteRear() {
        if (isEmpty()) {
            std::cout << "Deque is empty\n";
            return;
        }
        if (front == rear) {
            front = -1;
            rear = -1;
        } else if (rear == 0) {
            rear = MAX - 1;
        } else {
            rear--;
        }
        size--;
    }

    int getFront() {
        if (isEmpty()) {
            std::cout << "Deque is empty\n";
            return -1;
        }
        return arr[front];
    }

    int getRear() {
        if (isEmpty()) {
            std::cout << "Deque is empty\n";
            return -1;
        }
        return arr[rear];
    }
};

int main() {
    Deque dq;
    dq.insertRear(5);
    dq.insertRear(10);
    std::cout << "Rear element: " << dq.getRear() << std::endl;
    dq.deleteRear();
    dq.insertFront(15);
    std::cout << "Front element: " << dq.getFront() << std::endl;
    dq.deleteFront();
    return 0;
}


