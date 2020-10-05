# put your code here.
file_to_count = open("C:\\users\\Peri\\src\\dicts-word-count\\test.txt") 
content = file_to_count.read()
content = content.lower()
word_count = {}
# Change file into list of each line after line break
content = content.split('\n')
       #


list_of_words = []
for line in content:
    word = line.split(' ')
    list_of_words = list_of_words + word 

final_list = []
for word in list_of_words:
    if word.isalpha() == True:
        final_list = final_list + [word]
        
    else:
        word = word[:-1]
        final_list = final_list + [word]


for word in final_list:
    # if the word is already in the dictionary, add 1 to the value
    if word not in word_count:
        word_count[word] = 1
    
    # if the word is not in the dictionary, add word as key and set
    # set value to 1
    else:
        word_count[word] += 1
       
for key, items in word_count.items():
    print("{} {}" .format(key,items))
   