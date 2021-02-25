from bs4 import BeautifulSoup
import requests

# remove all punctuations, split and attend a list to count words easily
def AttendList(file_name):
    punctuations = '''!( )[]{ };: = `| 0123456789- '"\,<>./ ?@#$%^&*_~'''
    liste = list()
    liste2 = list()
    for line in file_name:
        #  split the text line by line
        for word in line.split():
            #  split lines word by word
            for char in word:
                #  check each char in words that there are any punctuation, if there are remove
                if char in punctuations:
                    word = word.replace(char, " ")
                # append every word to a list
            word.split(" ") # avoid the phrase word after remove punctuations
            liste.append(word.lower().strip())
    # remove the all spaces in words
    for word in liste:
        for words in word.split(" "):
            if words.strip() != "":
                liste2.append(words.strip())
    # return the word list
    return liste2


# intersection of  two lists
def intersection(list1, list2):
    # if a word in list1 , be found list2 too append this word to list3
    list3 = [value for value in list1 if value in list2]
    # return list that contain common words
    return list3


# create a list that is not contain any stop words and contains each word once
def CreateList(liste):
    # the file that contain stop words
    fileSW = open("StopWords.txt", "r")
    # list1 is the list that we want to count its word frequencies
    list1 = list()
    # stop is the list that contains stop words
    stops = list()
    # newlist is  our new list that contains no repeated words and no stop words
    newlist = list()
    # append each word to list
    for word in liste:
        list1.append(word)
    # append the stop words to stops list
    for word in AttendList(fileSW):
        stops.append(word)

    # to create a list that contain maximum one each word and do not contain stop words
    for word in list1:
        if word not in newlist:
            if word not in stops:
                newlist.append(word)
    # return the new list
    return newlist


# sorting the word frequencies and change the index of words as their frequencies
def sorting(countlst, wordlst, number):
    for i in range(len(wordlst)):
        for j in range(len(wordlst) - 1):
            # compare the frequencies
            if countlst[j] < countlst[j + 1]:
                # changing the index of words according to their frequencies
                temp1 = wordlst[j]
                wordlst[j] = wordlst[j + 1]
                wordlst[j + 1] = temp1
                # sorting the frequencies
                temp2 = countlst[j]
                countlst[j] = countlst[j + 1]
                countlst[j + 1] = temp2

    # print the 20 greater frequencies and the word has this frequency
    for i in range(number):
        print(i+1, '{:^12}'.format(wordlst[i]),  '{:4d}'.format(countlst[i]))


def main():
    # getting book names from the user
    book1_name = input("please enter the first books name:").replace(" ", "_")
    book2_name = input("please enter the second books name:").replace(" ", "_")

    print("Scraping the books....")
    # so that the website does not block the user and  for easy access to all strings.
    headers = {
        'user-agent': 'Mozilla/5.0 (Linux; U; Android 4.1.1; en-gb; Build/KLP)'
                  ' AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Safari/534.30',
        }
    # to request access to url
    try:
        url1 = requests.get('https://en.wikibooks.org/wiki/' + book1_name + '/Print_version', headers=headers)
        url2 = requests.get('https://en.wikibooks.org/wiki/' + book2_name + '/Print_version', headers=headers)
        urlSW = requests.get('https://github.com/igorbrigadir/stopwords/blob/master/en/terrier.txt', headers=headers)
    except requests.exceptions.RequestException:
        print("This book could not found :(")

    # access the content of web sites
    soup1 = BeautifulSoup(url1.content, 'lxml')
    soup2 = BeautifulSoup(url2.content, 'lxml')
    soup3 = BeautifulSoup(urlSW.content, 'lxml')

    # open files to write web contents to files
    # this file will contain the first book
    file1 = open("Book1.txt", "w", encoding="utf-8")
    # this file wi1ll contain the second book
    file2 = open("Book2.txt", "w", encoding="utf-8")
    # this file will contain the stop words
    fileSW = open("StopWords.txt", "w")

    # find the html classes that contain the text we want, in wikibooks web site texts are in div-mw-content-ltr class
    words1 = soup1.find_all('div', attrs={'class': 'mw-content-ltr'})
    words2 = soup2.find_all('div', attrs={'class': 'mw-content-ltr'})
    stopWords = soup3.find_all('td')

# write contents of web sites as a text to file
    for word in words1:
        file1.write(word.text)

    for word in words2:
        file2.write(word.text)

    for word in stopWords:
        fileSW.write(word.text + "\n")
