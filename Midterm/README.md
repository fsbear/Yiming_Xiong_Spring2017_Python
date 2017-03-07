# Midterm Exam - Spring 2017 INFO7374 Intro_Python  

Yiming Xiong 
00161641

---

### Question 1 : 

> In this question, I download the Enron email Dataset and conduct three analysis toward the persons of interest, their relationships, and the email content



#### Instructions :
#####For Analysis 1
- First of all, I read through the whole maildir to find each and every email
- Second, from the whole content just read I make code to find the email receiver, and then find out that the data contains a lot of unclear variabale, thus I made some data sanitize
```sh
#calculate email receiver 
    if email['to'] != None:
        if ',' in email['to']:
            for reciever in email['to'].split(','):
                reciever = reciever.replace('\n\t', '')
                reciever = reciever.replace(' ', '')
                personEmailReceiverEmail.append(reciever) 
        else:
            personEmailReceiverEmail.append(email['to'])
```
- Third, I apply the same method to find all the senders
```sh
 #calculate email sender 
            
    if email['from'] != None:
        if ',' in email['from']:
            for sender in email['from'].split(','):
                sender = sender.replace('\n\t', '')
                sender = sender.replace(' ', '')
                personEmailSenderEmail.append(sender) 
        else:
            personEmailSenderEmail.append(email['from'])
```
- Fourth, I used NLTK Freqdist function to find the frequency of persons receive or send emails
```sh
receiverFreq = FreqDist(receiverPersonNameList)
senderFreq = FreqDist(senderPersonNameList)
```
- Finally, output to csv
```sh
def outPutReceiverFreqCsv():
    f = open('Ana1/Q1AnalysisReceiverName.csv', 'a')
    try:
        writer = csv.writer(f)
        writer.writerow(["Receiver Name", "Count"])
        writer = writer.writerows(receiverFreqSorted)
    finally:
        f.close()
        
```

#####For Analysis 2
- Continued with Analysis 1, I pick top five person from the group who send most emails and five people from the group who receive most emails and some of people in the list is duplicate so it will contain 7 different account(which contain 6 person and one machine accoutn for auto-generated content) and I add in three VIPs Kenneth Lay, Founder, Chairman and CEO, Jeffrey Skilling, former President, and COO, Andrew Fastow, former CFO Rebecca Mark-Jusbasche, former Vice Chairman, Chairman and CEO of Enron International Stephen F. Cooper, Interim CEO and CRO So I made a List of Nine people who is the Person of Interests. Though Andrew Fastow have not directory of emials so eventually, there are eigth people into consideration.

###### Receiver Name,Count
- richard.shapiro,15149 -----  Richard Shapiro        Vice President     Regulatory Affairs
- jeff.dasovich,14207   -----  Jeff Dasovich          Employee           Government Relation Executive
- tana.jones,12828      -----  Tana Jones             N/A
- steven.kean,12754     -----  Steven Kean            Vice President     Vice President & Chief of Staff


###### Sender Name,Count
- kay.mann,16735        -----  Kay Mann               Employee
- vince.kaminski,14368  -----  Vince Kaminski         Manager            Risk Management Head
- jeff.dasovich,11411   -----  Jeff Dasovich          Employee           Government Relation Executive
- pete.davis,9149       -----  broadcast proxy	    used for auto-generated emails

###### Extra VIP
- Kenneth Lay  --  kenneth.lay
- Jeffrey Skilling  -- jeff.skilling
- Andrew Fastow  --  andrew.fastow (doesn't have a directory of email)

- **`I used the code below to calculate the email transactions between each of person in POI list`**.


```sh
def calculateEmailCommunication():
#     iterate through PoiList
    

    for namePair in Poi:
    
        dirname = namePair[0]
        email = namePair[1]
        path = os.path.dirname(os.getcwd())+ '/Data/maildir/' + dirname 
        pathList = []
        pathList = [os.path.join(root, filename) for root, dirs, files in os.walk(path) for filename in files if filename.endswith('.')]
#         iterate through all the file in the path

        for namePair2 in Poi :                 
            if namePair2[0] != dirname:
                count = 0
                countList = [namePair2[1], namePair[1], count]
                
                for path in pathList:
                    f = open(path, 'r', encoding = 'utf-8', errors = 'ignore')
                    content = f.read()  
                    email = Parser().parsestr(content)
                    if email['from'] != None:
                        senderlist = []
                        if ',' in email['from']:
                            for sender in email['from'].split(','):
                                sender = sender.replace('\n\t', '')
                                sender = sender.replace(' ', '')
                                sender = sender.split("@")[0]
                                senderlist.append(sender) 
                        else:
                            senderlist.append(email['from'].split("@")[0])   
                        if namePair2[1] in senderlist:
                            countList[2] += 1
                communicationCountList.append(countList) 
```


- Finally, output to a csv file


#####For Analysis 3
- Continued with Analysis 2, I select the email that is from the POI list and conducted the word frequency digging and found out some intersting fact
```sh
wordsList = []
for path in emialPathList:
    f = open(path, 'r', encoding = 'utf-8', errors = 'ignore')
    content = f.read()  
    email = Parser().parsestr(content)
    emailcontent = email.get_payload()
    words = [word for word in word_tokenize(emailcontent.lower()) if word not in stopwords.words('english') and word not in string.punctuation and word.isalpha()]
    wordsList.extend(words)
wordsList[:20]   

wordfreq  = FreqDist(wordsList)
sorted_words = sorted(wordfreq.items(), key=lambda wordfreq: wordfreq[1], reverse=True)
print (sorted_words[0:20])

```
- the most frequent words are [('enron', 5150), ('subject', 1903), ('ect', 1745), ('richard', 1711), ('cc', 1696), ('pm', 1664), ('ees', 1481), ('market', 1479), ('would', 1328), ('california', 1315), ('power', 1133), ('energy', 1094), ('forwarded', 1056), ('jeff', 985), ('please', 728), ('j', 711), ('electricity', 702), ('also', 662), ('state', 645), ('may', 629)]
- Which indicated that the richard is the main character of the company, CA will play an important role in the company stratgy. And the company mainly focus on the natural resource such as power and energy.


---
### Question 2 : 


> In this qustion I selected two different API to apply data analysis. One is 



#### Instructions :
- You would need to create an API key.
- Use `request` or `beautiful-soap` library to download the data. (No other library or crawler allowed).
- Store the data in your local machine.
- Your analysis should use **this downloaded data only** (and not try to redownload this data again during analysis time).
-  There is a rate limit for downloading the data. I would suggest you to start collecting the data from day 1. You can try using multiple account to get more than 1 key.
-  You need to use atleast 2 API method eg: `archive`, `Article Search`. **Do not use** `Movies Review`, `Semantic` API.

---

