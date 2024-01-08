# Partition array around the given pivot. 

""" Create an algorithm that separates all elements accordingly:
1. Elements less than the pivot appear in the first partition of the array
2. Elements equal to the pivot appear in the second partition of the array
3. Elements greater the pivot appear in the third partition of the array
"""


def dutch_national_flag(A: list, index: int) -> list:
    pivot = A[index]
    temp = A[0]
    A[0] = pivot
    A[index] = temp

    left_ptr = 1
    right_ptr = len(A) - 1

    while(left_ptr < right_ptr):
        # Step 1 -> Find first index whose value is greater or equal to the pivot
        while(A[left_ptr] < pivot):
            left_ptr += 1
        # Step 2 -> Find first index whose value is less than the pivot, starting from the end of the array
        while(A[right_ptr] >= pivot):
            right_ptr -= 1

        # Step 3 -> Swap the elements
        if(left_ptr >= right_ptr):
            break
        temp = A[left_ptr]    
        A[left_ptr] = A[right_ptr]        
        A[right_ptr] = temp

    # Lastly, swap the pivot element with the left ptr
    temp = A[right_ptr]
    A[right_ptr] = pivot 
    A[0] = temp

    print(A)

#  [4,3,1,5,2,4,6,8]
#  [4,3,1,2,5,4,6,8]
bob = [1,3,4,5,2,4,6,8]
A_ = [[99,88,77,66,55,44,33,22,11],
      [99,88,77,66,55,44,33,22,11,22,33,44,51,23,6,246,457,7,567,586,75424],
      [99,88,77,66,55,44,33,22,11,1,5,345,5,7823,3,43,3,46,6,45,4,23,2,3,5]
]
for array in A_:
    dutch_national_flag(array, 4)
    


