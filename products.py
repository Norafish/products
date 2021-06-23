# import標準函式庫、別人寫好的程式
import os # operating system作業系統模組
products = [] 
if os.path.isfile('products.csv'): # os模組的path路徑 # 相對路徑，檢查同一個資料夾是否有這個檔案 
	print('找到檔案了! ') # 讀取檔案
	
	with open('products.csv', 'r', encoding = 'utf-8') as f: #寫入跟讀取檔案都要用同一個編碼
		for line in f:
			if '商品,價格' in line:
			continue #continue跟break一樣，只能寫在迴圈，continue為直接跳到下一迴，break為跳出迴圈
			name, price = line.strip().split(',') #先把一行的尾巴換行去掉，再用逗點當切割標準 #切割完的結果是清單 #切割完直接存到name(p[0])和price(p[1])
			products.append([name, price]) #順利讀取檔案
else:
	print('找不到檔案')


# 讓使用者輸入新的商品
while True:
	name = input('請輸入商品名稱: ')
	if name == 'q':	
		break
	price = input('請輸入商品價格: ')
	price = int(price)
	products.append([name, price])
# 印出所有購買紀錄
for p in products:
	print(p[0], '的價格是', p[1])
# 寫入新檔案
with open('products.csv', 'w', encoding = 'utf-8') as f:
	f.write('商品,價格\n')
	for p in products:
		f.write(p[0] + ',' + str(p[1]) + '\n')