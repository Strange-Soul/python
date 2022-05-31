# Dictionaries

"""
9.4 Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.
"""        
filename=input("Enter the file_name:")
fhandle=open(filename) 
word_count=dict() #dct={}
for line in fhandle:
  if line.startswith("From:"):
    line=line.rstrip()
    e_mails=line.split()
    #print(e_mails[1])
    repeat_word=e_mails[1]
    word_count[repeat_word]=word_count.get(repeat_word,0)+1
for key,value in word_count.items():
    print("E-mail:",key,'....',"Number_of_times_appered:",value)
print(repeat_word,word_count[repeat_word])