# close the files to be able to open again to read
    file1.close()
    file2.close()
    fileSW.close()
    # get the number of frequencies that will be print on the screen from the user
    number = int(input("\nhow many word frequencies do you want to see?"))
    
    # avoid the default numbers
    if number not in range(1, 30):
        number = 20
        
    print("The frequencies are calculating....")
    
    # the file that contains stop words
    fileSW = open("StopWords.txt", "r")
    # read the file that contains the first book
    file1 = open("Book1.txt", "r", encoding="utf8")
    # read the file that contains the second bbok
    file2 = open("Book2.txt", "r", encoding="utf8")
    # words1 is the list that contains each word of first book
    words1 = list()
    # words2 is the list  that contains each word of the second book
    words2 = list()
    # nonstop1 is the list that contains first books words without repetitions and stop words
    nonstop1 = list()
    # nonstop2 is the list that contains second books words without repetitions and stop words
    nonstop2 = list()
    # intersect is the list of common words in first and second books
    intersect = list()
    # tempinter is a temporary list that use to find distinct words
    tempinter = list()
    # diff1 is the list that contain the distinct words of first book
    diff1 = list()
    # diff2 is the list that contain the distinct words of second book
    diff2 = list()
    # countbook1 is the list that contains word frequencies of first book
    countbook1 = list()
    # countbook2 is the list that contains word frequencies of second book
    countbook2 = list()
    # countcommon is the list that contains word frequencies of common words
    countcommon = list()
    # common1 is the list that contains word frequencies in first  book of common words
    common1 = list()
    # common2 is the list that contains word frequencies in second  book of common words
    common2 = list()
    # countdiff1 is the list that contains word frequencies of first books distinct words
    countdiff1 = list()
    # countdiff2 is the list that contains word frequencies of second books distinct words
    countdiff2 = list()

# appending the relevant words from the functions outputs to lists
    for word in AttendList(file1):
        words1.append(word)

    for word in AttendList(file2):
        words2.append(word)

    for word in CreateList(words1):
        nonstop1.append(word)

    for word in CreateList(words2):
        nonstop2.append(word)

    for word in intersection(nonstop1, nonstop2):
        intersect.append(word)
        tempinter.append(word)
# find the distinct words
    diff1 = list(set(nonstop1) - set(intersect))
    diff2 = list(set(nonstop2) - set(intersect))
# firstly append "0" for each words
    for i in range(len(words1)):
        countbook1.append(0)

    for i in range(len(words2)):
        countbook2.append(0)

    for i in range(len(diff1)):
        countdiff1.append(0)

    for i in range(len(diff2)):
        countdiff2.append(0)

    for i in range(len(intersect)):
        common1.append(0)
        common2.append(0)
        
# count the words if they are same increase the number
    index = 0
    for word in nonstop1:
        for words in words1:
            if words == word:
                countbook1[index] += 1
        index += 1
        
    index = 0
    for word in nonstop2:
        for words in words2:
            if words == word:
                countbook2[index] += 1
        index += 1
    index = 0

    for word in diff1:
        for words in words1:
            if words == word:
                countdiff1[index] += 1
        index += 1
    index = 0
    
    for word in diff2:
        for words in words2:
            if words == word:
                countdiff2[index] += 1
        index += 1

    index = 0
    for word in intersect:
        for words in words1:
            if words == word:
                common1[index] += 1
        index += 1

    index1 = 0
    index2 = 0
    for word in intersect:
        for words in words1:
            if words == word:
                common1[index1] += 1
        for words in words2:
            if words == word:
                common2[index2] += 1
        index1 += 1
        index2 += 1


#calculate the common words total frequencies
    for i in range(len(common1)):
        countcommon.append(int(common1[i]/2) + common2[i])

    # printing the frequencies and words
    print("\n\nFirst book greatest frequencies\n", book1_name, "\nNo    word      FreQ")
    sorting(countbook1, nonstop1, number)
    print("\n\nSecond book greatest frequencies\n", book2_name, "\nNo    word     FreQ")
    sorting(countbook2, nonstop2, number)
    print("\n\nBOOK1:", book1_name, "Distinct words\nNo   word     FreQ")
    sorting(countdiff1, diff1, number)
    print("\n\nBOOK2:", book2_name, "\nDistinct words\nNo   word     FreQ")
    sorting(countdiff2, diff2, number)

# sorting the common words printing the common words with their frequencies
    for i in range(len(intersect)):
        for j in range(len(intersect) - 1):
            if countcommon[j] < countcommon[j + 1]:
                temp1 = intersect[j]
                intersect[j] = intersect[j + 1]
                intersect[j + 1] = temp1
                temp2 = countcommon[j]
                countcommon[j] = countcommon[j + 1]
                countcommon[j + 1] = temp2
    print("\n\ncommon words\n  No   Word      FreQ1  FreQ2  FreQ_Sum")
    for i in range(number):
        temp = intersect[i]
        index = tempinter.index(temp)
        print('{:2d}'.format(i+1), '{:^10}'.format(intersect[i]), '{:6d}'.format(int(common1[index]/2)),
              '{:6d}'.format(common2[index]), '{:6d}'.format(countcommon[i]))

main()
