def main(list1):
    """
    A list of several elements is given. True if all items are the same, otherwise return False.
    Args:
        list1 (list): parameter
    Returns:
        bool: return answer
    """
    a=0
    b=0
    while a<len(list1):
        if list1[0]==list1[a]:
            b+=0
        else:
            b+=1
        a+=1
    if b==0:
        return True
    else:
        return False   
print(main([5,5,5,5,5,5,5,5,5,5,5,5,5,5,3,5,5]))