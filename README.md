# line-bot.py

今天要吃什麼？

* 店家資料庫
* 輸入「吃什麼」，程式就從資料庫中隨機挑一筆出來
* 輸入「#新增店家 龍品魚丸」，就把店家名稱加入資料庫中[:5]
 ---
 
import random

1. 如果使用者訊息含有「吃什麼」，就進入「選擇店家」函式
1. 讀取店家資料庫store_data
1. 產生一個從0到資料庫長度的隨機數
1. 將符合的店家名字印出 
 
 
 
 random_num = random.random()
 
 store_data = [龍品魚丸, 原食, 濰克]
 if '吃什麼' in msg:
 
    
 