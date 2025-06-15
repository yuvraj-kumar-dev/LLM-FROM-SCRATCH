import re

#method1:

#spliting text and removing none values
text = "Hello, I am yuvraj, Yuvraj is a cool guy"
result = re.split(r'(,)|(\s)', text)
print("split text", result)
for items in result:
    if items == None:
        print(items)
        result.remove(items)

print("splitted and removed none values: ", result)

# Removing empty strings from the list
result = [items for items in result if items.strip()]
print("removed empty strings from list: ", result)
print("lemgth of list: ", len(result))

#removing duplicates and sorting the list using set
all_words = sorted(set(result))
print("removed duplicates and sorted the list: ", all_words)
print("length of list now: ", len(all_words))

print("type of all_words", type(all_words)) #all_words is a list

# Creating a vocabulary dictionary from the list of words
vocabulary = {token:integer for integer, token in enumerate(all_words)}
print(vocabulary)

# Creating a reverse vocabulary dictionary
reverse_vocabulary = {integer:token for token, integer in vocabulary.items()}
print(reverse_vocabulary)

# Example usage of the vocabulary and reverse vocabulary
encode = vocabulary["yuvraj"]
decode = reverse_vocabulary[encode]

print(f"Encoded: {encode}, Decoded: {decode}")

#####################################################################################################################

#method 2: using simple functionality for creating vocabulary

print("\n")
print("Method 2 from now onwards")

vocabulary1 = {}
for token1 in all_words:
    vocabulary1[token1] = len(vocabulary1)

print("printing vocabulary1")
print(vocabulary1)

reverse_vocabulary1 = {}
for token1 in vocabulary1.items():
    reverse_vocabulary1[token1[1]] = token1[0]

print("printing reverse_vocabulary1")
print(reverse_vocabulary1)

#example usage of the vocabulary and reverse vocabulary

encode1 = vocabulary1["I"]
decode1 = reverse_vocabulary1[encode1]

print(f"Encoded: {encode1}, Decoded: {decode1}")


####################################################################

#character level tokenization

text_new = "Hello, I am Yuvraj Kumar!"

vocab = sorted(set(text_new))

print(vocab)

string_to_int = {}
count = 0
for i in vocab:
    string_to_int[i] = count
    count = count + 1

print(string_to_int)

int_to_string = {}
count1 = 0
for j in vocab:
    int_to_string[count1] = j
    count1 = count1 + 1

print(int_to_string)

def encode_ch(a):
    s = []
    for i in a:
        s.append(string_to_int[i])
    return s

encod = encode_ch("Yuv")
print(encod)

def decode_ch(a):
    s = ""
    for j in a:
        s = s + int_to_string[j]
        
    return s

decod = decode_ch(encod)
print(decod)
