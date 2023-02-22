# def restore(memory, origin):
#     if memory == origin:
#         return count
#     else:
#         for s in range(len(memory)):
#             if memory[s] == 1:
#                 origin[s:] = [1] * len(origin[s:])
#                 break
#             return restored(memory, origin)


Test_case = int(input())

for t in range(Test_case):
    restored = list(input())
    reset = len(restored) * ['0']
    count = 0

    for i in range(len(restored)):
        if restored == reset:
            break
        if restored[i] != reset[i]:
            if restored[i] == '1':
                reset[i:] = ['1'] * len(reset[i:])
                count += 1
                continue
            else:
                reset[i:] = ['0'] * len(reset[i:])
                count += 1
                continue

    print(f'#{t+1} {count}')
