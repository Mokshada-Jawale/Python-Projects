# Program for Binary Search

def get_element():
    array = list(map(int,input("Enter the values of array: ").split()))
    element = int(input('Enter a element whose index you want to search: '))
    return array, element

def binary_search(array, element):
    low  = 0
    high =len(array)-1
    # mid = 0

    while low <= high:
        mid = high+low // 2

        if array[mid] < element:
            low = mid + 1
        elif array[mid] > element:
            high = mid - 1
        else:
            return mid

    return -1

def main():
    array, element = get_element()
    index = binary_search(array, element)
    if index != -1:
        print("Element is present at index ", index)
    else:
        print("Given element is not in the array")


if __name__ == '__main__':
    main()



