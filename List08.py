def main(list1):
    """
    A list of ones and zeros, five in length, is given. replace one with True, replace zeros with False.
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
            if list1[x]==0:
                ans+=[False]
        else:
            ans+=[list1[x]]
        x+=1
    return ans
print(main([0,1,0,1,2]))