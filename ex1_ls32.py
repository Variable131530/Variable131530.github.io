'''Bài toán: Cho 1 hàm đa thức y, cho 1 luồng dữ liệu gồm (a,b)
- Xác định phần tử (a,b) nào trong luồng mà đồ thị y đi qua
- Nếu cắt, thêm vào A || thêm vào B
- Tính abs of subtract of
 sub = (sum_vertical A) - (sum vertical B) 
- Finally, print(sub)
'''


#lst = list input, coef = coefficients - các hệ số
def y_polynomial(lst, coef):
	A, B = [], []
	vertical_sum_abs = 0

	#create variable to contain value of sum in 2 case
	sum1, sum2 = 0, 0

	#for_loop to identify element belong to A or B
	for i in range(len(lst)):
		sum_ = 0
		#assign input with (x,y) variable
		y = lst[i][1]
		x = lst[i][0]
		
		#caculate sum  y polynomial input
		for j in range(len(coef)):
			sum_ += coef[j]*(x**j)
		
		#compare sum with input y
		#And caculate sum of y in 2 case
		if sum_ == y:
			A.append((x,y))
			sum1 += y
		else:
			B.append((x,y))
			sum2 += y

	#caculate abs of sum_vertical = y(A) + y(B)
	vertical_sum_abs = abs(sum1 - sum2)
	print(vertical_sum_abs)

lst = [(-5, -20), (-4, -15), (-3, 4), (-2, 9), (-1, 7),\
(0, 1), (1, -7), (2, -9), (4, 81), (5,130)]

coef = [1, -4, 2, 1]
y_polynomial(lst,coef)	






