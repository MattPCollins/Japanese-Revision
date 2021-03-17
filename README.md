# Japanese Vocabulary Revision Analysis: Overview

Over the work-from-home period of Covid-19 lockdown, I have been taking my Japanese studies more seriously, with a particular focus on writing Kanji. For anyone familiar with Kanji, they can appreciate the vast range of characters required to be mastered, and this was something I have previously struggled with.

While there are great revision apps already on the market, I wanted to kill two birds with one stone and create my own revision program in Python, as another avenue of self-development.

## App Background
I created my own space repetition algorithm and populated my own dictionary of vocabulary to study. I created fact and dimensional tables to model my results and track my progress.

My algorithm was experimentally created at first, but then introduced different samples of spaced repetition boundaries to better tune the efficiency of my learning. Spaced repetition is a learning technique that says "the more familiar you become with the thing in question (in my case, vocabulary) the greater the interval between practice attempts increases". I measure this by increasing and decreasing the 'streak' of a word after it has been practiced. A word with a low streak needs to be practiced more frequently; a word with a high streak needs to be practiced less frequently.

This Data Science project was aimed to help improve my understanding of my learning efforts since May 2020, and guide my findings.

**_TL;DR:_**
* Context: Created a revision algorithm using spaced repetition for studying Japanese vocabulary.
* Built Analysis tool to verify effectiveness on spaced repetition algorithm used.
* Scraped additional detail on vocabulary to provide further insights.
* Practiced vocabulary using different samples of boundaries in spaced repetition algorithm
* Analysed data to confirm algorithm was appropriately tuned to enhance my efficiency at learning.
* Chose sample with X% faster learning rate that demonstrated long-term recollection.

##  Code and resources
* Python version: 3.7
* Packages: pandas, numpy, matplotlib, seaborn, json, BeautifulSoup, datetime, webbrowser, re, requests

## Data Collection
A lot of the data is separated into different fact and dimension files for reporting purposes and so is not in the correct format to perform analysis on in the raw state. As this was my own dataset, I had created it with this kind of project work in mind so there was not much cleaning that was necessary.

**Existing data:**
* Dimensional Dictionary csv file

