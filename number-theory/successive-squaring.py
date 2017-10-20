# Method of Successive Squaring
nums = input('Enter three integers a, k, n separated by spaces to compute\n\t\ta^k (mod n),\tn>2,k>=1.\n').split()
try:
	a = int(nums[0])
	k = int(nums[1])
	n = int(nums[2])
	b = bin(k)
	b = b[2:len(b)]
	r = len(b)
	big_A = a
	prod = 1
	for i in range(r):
		power = 2**i  * int(b[r - i - 1])
		p = a**power % n
		prod = prod * p
	print (str(prod % n))
	
except:
	print('please provide 3 integers ')
#def __succ_powers():
