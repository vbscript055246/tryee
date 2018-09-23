#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <cstdlib>
#include <ctime>
using namespace std;

// 作業1
class Animal{
	public:
		string move(){return "動";}
};

class Cat:public Animal{
	public:
		virtual string move(){return "跳";} //Java預設所有的函式都有加 virtual
};											//反而提供了final來阻止子類別 functionoverload

class Tiger:public Cat{
	public:
		string move(){return "跑";}

		string skill(){return "獵殺";}
};


//作業2
class Demo{
	public:
		Demo():divider(1){}

		float getDivider(){return divider;}

		void setDivider(int div){
			if(div == 0) cout << "Divider can not be 0 !\n";
			else divider = div;
		}

		void dataHidingDemo(int number){
			float result = number/divider;
			cout << result << "\n";
		}

		static void main(){
			Demo demo;
			demo.setDivider(0);
			demo.dataHidingDemo(50);
		}
	private:
		int divider;
};


//作業3
//C語言版
int minimum(int *array,int n){
	int i,index,min = 99999999;
	for(i=0;i<n;i++){
		if(array[i]<min){
			min = array[i];
			index = i;
		}
	}
	return index;
}

void swap(int *a,int *b){ //call by pointer
	*a^=*b;
	*b^=*a;
	*a^=*b;
}

void SelectionSort(int *array,int n){
	int i;
	for(i=0;i<n;i++){
		int index = minimum(array,n-i);
		swap(array[n-i-1],array[index]);
	}
}

//C++語言版
void SelectionSort(vector<int> &array){ //call by reference
	for(int i=0;i<array.size();i++){
		vector<int>::iterator result = min_element(array.begin(),array.begin()+array.size()-i);
		array.push_back(*result);
		array.erase(result);
	}
}

//作業5
void binarySearch(vector<int> array,int target){ //call by value
	int mid = array.size()/2;
	if(array.size() == 1 && target != array[0]){
		cout << "Not found!!!" << endl;
		return;
	}

	if(target == array[mid]) cout << "found!!!" << endl;
	else{
		vector<int> temp;
		if(array[mid] > target)
			temp.assign(array.begin(),array.begin()+mid);
		else
			temp.assign(array.begin()+mid,array.end());
		binarySearch(temp,target);
	}
}


int main() {

	Cat cat;
	cout << cat.move() << "\n";
	Tiger tiger;


	//這裡就可以看出每種語言會有不同特性
	//而一切的起點都在這裡
	//Tiger可以被所有的父類別的指標變數儲存
	//可是在不同的容器下函式作用是不同的
	Cat *cat2 = &tiger;
	cout << cat2->move() << "\n";

	Tiger *tig = &tiger;
	cout << tig->move() << "\n";
	cout << tig->skill() << "\n";

	Animal *mal = &tiger;
	cout << mal->move() << "\n";
	/*
	執行結果:
		跳
		跳
		跑
		獵殺
		動
	*/

	cout << endl;

	Demo D;
	D.main();

	cout << endl;

	srand(time(NULL)); // 亂數初始

	int array[25]={0};
	for(int i=0;i<25;i++) array[i] = rand()%(1001);
	SelectionSort(array,25);
	for(int i=0;i<25;i++) cout << array[i] << endl;

	cout << endl;

	vector<int> matrix;
	for(int i=0;i<25;i++) matrix.push_back(rand()%(1001));
	SelectionSort(matrix);
	for(int i=0;i<matrix.size();i++) cout << matrix[i] << endl;

	binarySearch(matrix,rand()%(1001));
}
