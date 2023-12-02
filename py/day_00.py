def convert_to_word(input):
    ans = ""
    nums_to_str = {'1': 'one','2': 'two','3': 'three','4': 'four','5': 'five',
                   '6': 'six','7': 'seven','8': 'eight','9': 'nine'}

    for i in input:
        if i in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            ans += nums_to_str[i]
        else:
            ans += i
    
    return ans

def convert_to_num(input):
    ans = []
    str_to_nums = {'one': '1','two': '2','three': '3','four': '4','five': '5',
                   'six': '6','seven': '7','eight': '8','nine': '9'}
    
    for j in range(len(input)):
        for i in str_to_nums.keys():
            l = len(i)
            if input[j:j+l] == i:
                ans.append(int(str_to_nums[i]))

    return ans

inputs = open('../test/day_00.txt', 'r').read().split('\n')

ans = []
final = []
sum1 = 0

# Part 1 logic
for i in inputs:
    for j in i:
        if j in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            ans.append(int(j))
    
    final.append(ans)
    ans = []
for i in final:
    if len(i) == 1:
        i.append(i[0])
    sum1 += int(str(i[0]) + str(i[-1]))

print(sum1) # print part 1 answer

# Part 2 logic
part_2 = []

for i in inputs:
    answer = convert_to_num(convert_to_word(i))
    part_2.append(int(str(answer[0])+str(answer[-1])))

print(sum(part_2)) # print part 2 answer
