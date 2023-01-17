def return_Reverse(x):
    empty_str =''
    empty_list = []
    for ch in x:
        
        empty_list.append(ch)

    while len(empty_list) > 0:
        empty_str += empty_list[-1]
        empty_list.pop()
    print(empty_str)

return_Reverse('happy')
return_Reverse('Python')
return_Reverse("")
return_Reverse('a')