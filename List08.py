def main(fruits):
    """
    A list called "fruits" is given and is five in length and contains at least one "apple". Remove the apples from the list and return the list.
    Args:
        fruits(list): parameter
    Returns:
        list: return answer
    """
    return fruits.count(1)
fruits=[1,0,1,0,1,0,1,0,1,1]
print(main(fruits))