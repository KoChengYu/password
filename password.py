# 密碼重設程式
# password = 'a123456'
# 讓使用者重複輸入密碼
# 最多輸入三次
# 若密碼正確 則印出 "登入成功!"
# 若密碼錯誤 則印出 "密碼錯誤! 還有_次機會!"

password = 'a123456'
i = 3
while i > 0: # or True
	pwd = input('請輸入密碼: ')
	if pwd == password:
		print('登入成功!')
		break # 逃出迴圈
	else:
		i = i - 1
		print('密碼錯誤! 還有', i,'次機會!')
