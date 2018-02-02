def bubble_sort(arr):
	# Go over every element (arranged backwards)
    for n in range(len(arr)-1,0,-1):
        # For -1 each time beacuse each loop an elemnt will be set in position.
        for k in range(n):
        	# Check with the rest of the unset elements if they are greater than one another if so, switch
            if arr[k]>arr[k+1]:
                temp = arr[k]
                arr[k] = arr[k+1]
                arr[k+1] = temp