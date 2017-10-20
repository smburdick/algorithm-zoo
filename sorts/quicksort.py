# Standard quicksort
#
# source: CLRS 171
#
def quicksort(A,p,r):
	if p < r:
		q = partition(A, p, r) # linear
		quicksort(A,p,q-1)
		quicksort(A, q+1, r)

# Rearrange subarray A from index p(ivot) to r(ange)
def partition(A,p,r):
	x = A[r]
	i = p - 1
	for j in range(p, r): # damned mathematicians with their 1-based indexing!
		if A[j] <= x:
			i = i + 1
			swap(A, i, j)
	swap(A, i+1, r)
	return i + 1

# swap A[i] and A[j]
def swap(A, i, j):
	temp = A[i]
	A[i] = A[j]
	A[j] = temp

## Testing
lists = [[27,89,15,174,1,5,14,88,2],[1,1,1,1,1,1,1,1,1,1,1,1,1,1],[9,8,7,6,5,4,3,2,1]]
for list in lists:
	quicksort (list, 0, len(list) - 1)
	print list

# Djikstra's Dutch National Flag Problem
# AKA 3-way quicksort (A. A. Smith)
# AKA Quick3way (Sedgewick & Wayne)...
def dutchflag(A, l, h):
	if h <= l:
		return
	t = l 		# "less than"
	g = h 		# "greater than"
	i = l + 1
	p = A[l]
	while i <= g:
		if A[i] < p:
			swap(A, t, i)
			t = t + 1
			i = i + 1
		elif A[i] > p:
			swap(A, i, g)
			g = g - 1
		else:
			i = i + 1
	dutchflag(A, l, t - 1)
	dutchflag(A, g + 1, h)

lists = [[27,89,15,174,1,5,14,88,2],[1,1,1,1,1,1,1,1,1,1,1,1,1,1],[9,8,7,6,5,4,3,2,1]]
for list in lists:
	dutchflag (list, 0, len(list) - 1)
	print list