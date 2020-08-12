def mul_matrix():
	n = int(input())

	a = [0] * n
	for i in range(n):
	    a[i] = input()

     
	b = [0] * n
	for i in range(n):
	    b[i] = input()

	#print(a)
	#print(b)
    
	#for i in range(n):
	#	print(a[i])   

	#sum = 0
	for i in range(n):
		a_mul_b = a[i] * b[i]  
		sum = sum + a_mul_b
		print(a_mul_b)

	return sum

if __name__ == "__main__":
	sum = mul_matrix()
	print(sum)