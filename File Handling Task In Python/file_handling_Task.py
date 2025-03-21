file=open("sample.txt","w")
file.write("hello world ""\n"
"hello java" "\n"
"hello python" "\n"
"hello world" "\n"
"hello java" "\n"
"iam learning python programming")
file.close()
print("_"*100)

#1 Read an Entire Text File
def read_file(filename):
    with open(filename, 'r') as file:
        print(file.read())

read_file("sample.txt")

print("_"*100)
#2 Read First N Lines of a File
def read_first_n_lines(filename, n):
    with open(filename, 'r') as file:
        for _ in range(n):
            print(file.readline(), end='')

read_first_n_lines("sample.txt", 3)

print("_"*100)
#3 Append Text to a File and Display the Text
def append_text(filename, text):
    with open(filename, 'a') as file:
        file.write(text + "\n")
    
    with open(filename, 'r') as file:
        print(file.read())

append_text("sample.txt", "New line added!")

print("_"*100)
#4 Read Last N Lines of a File
from collections import deque

def read_last_n_lines(filename, n):
    with open(filename, 'r') as file:
        lines = deque(file, n)
        print("".join(lines))

read_last_n_lines("sample.txt", 3)

print("_"*100)
#5 Read a File Line by Line and Store into a List
def file_to_list(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    return lines

lines_list = file_to_list("sample.txt")
print(lines_list)

print("_"*100)
#6 Find the Longest Word in a Text File
def longest_word(filename):
    with open(filename, 'r') as file:
        words = file.read().split()
    return max(words, key=len)

print(longest_word("sample.txt"))

print("_"*100)
#7  Count the Number of Lines in a Text File
def count_lines(filename):
    with open(filename, 'r') as file:
        return sum(1 for line in file)

print(count_lines("sample.txt"))

print("_"*100)
#8 Count the Frequency of Words in a File
from collections import Counter

def word_frequency(filename):
    with open(filename, 'r') as file:
        words = file.read().split()
    return Counter(words)

print(word_frequency("sample.txt"))

print("_"*100)
#9 Copy Contents of a File to Another File
def copy_file(source, destination):
    with open(source, 'r') as src, open(destination, 'w') as dest:
        dest.write(src.read())

copy_file("sample.txt", "copy.txt")

print("_"*100)
# #10 Combine Each Line from Two Files
# def combine_files(file1, file2, output):
#     with open(file1, 'r') as f1, open(file2, 'r') as f2, open(output, 'w') as out:
#         for line1, line2 in zip(f1, f2):
#             out.write(line1.strip() + " " + line2)

# combine_files("file1.txt", "file2.txt", "combined.txt")

print("_"*100)
#11 Count the Number of Words in a Text File
import re
def count_words(filename):
    with open(filename, 'r') as file:
        text = file.read()
        words = re.findall(r'\b\w+\b', text)  # This handles words separated by commas
    return len(words)

print(count_words("sample.txt"))