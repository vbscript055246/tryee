# 關於怎麼得到數列的"思維"
# 首先分析"collatz猜想"本身"定義"
#
# 給一個正整數, [我給你全世界(誤)]
# 對這個數 奇的 乘3倍+1
#         偶的 除與2
#
# 所以你會的到一個新的"正整數"
# 然後得到一個"正整數"了~對吧~, 你知道該怎麼做了吧~嘿嘿嘿~
# 所以就一直重複做, 直到什麼時候停止呢? 正整數等於1的時候


# 實作層面
# 首先你有一個"最初的正整數"
# 然後重複地做 奇數... 偶數... 的事
# 到"1"的時候記得"停下來"


# 所以我要先"有"一個正整數, 所以用input()沒問題吧~
# 但輸入的是"文字"記得int()包在input外, 把型態轉成"整數"

# 怕有人不知道 宣告 num = 123 跟 num = "123" 是不一樣的
# 第一個 num 裡面裝的是數字 可以計算(可加減乘除)
# 第二個 num 裡面裝的是文字 不可以計算(不可加減乘除)

# 所以這跟input 外面要包 int 的道理是一樣的
# 因為我們想要"數字" 不是"文字" (為什麼想要"數字"是等等要對它 奇數... .偶數... 對吧~)

# 由上面 我們可以得到
num = int(input())


# 接著如果奇數...(做一些事)
#     如果偶數...(做一些事)

# 先想數字是否"非奇即偶"
# 所以我們可以改成
# 如果奇數..., 否則 (做一些偶數做的事)...
# 轉成語法:
# if 奇數 :
#   (做一些事)
# else:
#   (做一些事)

# 此時發現個問題, 我們要"怎麼判斷是奇數還是偶數"(數學問題...大家自己加油~)
# 最簡單的方法: "除與2除不盡的"就是奇數, 但問題又來了
# 怎麼表示"除不盡", 看除了之後有沒有小數點,OK但不夠簡單
# 程式中有種"運算符號"(英文叫"operator", 就是跟"加減乘除"一樣), 有取得"餘數"的功能
# 小複習: 被除數/除數 = 商數 ... "餘數"
#          7  /  2  =  3  ...   1
# 這個符號就是 "%"
# 所以我們可以運用取餘數得到判斷奇數的方法為: "num % 2 == 1" ,此時的num為奇數
# 再搭配"collatz猜想"原先的定義
# 得到程式碼

if num % 2 == 1:
    num * 3 + 1
else:
    num / 2


# 此時你取得了"新的正整數"了
# 但你必須為"下一次的運算"做準備(除非你拿到"1"了)
# 你的程式也執行到了

# 0 num = int(input())
# 1                        <------想辦法回到這行
# 2 if num % 2 == 1:
# 3     num * 3 + 1
# 4 else:
# 5     num / 2
#                           <------這一行

# 先假設裡面的數不是"1" (因為大多數的狀況 不是1對吧~ 之後再把1挑出來特別處理就好)
# 所以你要再做一遍, 因此你要"設法回到"行號1的位置
# while迴圈 在向你招手朋友~

# 先教怎麼選擇要用 while 還是 for
# 簡單說一句話就是 你要怎麼停止迴圈 回到那一行, 你要在怎樣的狀況下 停止這個迴圈
# for 是"沒判斷"的 也就是它是個計數器 "做某個次數" 停!!!
# while 是"有判斷"的 它可以在任何你想設定的狀況下停
# 舉例: 你知道 collatz(27)要執行幾次才會停嗎?(或是collatz(27)數列有幾個數?)
# 不知道對吧~ 所以你應該用while迴圈 因為你不知道 for迴圈要做幾次
# 所以我們可以得到程式碼:

# num = int(input())
# while 不停止的條件:
#   if num % 2 == 1:
#       num * 3 + 1
#   else:
#       num / 2

# 不停止的條件 不用多說 就是 num != 1
# 可能有人會問說 為什麼是"不停止的條件", 因為while是當"條件敘述"為真(True), 才持續執行
# 所以要是"不停止的條件"

# 可是問題又來了

# num = int(input())
# while num != 1:
#   if num % 2 == 1:
#       num * 3 + 1
#   else:
#       num / 2


# 執行一次給大家看

# num = int(input())    <---- 執行這行, 取到num的值, 假設我輸入27, 此時 num = 27
# while num != 1:
#   if num % 2 == 1:
#       num * 3 + 1
#   else:
#       num / 2


# num = int(input())
# while num != 1:      <---- 執行這行, num = 27, 不等於 1, 進入while迴圈
#   if num % 2 == 1:
#       num * 3 + 1
#   else:
#       num / 2


# num = int(input())
# while num != 1:
#   if num % 2 == 1:    <---- 執行這行, num = 27, num % 2 等於 1, 進入if分支
#       num * 3 + 1
#   else:
#       num / 2


# num = int(input())
# while num != 1:
#   if num % 2 == 1:
#       num * 3 + 1     <---- 執行這行, num = 27, num * 3 + 1 等於 82, 離開if結構
#   else:
#       num / 2


