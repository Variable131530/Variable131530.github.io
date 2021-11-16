'''
#Ex1
lst = []
cnt = 1
while len(lst) < 5:
	if cnt % 2 == 0:
		lst.append(cnt)
	cnt += 1
print(lst)
print(cnt)
'''
#EX2
#Đọc và xuất nội dung ra biến data <str>
with open('draft.txt') as f:
    data = f.readlines()

#Tạo 1 biến để chứa nội dung mới sau khi sửa:
n_dt = ''

#Khởi tạo biến chạy các dòng:
i = 0
while i < len(data):
	#Tách dòng<str> thành list chứa các từ
	l_lst= data[i].split()
	#Khởi tạo biến chạy các từ trong list để so sánh
	j = 0
	while j < len(l_lst):
		if l_lst[j] == 'Hung':
			#Thay thế từ phía trước từ 'Hùng'
			l_lst[j-1] = 'Van'
		#Chuyển sang phần tử khác trong dòng thứ i
		j += 1
	#Ghi nội dung của dòng sau khi sửa <list> vào chuỗi thành <str> 
	#Phân cách bởi ' ', kết thúc dòng bằng cách thêm '\n'
	n_dt += ' '.join(l_lst) + '\n'
	#Chuyển sang dòng tiếp theo
	i += 1
print(n_dt)

with open('name.txt', 'a') as g:
	g.write(n_dt)
