number_words = {
    1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five',
    6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'
}

num_11_19 = {11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen'}


# Tens
ten_words = {
    1: 'ten', 2: 'twenty', 3: 'thirty', 4: 'forty', 5: 'fifty',
    6: 'sixty', 7: 'seventy', 8: 'eighty', 9: 'ninety'
}

value = int(input())
if len(str(value)) == 1:
    print(number_words[value])
elif value in range(11,20):
    print(num_11_19[value])
else:
    value = str(value)
    print(f'{ten_words[int(value[0])]} {number_words[int(value[1])]}')