|   Word Index  |    English    |    Hiragana   |      Kanji    |    Date Added | Rank         |    Sample    | Is Active |
| ------------- | ------------- | ------------- | ------------- | ------------- |------------- |------------- |-----------|
|0              | house	        |いえ         	 |家	         |09/05/2020	 |1	            |1             |0          |
|1	            |(someone's) house	|おたく      |お宅            |09/05/2020     |1             |1             |0          |
|...        	|...        	|...        	|...        	 |...        	 |...        	|...           |...        |
|611	        |factory        |こうじょう	      |工場	            |17/02/2021     |3             |4             |1          |
|612	        |last train     |しゅうでん	      |終電	            |17/02/2021     |3	           |5	          |1          |

* Dimensional Streak csv file

| |  Word Index  |    Streak     |    Date   |      Sample    | 
| - |------------- | ------------- | --------- | -------------- | 
|0|0	|10|05/09/2020|	1|
|1|1	|10|05/10/2020|	1|
|2|2	|10|04/10/2020|	1|
|3|3	|8 |07/02/2021|	1|

* Fact Results csv file

|   |  Word Index  |    Index Relation     |    Result  |      Date    |  Time |
| - |------------- | -------------  | --------- | -------------- | ----- | 
|1|35|4|1|14/05/2020|23:39:27|
|2|9|5|1|14/05/2020|23:39:40|
|...|...            |...  |... |...        |...   |
|16890|492|0|1|03/03/2021|18:24:12|
|16891|611|0|1|03/03/2021|18:24:22|

* Fact Streak csv file

| |  Word Index  |    Streak     |    Date   |      Sample    | 
| - |------------- | ------------- | --------- | -------------- | 
|1|1	|10|05/10/2020|	1|
|2|	1|	8|	04/08/2020|	1|
|... |...  |... |...        |...   |
|5620|	611|	1|	19/02/2021|	4|
|5621|	612|	1|	19/02/2021|	5|

The samples referred to above are the following lists:

Sample 1 = [0, 1, 2, 4, 7, 12, 12, 31, 31, 31, 31]

Sample 4 = [0, 1, 2, 3, 5, 10, 10, 31, 31, 31, 31]

Sample 5 = [0, 1, 1, 2, 4, 6, 10, 10, 31, 31, 31, 31]

Each element represents the # days that must pass from the last practiced attempt before the word is next practiced at the given streak.

Please note I have not detailed each column as several are out-of-scope for this project.

## Data Cleaning
To make all this data usable and useful during analysis, I performed the following actions:
* Concatenated data for word-by-word analysis, including success measures
* Scraped missing data descriptions
* Converted date data for time-series analysis purposes

**Missing Data:**
* Japanese Learning Proficiency Test (JLPT) grade
* Generalised level (personal grade boundaries)

I would need to do some scraping to get the JLPT grades for each word / expression, as this was something not included in my data. The ever useful Japanese online dictionary site [Jisho](https://jisho.org/) contained the JLPT grades I needed for this analysis. Looping through each word in my personal dictionary and scraping the relevant JLPT grade from the site was then added to my Pandas DataFrame.

I also wanted some qualitative description of the streak values, which demonstrates my mastery of the vocabulary.


## Exploratory Data Analysis
The analysis phase began gathering insights on the data in the following fields:
* Words per JLPT grades
* Words per sample
* Words per day(?)
* Age vs streak achieved
-- Note which files this data comes from (?)

First up is the daily count of practices. We can see that when this project started back in May and June last year the number of daily practices was a lot higher, no doubt enhanced by the initial enthusiasm and energy to the project in lockdown, but also due to the inefficiency of some aspects of the model and algorithm, which required more random practices to ensure all words required that day were practiced. As this was tuned, fewer attempts were required and the numbers generally drop.



Breaking down the size of my samples gives me confidence that I am evaluating and drawing conclusions on an appropriate sample of data. We are ignoring sample 2 and 3 for the purpose of this research, but do not beed to go into this here. Sample 1 also has been subject to many changes in the underlying code during the lifecycle of this project, so a subset of this is used for analysis - I shall explain this a bit later on.





This initial investigation gave me some insight I had overlooked initially: Some of the older words (possibly configured with poor streak boundaries / streak practice thresholds (new phrasing to use?)) have not been able to progress particularly far. 
This led me to implement logic in my program which raises these words as a notification for me, giving the option to reset the word back to streak 0, for re-practicing. Resetting these means that the words are practiced more frequently again, and I have a better chance of recollection. I will store these refreshed words to keep a specific view on, which will be investigated separate to this project.

Now that I have some insight into how my data is categorised and what my efforts look like on a day-to-day basis, I want to see how I can improve the efficiency of my studies: minimizing the time to learn a word and maintain long-term recollection of it.

I consider a streak of 5 to be when I have mastered a word and as such want to evaluate the time taken to get here and the recollection ability at this point. 
Before digging into the data and drawing comparisons, I made a note that the data in sample 1 has gone through several iterations as the algorithm has been improved during the creation of the app. As can be seen in the below graph, the month-on-month average number of days for a word to reach streak 5 for the sample has decreased over time as the model has improved. Due to this, I am drawing comparisions for words from 09/2020 onwards.

![alt text](https://github.com/MattPCollins/Analysis/blob/master/Screenshots/rolling_avg_sample1_all.png "Rolling Avg Duration: Sample 1")

Comparing the average number of days to this target streak for each sample against both each other, and the minimum number of days possible for the sample itself, I found the following results.

Sample 1  
Absolute minimum of 15 days to reach streak 5 for sample 1  
Number of words in sample: 121  
Average of 29.61 days to reach streak 5 for sample 1  
Observed minimum of 14 days to reach streak 5 for sample 1  
Observed maximum of 149 days to reach streak 5 for sample 1  
![alt text](https://github.com/MattPCollins/Analysis/blob/master/Screenshots/rolling_avg_sample1_recent.png "Rolling Avg Duration: Sample 1 Short")
*note anomaly: min of 15, somehow observed min of 14

Sample 4  
Absolute minimum of 12 days to reach streak 5 for sample 4  
Number of words in sample: 19  
Average of 24.89 days to reach streak 5 for sample 4  
Observed minimum of 14 days to reach streak 5 for sample 4  
Observed maximum of 45 days to reach streak 5 for sample 4  
![alt text](https://github.com/MattPCollins/Analysis/blob/master/Screenshots/rolling_avg_sample4.png "Rolling Avg Duration: Sample 4")

Sample 5  
Absolute minimum of 9 days to reach streak 5 for sample 5  
Number of words in sample: 16  
Average of 25.62 days to reach streak 5 for sample 5  
Observed minimum of 15 days to reach streak 5 for sample 5  
Observed maximum of 44 days to reach streak 5 for sample 5  
![alt text](https://github.com/MattPCollins/Analysis/blob/master/Screenshots/rolling_avg_sample5.png "Rolling Avg Duration: Sample 5")

The boxplot below gives greater weight to these results, showing the variation between the samples, and how the data truly sits.
![alt text](https://github.com/MattPCollins/Analysis/blob/master/Screenshots/boxplot.png "Boxplot")

The larger sample of data for sample 1

streak 4 - 

Generally the words in this sample have been more consistently in less time than the other samples. slightly more outliers than sample 5, but given the spread of data is closer to the average makes it a better choice.

Given that I want to evaluate the performance of each sample, understanding their weak points is important. The below visuals shows the number of occurrences a word decreased from streak n to n-1.
the following graph shows streak 5 to be a weak point - potentially too greater time between previous streaks to retain the spelling (would maybe look at the distribution of words in each rank (normalise for each sample)

![alt text](https://github.com/MattPCollins/Analysis/blob/master/Screenshots/streak_decrease_sample1.png "Streak Degradation: Sample 1")

![alt text](https://github.com/MattPCollins/Analysis/blob/master/Screenshots/streak_decrease_sample4.png "Streak Degradation: Sample 4")

more consistent degradations (potentially not enough data collected), suggesting good retention generally between each streak.
ideally want comparable sample sizes. (potentially shrink sample 1, add more words to 4 and 5 (3 each, daily)

![alt text](https://github.com/MattPCollins/Analysis/blob/master/Screenshots/streak_decrease_sample5.png "Streak Degradation: Sample 5")


This shows that across the samples, streak 5 is generally the weakest (we ignore streak 0 as the word is just being learned for the first time and we do expect failures!), hence is a good target to improve upon.


What was I interested in seeing:
Streak regression for each sample
Min days to streak N and streak M
Avg days to streak N and streak M
Variation in above.
Avg success for samples

## Model Tuning



## Project Outcome / Things I learned
