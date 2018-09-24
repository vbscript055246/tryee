#include <iostream>
using namespace std;

class node{ //有使用static member
	public:
		static int count; 
		node(){		//建構式
			count++;
		}
			
};
int node::count = 0; //static member initialize


class Node{ //沒有使用static member
	public:
		int count; 	
		Node():count(0){ //建構式
			count++;
		}
};


int main(){
	//有使用static member
	node a;
	node b;
	cout << a.count << "\n";
	a.count = 1;
	b.count = 0;
	cout << a.count << "\n";
	//大家的count是同一個
	
	//沒有使用static member
	Node A;
	Node B;
	cout << A.count << "\n";
	A.count = 1;
	B.count = 0;
	cout << A.count << "\n";
	//大家的count是不同的
} 
