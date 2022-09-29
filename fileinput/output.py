import os


# with open("mydata.txt", mode="w", encoding="utf-8") as myfile:
#     myfile.write("some random text\nmore randomtext\nand some more")


# with open("mydata.txt", encoding="utf-8") as myfile:
#     lineNum = 1
#
#     while True:
#
#         line = myfile.readline()
#
#         if not line:
#             break
#
#         print("line", lineNum, ":", line, end="")
#         lineNum += 1














#     print(myfile.read())
#
#
# os.rename("mydata.txt", "mydata7.txt")
#
# # os.remove("mydata.txt")
#
# os.mkdir("mydir")
#
# os.chdir("mydir")
#
#
# print("current Directory :", os.getcwd())

with open("mydata.txt", mode="w", encoding="utf-8") as mydata:
    mydata.write("Erick keep going\nkeep learning\nand some more more")

with open("mydata.txt", encoding="utf-8") as mydata:

    lineNum = 1

    while True:

        line = mydata.readline()

        if not line:
            break
        print("line", lineNum)

        #split()
        wordlist = line.split()

        #len()
        print("number of words :", len(wordlist))


        #loop count charactre in the word list


        charCount = 0
        for word in wordlist:
            for char in word:
                charCount += 1


        #devide character count / len word list

        avgNumChars = charCount/len(wordlist)
        print("aVg word length : {:.2}".format(avgNumChars))

        lineNum += 1