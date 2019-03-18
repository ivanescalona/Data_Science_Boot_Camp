import re

print("Howdy? Will you be analyzing a text file(1) or entering the text directly(2)?")
file_or_string = input("Enter your choice (1) or (2): ")

def get_string_file(f_or_s, selection):
    if selection == 1:
        with open (f_or_s+'.txt', 'r') as file1:
            data = file1.read()
    else:
        data = f_or_s
    return data
    
if (file_or_string == "1"):
    file_name = input("Please enter your file name (don't include .txt): ")
    data = get_string_file(file_name, 1)
else:
    my_string = input("Please enter your text: ")
    data = get_string_file(my_string, 2)

sentences = re.split('\. |\n |\n\n |.\n |.\n\n' ,data)
sen_count = len(sentences)

sen_word_count = 0
for sen in sentences:
    current = sen.split()
    sen_word_count += len(current)

average_words = sen_word_count/sen_count

words = []
for sen in sentences:
    current = re.sub('[0-9,]', '', sen)
    current = current.split()
    
    for item in current:
        words.append(item)

word_count = len(words)

word_letter_count = 0
i = 0
for i in range(0,len(words)):
    current_word = re.findall("[a-zA-Z]*", words[i])
    
    for item in current_word:
        word_letter_count += len(item)
            
average_letters = word_letter_count/word_count

print("Paragraph Analysis")
print("---------------------")
print("Approximate word count: "+ str(word_count))
print("Approximate sentence count: "+ str(sen_count))
print("Average letter count: {:.2f}".format(average_letters))
print("Average sentence length: {:.2f}".format(average_words))