def remove_duplicates(lst):
    seen=set()
    result=[]
    for items in lst:
        if items not in seen:
            result.append(items)
            seen.add(items)
    return result


lst=[1,2,2,3,4,1]
answer=remove_duplicates(lst)
print(answer)
    
