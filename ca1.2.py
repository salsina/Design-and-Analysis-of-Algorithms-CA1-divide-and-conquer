def make_list(begin,end):
    l = []
    for i in range(begin,end+1):
        l.append(i)
    return l

def make_one_list(list1,list2):
    l =[]
    for i in list1:
        l.append(i)
    for i in list2:
        l.append(i)
    return l

def paint(i_column,j_column):
    if j_column - i_column == 0:
        return []
    if j_column - i_column == 1:
        return [[i_column],[j_column]]
    if (i_column + j_column)%2 == 1:  
        result1 = paint(i_column,(i_column + j_column)//2)
        result2 = paint((i_column + j_column)//2+1,j_column)
    else:
        result1 = paint(i_column,(i_column + j_column)//2 - 1)
        result2 = paint((i_column + j_column)//2,j_column)
    new_result = []
    for i in range(len(result2)):
        if i < len(result1):
            new_result.append(make_one_list(result1[i],result2[i]))
        else :
            new_result.append(result2[i])
    if (i_column + j_column)%2 == 1:  
        new_result.append(make_list(i_column + (j_column-i_column)//2+1,j_column))
        new_result.append(make_list(i_column,i_column + (j_column-i_column)//2))
    else:
        new_result.append(make_list(i_column + (j_column-i_column)//2,j_column))
        new_result.append(make_list(i_column,i_column + (j_column-i_column)//2 - 1))
    return new_result
    
n = int(input())
final_result = paint(1,n)
print(len(final_result))
for i in range(len(final_result)):
    nums = ""
    for j in range(len(final_result[i])):
        nums += str(final_result[i][j]) + " "
    print(len(final_result[i]),nums)


