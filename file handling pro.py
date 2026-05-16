#1.Write a Python program to read a text file and count the total number of words in it.

with open("test.txt","r") as f:
    content=f.read()
    words=content.split()
    print(len(words))

#2.Write a program to reverse the contents of a file line by line and save it to another file.

with open("test.txt","r") as f:
    lines=f.readline()

with open("input.txt","w") as destination:
    for line in reversed(lines):
        destination.write(line)


#3.Write a program to find the longest word in a file.

with open("example.txt", "r") as file:
    words = file.read().split()
    longest_word = max(words, key=len)
    print("Longest word:", longest_word)

#4.Write a program to count how many times a specific word appears in a file.

word_to_count = "Python"
with open("example.txt", "r") as file:
    content = file.read()
    count = content.lower().split().count(word_to_count.lower())
    print(f"The word '{word_to_count}' appears {count} times.")


#5.Write a program to copy only the lines that contain a specific keyword to a new file.

keyword = "important"
with open("input.txt", "r") as source:
    lines = source.readlines()

with open("output.txt", "w") as destination:
    for line in lines:
        if keyword in line:
            destination.write(line)

#6.Write a program to remove duplicate lines from a file.

with open("input.txt", "r") as file:
    lines = file.readlines()

unique_lines = list(set(lines))

with open("output.txt", "w") as file:
    file.writelines(unique_lines)


#7.Write a program that writes numbers from 1 to 100 to a file, then reads the file and calculates the sum.

with open("numbers.txt", "w") as file:
    for number in range(1, 101):
        file.write(f"{number}\n")

with open("numbers.txt", "r") as file:
    numbers = [int(line.strip()) for line in file]
    print("Sum of numbers:", sum(numbers))



#8.Write a program to find and replace a specific word in a file.

word_to_find = "oldword"
replacement = "newword"

with open("example.txt", "r") as file:
    content = file.read()

new_content = content.replace(word_to_find, replacement)

with open("example.txt", "w") as file:
    file.write(new_content)
print(f"Replaced '{word_to_find}' with '{replacement}'.")