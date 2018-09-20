#include <iostream>
using namespace std; 


class Extends{
	public:
		Extends(){
			n+=1;
		}
		int get_n(){
			return n; 
		} 
	private:
		static int n;
};

static int num;
int main(){
	Extends A;
	cout << A.get_n();
	Extends B;
	cout << A.get_n();
	return 0; 
}
