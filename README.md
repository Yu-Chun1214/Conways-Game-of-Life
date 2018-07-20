# X-Village-Challange

pattern.py是去做pattern的處裡，例如題目一開始給的初始化地圖等。另外如果輸入的pattern值超過3則會再pattern.py裡製造出新的地圖。
在gameoflife裡的def set_pattern是去把遊戲的地圖生出來。
裡面包括將題目的地圖定位在遊戲地圖的正中間(call def __pattern_manage() and def __position())或是call pattern.pattern_maker()去製造出新的地圖

函數play裡會call def __life()，這個函數會回傳附近的細胞生命狀態，而def __count_of_life()則是會判斷下一個generation要變成什麼樣的生命狀態。 

