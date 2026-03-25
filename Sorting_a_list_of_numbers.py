list2 = [1,2,3,4]
#list2 = [1,3,2,4]
asc = True
for i in range(len(list2)-1):
    if list2[i] < list2[i+1]:
        pass
    else:
        asc = False
        print("This list is not sorted in ascending order")
if asc == True:
    print("This list is sorted in ascending order")

# Adding a comment to in branch1 and to merge in main
