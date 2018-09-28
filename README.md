# tryee
##### 想要我的code嗎？想要的話可以全部給你，去找吧！我把code都放在這裡了~
##### (有問題就私下密吧~)
#### 想執行程式碼卻沒有環境可以用[ideone](https://ideone.com/ideone/Index/submit/)直接線上編譯喔~
#### 寫Python的IDE,我推[Pycharm](https://www.jetbrains.com/pycharm/download/#section=windows)[教學]()
### 補充
 - pointer
一句話: 儲存變數記憶體位址的變數
> 假設有個變數 A
> 既然是"變數"就會住在"記憶體上的某個角落"
> 也就表示是每個"變數"都會有他家"住址"
> 然後"住址"就是所謂"pointer"
> "pointer"可以用專門的變數型態儲存
- reference
一句話: pointer的改良版,比它省資源(記憶體),也比較好寫

- 應用
> 函數傳參數時,如果想更改傳進來的參數的值
> 以C來說,假設你想寫個swap(a,b)
```C
    void swap(int a,int b){
        int temp = a;
        a = b;
        b = temp;
    }
```
> 這樣是無法更改原值的
> 原因是swap(int a,int b)這樣的函式 屬於所謂"call by value"
> 簡單來說就是只把便參數的值傳進函式
> 所以在函式在執行時,被操作的變數跟原來的不一樣,只是原先的複製體
> 如果使用swap(int *a,int *b):   \[int *是儲存指標的變數型態\]

``` C
    viod swap(int *a,int *b){
    //注意 a 裡面儲存的是變數的位址
//從位址存取變數資料需要"dereference" (在儲存著指標的變數前+*)
    //所以不可以寫int temp = a;這樣會是把a裡面的地址拿出來
        int temp = *a;
        *a = *b;
        *b = temp;
    }
```
> 在傳參數時也要注意 需要用&+在傳入的參數前 來取得變數的位址
> 而reference的傳法跟原本一樣
> 只是在函是宣告時使用void swap(int &a,int &b)
- 其他語言
    -- Java 都是reference
    -- python 有方法硬傳reference


    
