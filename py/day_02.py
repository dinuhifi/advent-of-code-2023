special_characters = [
                    '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '{', '}',
                    '[', ']', '\\', '|', ';', ':', "'", '"', '<', '>', ',', '/', '?', '~', '`', '¢',
                    '£', '¥', '€', '©', '®', '™', '§', 'µ', '°', '×', '÷', '≠', '±', '∞', '√', '∆',
                    'π', 'Ω'
                     ]

input_strings = open("../test/day_02.txt", "r").read().split("\n")

row = []
input_matrix = []

for i in range(len(input_strings)):
    for j in range(len(input_strings[i])):
        row.append(input_strings[i][j])
    input_matrix.append(row)
    row = []
            
for i in input_matrix:
    for j in i:
        print(j, end=" ")
    print()


found = []
big_found = []

answer = []

for i in range(len(input_matrix)):
    for j in range(len(input_matrix[i])):
        if input_matrix[i][j] in "123456789":

            #checking row 1
            if i == 0 and j == 0:
                if input_matrix[i+1][j] in special_characters or input_matrix[i][j+1] in special_characters or input_matrix[i+1][j+1] in special_characters:
                    found.append([input_matrix[i][j],i])

                    if input_matrix[i][j+1] in "123456789" and input_matrix[i][j+2] in "123456789":
                        num = input_matrix[i][j] + input_matrix[i][j+1] + input_matrix[i][j+2]
                        answer.append(int(num))
                    elif input_matrix[i][j+1] in "123456789":
                        num = input_matrix[i][j] + input_matrix[i][j+1]
                        answer.append(int(num))


            elif i==0 and j < len(input_matrix[i])-1:
                if input_matrix[i+1][j] in special_characters or input_matrix[i][j+1] in special_characters or input_matrix[i+1][j+1] in special_characters or input_matrix[i][j-1] in special_characters or input_matrix[i+1][j-1] in special_characters:
                    found.append([input_matrix[i][j],i])
                    
                    if j < len(input_matrix[i])-2:
                        if input_matrix[i][j+1] in "123456789" and input_matrix[i][j+2] in "123456789":
                            num = input_matrix[i][j] + input_matrix[i][j+1] + input_matrix[i][j+2]
                            answer.append(int(num))
                        elif input_matrix[i][j+1] in "123456789":
                            num = input_matrix[i][j] + input_matrix[i][j+1]
                            answer.append(int(num))
                    
                    if j >= 2:
                        if input_matrix[i][j-1] in "123456789" and input_matrix[i][j-2] in "123456789":
                            num = input_matrix[i][j-2] + input_matrix[i][j-1] + input_matrix[i][j]
                            answer.append(int(num))
                    elif j >= 1:
                        if input_matrix[i][j-1] in "123456789":
                            num = input_matrix[i][j-1] + input_matrix[i][j]
                            answer.append(int(num))


            elif i==0 and j == len(input_matrix[i])-1:
                if input_matrix[i+1][j] in special_characters or input_matrix[i][j-1] in special_characters or input_matrix[i+1][j-1] in special_characters:
                    found.append([input_matrix[i][j],i])

                    if input_matrix[i][j-1] in "123456789" and input_matrix[i][j-2] in "123456789":
                        num = input_matrix[i][j-2] + input_matrix[i][j-1] + input_matrix[i][j]
                        answer.append(int(num))
                    elif input_matrix[i][j-1] in "123456789":
                        num = input_matrix[i][j-1] + input_matrix[i][j]
                        answer.append(int(num))

                    
            #checking middle rows
            elif i < len(input_matrix)-1 and j == 0:
                if input_matrix[i+1][j] in special_characters or input_matrix[i-1][j] in special_characters or input_matrix[i][j+1] in special_characters or input_matrix[i+1][j+1] in special_characters or input_matrix[i-1][j+1] in special_characters:
                    found.append([input_matrix[i][j],i])

                    if input_matrix[i][j+1] in "123456789" and input_matrix[i][j+2] in "123456789":
                        num = input_matrix[i][j] + input_matrix[i][j+1] + input_matrix[i][j+2]
                        answer.append(int(num))
                    elif input_matrix[i][j+1] in "123456789":
                        num = input_matrix[i][j] + input_matrix[i][j+1]
                        answer.append(int(num))
                    
            elif i < len(input_matrix)-1 and j < len(input_matrix[i])-1:
                if input_matrix[i+1][j] in special_characters or input_matrix[i-1][j] in special_characters or input_matrix[i][j+1] in special_characters or input_matrix[i+1][j+1] in special_characters or input_matrix[i-1][j+1] in special_characters or input_matrix[i][j-1] in special_characters or input_matrix[i+1][j-1] in special_characters or input_matrix[i-1][j-1] in special_characters:
                    found.append([input_matrix[i][j],i])

                    if input_matrix[i][j+1] in "123456789" and input_matrix[i][j+2] in "123456789":
                        num = input_matrix[i][j] + input_matrix[i][j+1] + input_matrix[i][j+2]
                        answer.append(int(num))
                    elif input_matrix[i][j+1] in "123456789":
                        num = input_matrix[i][j] + input_matrix[i][j+1]
                        answer.append(int(num))


                    elif input_matrix[i][j-2] in "123456789" and input_matrix[i][j-1] in "123456789":
                        num = input_matrix[i][j-2] + input_matrix[i][j-1] + input_matrix[i][j]
                        answer.append(int(num))

                    elif input_matrix[i][j-1] in "123456789":
                        num = input_matrix[i][j-1] + input_matrix[i][j]
                        answer.append(int(num))
                

            elif i < len(input_matrix)-1 and j == len(input_matrix[i])-1:
                if input_matrix[i+1][j] in special_characters or input_matrix[i-1][j] in special_characters or input_matrix[i][j-1] in special_characters or input_matrix[i+1][j-1] in special_characters or input_matrix[i-1][j-1] in special_characters:
                    found.append([input_matrix[i][j],i])

                    if input_matrix[i][j-1] in "123456789" and input_matrix[i][j-2] in "123456789":
                        num = input_matrix[i][j-2] + input_matrix[i][j-1] + input_matrix[i][j]
                        answer.append(int(num))
                    elif input_matrix[i][j-1] in "123456789":
                        num = input_matrix[i][j-1] + input_matrix[i][j]
                        answer.append(int(num))


            #checking last row
            elif i == len(input_matrix)-1 and j == 0:
                if input_matrix[i-1][j] in special_characters or input_matrix[i][j+1] in special_characters or input_matrix[i-1][j+1] in special_characters:
                    found.append([input_matrix[i][j],i])

                    if input_matrix[i][j+1] in "123456789" and input_matrix[i][j+2] in "123456789":
                        num = input_matrix[i][j] + input_matrix[i][j+1] + input_matrix[i][j+2]
                        answer.append(int(num))
                    elif input_matrix[i][j+1] in "123456789":
                        num = input_matrix[i][j] + input_matrix[i][j+1]
                        answer.append(int(num))


            elif i == len(input_matrix)-1 and j < len(input_matrix[i])-1:
                if input_matrix[i-1][j] in special_characters or input_matrix[i][j+1] in special_characters or input_matrix[i-1][j+1] in special_characters or input_matrix[i][j-1] in special_characters or input_matrix[i-1][j-1] in special_characters:
                    found.append([input_matrix[i][j],i])

                    if j < len(input_matrix[i])-2:
                        if input_matrix[i][j+1] in "123456789" and input_matrix[i][j+2] in "123456789":
                            num = input_matrix[i][j] + input_matrix[i][j+1] + input_matrix[i][j+2]
                            answer.append(int(num))
                        elif input_matrix[i][j+1] in "123456789":
                            num = input_matrix[i][j] + input_matrix[i][j+1]
                            answer.append(int(num))
                    
                    if j >= 2:
                        if input_matrix[i][j-1] in "123456789" and input_matrix[i][j-2] in "123456789":
                            num = input_matrix[i][j-2] + input_matrix[i][j-1] + input_matrix[i][j]
                            answer.append(int(num))
                    elif j >= 1:
                        if input_matrix[i][j-1] in "123456789":
                            num = input_matrix[i][j-1] + input_matrix[i][j]
                            answer.append(int(num))


            elif i == len(input_matrix)-1 and j == len(input_matrix[i])-1:
                if input_matrix[i-1][j] in special_characters or input_matrix[i][j-1] in special_characters or input_matrix[i-1][j-1] in special_characters:
                    found.append([input_matrix[i][j],i])

                    if input_matrix[i][j-1] in "123456789" and input_matrix[i][j-2] in "123456789":
                        num = input_matrix[i][j-2] + input_matrix[i][j-1] + input_matrix[i][j]
                        answer.append(int(num))
                    elif input_matrix[i][j-1] in "123456789":
                        num = input_matrix[i][j-1] + input_matrix[i][j]
                        answer.append(int(num))

    if found:
        big_found.append(found)
    found = []

print()

for i in answer:
    print(i, end=" ")

print('\n')

final = []

unique_list = []
seen_items = set()

for item in answer:
    if item not in seen_items:
        unique_list.append(item)
        seen_items.add(item)

print(unique_list)

super_final = unique_list.copy()

i = 0
while i < len(super_final) - 1:
    if super_final[i] > super_final[i + 1] and str(super_final[i + 1]) in str(super_final[i]):
        super_final.remove(super_final[i + 1])
    elif super_final[i + 1] > super_final[i] and str(super_final[i]) in str(super_final[i + 1]):
        super_final.remove(super_final[i])
        if i > 0:
            i -= 1
    else:
        i += 1

print(sum(super_final))