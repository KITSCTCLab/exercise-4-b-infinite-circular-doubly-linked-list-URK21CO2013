length__of__circular__linked__list = int(input())

circular__linked__list = list(map(int,input().strip().split(" ")))

final__list = [circular__linked__list[i] for i in range(3)]

for i in circular_linked_list:
 	if i not in final_list:
 final_list.append(i)

print(len(final_list))

for i in final_list:
 print(i,end=" ")
