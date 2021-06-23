# 讀取檔案

products = []
with open('products.csv', 'r', encoding = 'utf-8') as f: #寫入跟讀取檔案都要用同一個編碼
	for line in f:
		if '商品,價格' in line:
			continue #continue跟break一樣，只能寫在迴圈，continue為直接跳到下一迴，break為跳出迴圈
		name, price = line.strip().split(',') #先把一行的尾巴換行去掉，再用逗點當切割標準 #切割完的結果是清單 #切割完直接存到name(p[0])和price(p[1])
		products.append([name, price]) #順利讀取檔案
# 讓使用者輸入
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
# 寫入檔案
with open('products.csv', 'w', encoding = 'utf-8') as f:
	f.write('商品,價格\n')
	for p in products:
		f.write(p[0] + ',' + str(p[1]) + '\n')