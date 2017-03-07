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


> In this qustion I selected two different API to apply data analysis. One is the Books API and the other one is the Article API
> In Ana1 I selected three kinds of catagory of books and find out all the author of those books and caoculate the how many books each author write
> In Ana2 I use the best seller history api. What I have done is to fetch the author list from my previous work and use it as params to make a request to NYT and get the list of best seller books of each authors in each kind of listname
> In Ana3 I applyed the article API, give it a time period (2000-01-01  to 2017-03-01) and a keyword: machine learning to count how many machine learning related article are published in that time period. 



#### Analysis 1 :
- I have choosen three different catagories of books to apply analysis, they are list_name = ['Business Books', 'Science', -'E-Book Fiction']
- Because both Science books and Business books are published by NYT monthly, I made a function to iterate through all the sundays of the specific time period

```sh
def calculateDateRange(beginDate, endDate):
    dateList = []
    while(beginDate < endDate):
        beginDate =  beginDate + relativedelta.relativedelta(months=1)
        dateList.append(beginDate)
    return dateList

```
- I used the following function to fetch those two data using calculateDateRange
```sh
def getData(dateList, listname):  
    for date in dateList:        
        payload = {
            'api-key': key,
            'list': listname,
            'date': date

        }
        r = requests.get('https://api.nytimes.com/svc/books/v3/lists.json', params = payload).json()
        time.sleep(1)
        path = os.path.dirname(os.getcwd())+ '/Data/' + listname + 'bookList/'
        filename = listname + str(date)
        with open(path + filename + '.json', 'a') as outfile:
            json.dump(r, outfile)
```
- And E-Book Fiction boonks dataset is released weekly so that I got to find the Sundays of each week
```sh
def calculateWeekDateRange(beginDate, endDate):
    dateList = []
    while(beginDate < endDate):
        beginDate =  beginDate + relativedelta.relativedelta(days=7)
#         print(beginDate)
        dateList.append(beginDate)
    return dateList
```

- After getting all the authors from the specific list_name, I wrote iteration to get how many books did each and every authors made
```sh
def authorFreq(authorList):
    wordfreq  = FreqDist(authorList)
    sorted_words = sorted(wordfreq.items(), key=lambda wordfreq: wordfreq[1], reverse=True)
    
    print (sorted_words[0:20])
    return sorted_words

```
- Finally out put to csv file


#### Analysis 2 :
- From the out put csv file from Ana 1 I got the list of all authors, then I use requests to request for best seller 
- For each author in the list I made the request to ask for all the best seller books of that author
```sh
def getAllBestsellerBooks(authorList):
    bestSellerList = []
    for author in authorList:
        payload = {
            'api-key': key, 
            'author': author
        }
        r = requests.get('https://api.nytimes.com/svc/books/v3/lists/best-sellers/history.json', params = payload).json()
        try:
            alist = [author, r["num_results"]]
            bestSellerList.append(alist) 
        except:
            alist = [author, 0]
            bestSellerList.append(alist)
            
        time.sleep(0.5)
    return bestSellerList

```
- And count how many best seller books does each author have. and ouput the result to a csv file

#### Analysis 3 :
- For this analysis, I used a brand new API called Article, for this API, I made the request contain four attributes: query word, begin_date, end_date, and page
```sh
def getAllArticles():
    i = 0
    while(i < 200):
        payload = {
            'api-key': key, 
            'q': "machine learning",
            'begin_date': "20000101",
            'end_date': "20170301",
            'page': i
        }
        r = requests.get('https://api.nytimes.com/svc/search/v2/articlesearch.json', params = payload).json()  
        path = os.path.dirname(os.getcwd())+ '/Data/articlesearch/'
        filename = "articlesearch_page" + str(i)
        i += 1
        time.sleep(0.4)
        with open(path + filename + '.json', 'a') as outfile:
            json.dump(r, outfile)
getAllArticles()
```
- I've count in each month how many article about machine learning is published and get the result in a list and then I used the ploting to plot the total trend of machine learning.

```sh
%matplotlib inline
from matplotlib import pyplot as plt


datetimeList = []
for item in sorted_words:
    date = datetime.strptime(item[0], '%Y-%m')
    datetimeList.append(date)


z_list = [z for [x, z] in sorted_words]

plt.plot_date(datetimeList, z_list)
plt.xlabel('Date')
plt.ylabel('Frequency')
plt.title(" Machine Learning Trend")

```

---

