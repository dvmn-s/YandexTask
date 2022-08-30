question_word = list(input())
answer_word = list(input())
dict1 = {}
unresult_indecies = []
results = [None,] * len(question_word)

for index, letter in enumerate(question_word):
    if letter in dict1:
        dict1[letter].append(index)
    else:
        dict1[letter] = [index]

for index, letter in enumerate(answer_word):
    current_letter_indecies = dict1.get(letter)
    if current_letter_indecies:
        if index in current_letter_indecies:
            results[index] = 'correct'
            current_letter_indecies.remove(index)
        else:
            unresult_indecies.append(index)
    else:
        results[index] = 'absent'

for index in unresult_indecies:
    current_letter_indecies = dict1.get(answer_word[index])
    if current_letter_indecies:
        results[index] = 'present'
        current_letter_indecies.pop(0)
    else:
        results[index] = 'absent'

print(*results, sep='\n')


