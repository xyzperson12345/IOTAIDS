/*Write C++ program for storing binary number using doubly linked lists. Write functions
a) To compute 1„s and 2„s complement
b) Add two binary numbers*/
#include<iostream>
#include<string>
using namespace std;
int count;
struct node{
	node* prev;
	int bit;
	node* next;
};

class linklist{
	public:
		node* head;
		node* tail;
		
		linklist(){
			head=NULL;
			tail=NULL;	
		}		
		void insert();
		void display();
		void ones_compliment();
		void twos_compliment();		
	
};

void linklist::insert(){
	node* nnode;
	char ch;
	int n;
	cout<<"Enter no. of bit you want to Enter:";
	cin>>n;
	for(int i=0;i<n;i++){	
	node* nnode;
	nnode= new node;
	cout<<"Enter BIT:";
	cin>>nnode->bit;
	nnode->next=NULL;
	if(head==NULL && tail==NULL){
		head=tail=nnode;
	}
	else{
		
		tail->next=nnode;
		nnode->prev=tail;
		tail=nnode;
	}
}
}

void linklist::display(){
	node* temp;
	temp=head;
	while(temp!=NULL){
		cout<<temp->bit;
		temp=temp->next;
	}
}

void linklist::ones_compliment(){
	node* temp;
	temp=head;
	while(temp!=NULL){
		if (temp->bit==1){
			cout<<0;
		}
		else{
			cout<<1;
		}
		temp=temp->next;
	}		
}
void linklist::twos_compliment() {
    node* temp;
    temp = tail;
    int flag = 0;

    cout << "2's Complement: ";
    while (temp != NULL) {
        if (flag == 0) {
            if (temp->bit == 0) {
                cout << 0;
            } else {
                cout << 1;
                flag = 1;
            }
        } else {
            if (temp->bit == 0) {
                cout << 1;
            } else {
                cout << 0;
            }
        }
        temp = temp->prev;
    }
    cout << endl;
}
int main(){
	linklist l;
	l.insert();
	cout<<"Entered binary number is:";
	l.display();
	cout<<endl;
	cout<<"Ones compliment of binary number is:";
	l.ones_compliment();
	cout<<endl;
	cout<<"Twos compliment of binary number is:";
	l.twos_compliment();
	cout<<endl;
	
	return 0;
}

