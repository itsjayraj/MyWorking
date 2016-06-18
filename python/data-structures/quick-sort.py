
def partiotion(mylist, start, end):
    pivot = mylist[end]
    partitionIdx = start
    i=start
    while i < end:
        if mylist[i] < pivot:
            mylist[i], mylist[partitionIdx] = mylist[partitionIdx], mylist[i]
            partitionIdx += 1
        i += 1

    mylist[partitionIdx], mylist[end] = mylist[end], mylist[partitionIdx]
    print mylist
    return partitionIdx


def quick_sort(mylist, start, end):
    if start < end:
        partitionIdx = partiotion(mylist, start, end)
        quick_sort(mylist, start, partitionIdx-1)
        quick_sort(mylist, partitionIdx+1, end)


if __name__ == '__main__':
    mylist = [34, 564, 65, 43, 65,23, 876, 23, 76, 90, 450, 43, 55]
    print mylist
    quick_sort(mylist, 0, len(mylist)-1)
    print mylist






