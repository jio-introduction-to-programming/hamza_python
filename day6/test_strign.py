N = int(input())
"""
insert i e: Insert integer  at position .
print: Print the list.
remove e: Delete the first occurrence of integer .
append e: Insert integer  at the end of the list.
sort: Sort the list.
pop: Pop the last element from the list.
reverse: Reverse the list.
"""

li = []
for i in range(N):
    ins = input().split(" ")
    if ins[0] == 'insert':
        li.insert(ins[1],ins[2]) #first index then element.
    elif ins[0] == 'print'
        print(li)
    elif ins[0] == 'remove':
        li.remove(ins[1])  
    elif ins[0] == 'append'
        li.append(ins[1])
    elif ins[0] == 'sort':
        li = sorted(li)
    elif ins[0] == 'pop':
        li.pop()
    elif ins[0] == 'reverse':
        li = li.reverse()
    else:
        print("laude lag gaye")



