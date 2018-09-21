#include <iostream>
using namespace std;
 
// 集合元素儲存狀態
enum Status{empty,occupied};
 
// 集合類別
class Set{

	private:// 權限控制宣告 以下的部分限"自己"使用 也就是不管是"誰" 就是只有"本物件"可以用 
		// Default_Size : 預設的集合最小可儲存元素的個數
   		// Inc_Size     : 每次增加的元素個數
   		//enum 宣告特定字串代表一個值,如果不指定則順著前面的編號遞增
   		enum{Default_Size = 10,Inc_Size=20};
   		
   		int	*element;       // 元素
   		Status *status;     // 元素儲存狀態
   		int element_no;     // 已儲存的元素個數
   		int max_element_no; // 可儲存的元素個數

	public://權限控制宣告 以下的部分"大家"都可以用 包括被他人include之類的 
   		
		//建構函式 Set() 
		//物件在被"宣告時"做的事 
		Set():element_no(0),max_element_no(Default_Size){
			//element_no(0) 就是 element_no=0;
			//max_element_no(Default_Size) 就是 max_element_no=0;
			
			// new int[大小] 就是 malloc(sizeof(int)*大小) 
       		element = new int[Default_Size];
       		status = new Status[Default_Size];
       		
       		for(int i=0;i<Default_Size;++i)	
			   status[i] = empty ;
   		}
 
   		//解構函式  ~Set()
   		//當物件被釋放記憶體時會做的事 
		~Set(){ 
			delete [] element;// delete 變數名稱 就是 free(變數名稱) 
			delete [] status; // delete [] 變數名稱 就是 根據"陣列頭的指標"去釋放"整串陣列 "的記憶體 
		}
  
   		//複製函式  名稱跟建構式重複了 
		//這邊的操作是所謂函式重載(function overload)
   		//當物件的函式 有名稱相同但參數不同時會根據"輸入的變數型態"選擇要執行的函式 
 		// 複製建構函式
		Set(const Set &set){
		 
		   element_no = set.element_no;
		   max_element_no = set.max_element_no;
		      
		   element = new int[max_element_no];
		   status = new Status[max_element_no];
		      
		   for(int i=0;i<max_element_no;++i){
		       element[i] = set.element[i];
		       status[i] = set.status[i];
		   }
		 
		}
		
   		// 加入元素
		void insert_element(int data){
			int i;
			// 如果現有的元素個數已經滿了, 則須另尋空間儲存
   			if(element_no==max_element_no)
			{
			   int *tmp_element = new int[max_element_no+Inc_Size];
			   Status *tmp_status = new Status[max_element_no+Inc_Size];
      
			       // 複製現有元素到新的記憶空間
       			for( i = 0 ; i < max_element_no ; ++i ) {
           			tmp_element[i] = element[i] ;
           			tmp_status[i] = status[i] ;
        		}
      
       			// 儲存新元素
       			tmp_element[max_element_no] = data ;
       			tmp_status[max_element_no] = occupied ;
 
       			for(i=1;i<Inc_Size;++i)
          			tmp_status[max_element_no+i] = empty ;
      
       			// 釋放舊記憶空間
       			delete [] element;
				delete [] status;
      
       			element=tmp_element;
       			status=tmp_status;
      
       			max_element_no+=Inc_Size;
       			++element_no;
      
   			}
			else{
       			// 原有空間已夠用, 直接增加一個元素
       			for (i=0;i<max_element_no;++i)
				{
           			if (status[i]==empty)
					{
               			element[i]=data;
               			status[i]=occupied;
               			++element_no;
               			return;
           			}
       			}
			}
		}
  
   		// 刪除元素
		int delete_element(int data){
	   		// 定義變數表示刪除元素的個數
			int no_element_deleted=0;
			for(int i=0;i<max_element_no;++i){
			    // 尋找到元素後刪除
			    if(status[i]==occupied&&element[i]==data){
			        status[i]=empty;
			        --element_no;
			        ++no_element_deleted;
			    }
			 
			}
			return no_element_deleted;
		}
  
   		// 列印元素
		void print_set(){
		   cout << "集合有" << element_no << " 元素: ";
		   for(int i=0;i<max_element_no;++i)
		       if(status[i]==occupied)cout << element[i] << ' ';
		   cout << endl;
		}
		
		
		
		//運算子宣告
		//任何"自創物件"本身是沒有宣告任何運算子的(不像 int,float,double
		//換句話說就是沒有+ - * / = %更沒有 ++,-=,? : 
		//所以如果你想使用運算子
		//就要自己定義
		//怎麼定義呢?
		//首先 要先理解 + - * / = %,的"左右"必定"各有一個物件"
		//左邊的物件的"函式"會因為"使用運算子"被"呼叫"
		//至於呼叫函式時的"參數"就是"右邊的物件"
		
		//定義指定運算子 (call by reference)
		void operator=(const Set &set){
		   // 如果所欲複製的集合類別的元素較現有的空間多,
		   // 則須要重新分配空間, 否則利用現有的空間即可
		   if(set.element_no>max_element_no){
		      
		       element_no     = set.element_no;
		       max_element_no = set.max_element_no;
		      
		       int   *tmp_element = new int[max_element_no];
		       Status *tmp_status = new Status[max_element_no];
		      
		       for(int i=0;i<max_element_no;++i){
		           tmp_element[i] = set.element[i];
		           tmp_status[i]  = set.status[i];
		       }
		 
		       // 釋放現有的記憶空間
		       delete [] element;
			   delete [] status;
		 
		       // 使用新記憶空間
		       element = tmp_element;
		       status  = tmp_status;
		 
		   }
		   else {
		 
		       int i , c = 0 ;
		       element_no = set.element_no ;
		 
		       // 重新分配元素
		       for ( i = 0 ; i < set.max_element_no ; ++i ) {
		           if ( set.status[i] == occupied ) {
		               element[c] = set.element[i] ;
		              status[c] = occupied ;
		               ++c ;
		           }
		       }
		 
		       for ( i = c ; i < max_element_no ; ++i )
		           status[i] = empty ;
		 
		   }
		 
		}
		
   		//定義比較元素 (call by reference) 回傳真假值 
   		bool operator==(const Set &set)
		{
			if(set.element_no == element_no){
				for(int i=0;i<max_element_no;++i){
					if(status[i]==occupied){
						bool flag=1;
						for(int j=0;j<set.max_element_no;j++)
							if(set.status[j]==occupied&&set.element[j]==element[i]) flag=0;
						if(flag) return false;
					}
				} 
				return true;
			}
			return false;
		}
};
 
int main(){
	
	//宣告變數 觸發建構式 
	Set set1;
   	// 儲存20個 個位數元素
   	for(int i=0;i<20;++i) set1.insert_element(i%10);
   	
   	//使用物件1的函式 print_set()
   	set1.print_set();
   	
   	// 測試複製函式 -> 宣告set2 -> 觸發建構式 -> 根據參數 -> 選擇執行複製函式 
   	Set set2(set1);
   	
   	//使用物件2的函式 print_set()
   	set2.print_set();
   	
   	// 增減集合元素  使用物件insert_element() delete_element()
   	set2.insert_element(5); 
   	set2.insert_element(9);
   	set2.delete_element(3); 
   	set2.delete_element(0);
   	set2.print_set();
 	
	// 測試指定運算子
   	set1 = set2; //觸發 void operator=(const Set &set)
   	set1.print_set();
	   
	if(set1 == set2){ //bool operator==(const Set &set)
		cout << "OK!!!" << endl;
	}
   	else cout << "shit!!!" << endl;
 
   return 0 ;
  
}

