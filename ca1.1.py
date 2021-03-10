def make_dict(dictionary):
    new = {}
    for i in dictionary:
        new[i] = dictionary[i]
    return new

def calculate_happiness(people_ages):
    
    forward = [1] * len(people_ages)
    behind = [0] * len(people_ages)
    dictionary = {}
    
    for i in range(len(people_ages)):
        if not people_ages[i] in dictionary:
            dictionary[people_ages[i]] = 1
        else:
            dictionary[people_ages[i]] += 1
            
    copy_dict = make_dict(dictionary)
    
    for i in range(len(people_ages)):
        behind[i] = dictionary[people_ages[i]]
        forward[i] = copy_dict[people_ages[i]] - dictionary[people_ages[i]] +1
        dictionary[people_ages[i]] -= 1
    
    return forward,behind    

def make_list(l,begin,end):
    new_l = []
    for i in range(begin,end):
        new_l.append(l[i])
    return new_l

def calculate_harassment(begin,end,new_forward,new_behind,harassment):
    if begin == end :
        return 
    if end - begin ==1:
        if new_forward[begin] > new_behind[end]:
            harassment[0] += 1
        return 
    
    if (begin+end)%2 == 1:
        calculate_harassment(begin,(begin+end)//2,new_forward,new_behind,harassment)
        calculate_harassment((begin+end)//2+1,end,new_forward,new_behind,harassment)
    else:
        calculate_harassment(begin,(begin+end)//2-1,new_forward,new_behind,harassment)
        calculate_harassment((begin+end)//2,end,new_forward,new_behind,harassment)
    
    if (begin+end)%2 == 1:
        new_f = make_list(new_forward,begin,(begin+end)//2+1)
        new_b = make_list(new_behind,(begin+end)//2+1,end+1)
    else:
        new_f = make_list(new_forward,begin,(begin+end)//2)
        new_b = make_list(new_behind,(begin+end)//2,end+1)
    
    new_f.sort()
    new_b.sort()
    
    forward_index=0
    behind_index=0
    while forward_index<len(new_f) and behind_index < len(new_b):
        if new_f[forward_index] > new_b[behind_index]:
            harassment[0] += len(new_f) - forward_index
            behind_index+=1
        else:
            forward_index+=1
            
people = int (input())
people_ages = [int(x) for x in input().split()]
f,b = calculate_happiness(people_ages)
harassment = [0]
calculate_harassment(0,people-1,f,b,harassment)
print(harassment[0])