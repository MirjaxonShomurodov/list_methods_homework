def main(numbers1, numbers2):
    """
    You are given a list called numbers1 and numbers2.
    Delete the last item in the first list and add that deleted item to the beginning of the second list.
    Merge the first list into the second and return.
    Args:
        numbers1(list): parameter
        numbers2(list): parameter
    Returns:
        list: return answer
    """
 
    numbers1.pop(3)
    return numbers1.append(numbers2)
numbers1=[2,3,5,4]
numbers2=[9,8,7]
print(main(numbers1,numbers2))