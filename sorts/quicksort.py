# Standard quicksort
#
# source: CLRS 171
#
def quicksort(A,p,r):
	if p < r:
		q = partition(A, p, r)
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
