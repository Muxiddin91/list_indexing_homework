def main(list1):
    """
    A list of units and zeros with a length of five is given. Replace one with True.
    Args:
        list1 (list): parameter
    Returns:
        list: return answer
    """
    x=0
    ans=[]
    while x<len(list1):
        if list1[x]==1:
            ans+=[True]
        else:
            ans+=[list1[x]]
        x+=1
    return ans
print(main([0,0,9,0,1,1,1,1,1]))