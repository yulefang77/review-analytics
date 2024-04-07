data = []
count = 0
with open('reviews.txt', 'r') as f:
    for line in f:
        data.append(line)
        count += 1
        if count % 10000 == 0:
            print(len(data))
print('留言檔案讀取結束，總共', len(data), '筆資料。')

sum_len = 0
for d in data:
    sum_len += len(d)
print('每筆留言平均長度', sum_len / len(data), '個字母。')


new = []
for d in data:
    if len(d) < 100:
        new.append(d)
print('總共有', len(new), '筆留言長度小於100個字母。')
print('以下印出前2筆留言長度小於100個字母的內容。')
print('--------------------')
print(new[0])
print('--------------------')
print(new[1])


good = []
for d in data:
    if 'good' in d:
        good.append(d)
print('總共有', len(good), '筆留言內容提到good。')
print('印出第一筆留言內容。')
print('--------------------')
print(good[0])


wc = {} # world count
for d in data:
	words = d.split()
	for word in words:
		if word in wc:
			wc[word] += 1
		else:
			wc[word] = 1
		break

while True:
	word = input('請輸入你想查詢的關鍵字: ')
	if word in wc:
		print(word, '一共出現過', wc[word], '次。')
	else:
		print('這個字沒有出現過喔！')
		break
print('感謝你使用查詢服務！')