# num = int(input())
# while num != 1:       <---- 執行這行, num = 27, 不等於 1, 進入while迴圈
#   if num % 2 == 1:
#       num * 3 + 1
#   else:
#       num / 2


# 等等等等 你發現了什麼...?!
# num的值沒被新的算出來的新正整數取代
# 所以      num         =    num * 3 + 1
#     (原本就的正整數)  (寫入) (新算出來的)
# 所以我們可以得到程式碼:

num = int(input())
while num != 1:
    if num % 2 == 1:
        num = num * 3 + 1
    else:
        num = num / 2

# 教到這邊, 基本的程式設計思維教完了 (自己的作業還是要自己寫 上面得程式碼是執行結果不對的)
# 之後更新會補充函數跟變數使用的一些細節

# 函數篇

# 先不談該死的python特性, 這東西原理來自跟它同名同姓的數學朋友, 我們姑且以 y=f(x) 的數學方程式來比較
# 我們在數學上"定義"一個方程式   f(x) = 2*x

# python"定義"一個方程式       def f(x):    <----def是英文defined
#                               2*x
#
# 然後我們講義點function在程式中的特性
# function中文別名: 函式 函數
# 首先如果我們要使用"定義過的函式", 向上面的f(x)
# 在程式碼中使用 "f()" 來"使用"(這邊的使用也有專有名詞: 呼叫 又稱call)
# "呼叫"的時候, 小括弧裡面的東西, 也有專有名詞我們稱為"參數"
# 而參數的意義就跟數學當x = 3, f(x) = 2 * 3,的"3"一樣, 它會根據"定義"被代入
# 所以如果你呼叫f(3)
# 上面的函式在執行的時候就會是:
# def f(3):
#    2 * 3
#
#
# 再講一個跟數學不一樣的地方
# 數學      y = f(3) => y = 6, 這無庸置疑
# python   y = f(3) => y = None, WTF!?
#
# 這時大家要意識到 function的"定義"是有問題的, 結果才會亂噴~
# 就讓我們來檢查定義
# def f(x):
#    2 * x
#
# 我們必須"設定"一個當它要"等於"的值, 這"等於"的"值"也有專有名詞: "回傳值"
# 因為不然不知道要"等於"函式中的哪個值
# 假設:
#     def g(x):
#       2 * x
#       3 * x
#
# g(3) 該"等於"? 電腦不知道, 所以要設定
#
# 所以我們用"return"關鍵字 來放在要傳的那行的值的最前面 來標示
# def f(x):
#   return 2 * x
#
# 所以現在:
# 數學      y = f(3) => y = 6
# python   y = f(3) => y = 6
#
#
# 補充一些"變數"使用的小細節
#
# 首先變數有分"區域變數" 和 "全域變數"
# 為啥程式有分 "全域" "區域"
# 是因為"變數"其實有"生命週期", 電腦為了節省儲存空間, 在特定的範圍內會把資料清空
# 顧名思義 區域變數 => "區域"裡面的變數
# "區域" 通常指的是"一個迴圈內"或"一個函式內", 也就是在上述兩個地方內部裡面宣告的變數
# 在"離開該區域"時, 變數會"被回收掉"
#
# for i in range(5):
#     pass
#
# i 在離開迴圈時, 會消失
#
# def func(x):
#   a = 1
#   b = 4
#
# x, a, b 在離開func()時, 會消失
#
#
# "全域變數" 就是整個程式執行的時候都用的是同一個的變數
# 不管再哪裡都一樣, 但python其實沒辦法直接生成這種變數
#
# 當區域與全域發生衝突? 當"兩種變數"取同"一個名稱"的時候會發生, 大多數語言優先採用"區域變數"
#
# 當區域與區域發生衝突? 選擇區域較小的優先使用
#
# 所以牛刀小試一下?
#
# number = 100
#
# def func(number):
#     number = number + 1
#
# func(number)
# print(number)
#
# 印出來是多少呢?
# Ans:100
#
# 解釋一下
#
# 最外層的變數 也是"區域變數"
# 然後呼叫的時候, 只是把外面的number的值, 存到func裡面的number的值
# 兩邊是沒有關係的
# (有別的呼叫方式, 但python很難寫出來, 請看專案首頁的補充, python的這種傳"值"來呼叫的方式, 有專有名詞:call by value)
#
# 另外提一下python 並沒有設計錯誤或是全域變數可以被完全取代
# 所以它提供的一種關鍵字"global"放在你想要用的"區域"裡面
# 語法是: global 變數名稱, 在該區域該名稱變數與外面相同
#
#




# =============================================================================

# 原本以為上課上的大家都會, 想給大家一些新東西嘗嘗...sorry~  QAQ 不要怕拿些基本的問題我喔~

def collatz(x):
    if x <= 0: print("no");return
    while x != 1:x = (3 * x + 1) if (x & 1) else x // 2;print(x)

collatz(int(input("請輸入:\n")))



