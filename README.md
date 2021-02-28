# Japanese Vocabulary Revision Analysis: Overview

Over the work-from-home period of Covid-19 lockdown, I have been taking my Japanese studies more seriously, in particular around finally focus on writing Kanji. For anyone familiar with Kanji, they can appreciate the vast range of characters required to be mastered, and this was something I have previously struggled with.

While there are great revision apps already on the market, I wanted to kill two birds with one stone and create my own revision program in Python, as another avenue of self-development.

## App Background
I created my own space repetition algorithm and populated my own dictionary of vocabulary to study. I created fact and dimensional tables to model my results and track my progress.

My algorithm was experimentally created at first, but then introduced different samples of spaced repetition boundaries to better tune the efficiency of my learning. Spaced repetition is a learning technique that says "the more familiar you become with the thing in question (in my case, vocabulary) the more the interval between practice attempts increases". I measure this by increasing and decreasing the 'streak' of a word after it has been practiced. A word with a low streak needs to be practiced more frequently; a word with a high streak needs to be practiced less frequently.

This Data Science project was aimed to help improve my understanding of my learning efforts since May, and guide my findings.

**_Tl;dr:_**
* Context: Created a revision algorithm using spaced repetition for studying Japanese vocabulary.
* Built Analysis tool to verify effectiveness on spaced repetition algorithm used.
* Scraped additional detail on vocabulary to provide further insights.
* Practiced vocabulary using different samples of boundaries in spaced repetition algorithm
* Analysed data to confirm algorithm was appropriately tuned to enhance my efficiency at learning.
* Chose sample with X% faster learning rate that demonstrated long term recollection.

##  Code and resources
* Python version: 3.7
* Packages: pandas, numpy, matplotlib, seaborn, json, BeautifulSoup, datetime, webbrowser, re, requests

## Data Cleaning
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


* Fact Streak csv file

| |  Word Index  |    Streak     |    Date   |      Sample    | 
| - |------------- | ------------- | --------- | -------------- | 
|1|1	|10|05/10/2020|	1|
|0|	1|	8|	04/08/2020|	1|
|... |...  |... |...        |...   |
|5620|	611|	1|	19/02/2021|	4|
|5621|	612|	1|	19/02/2021|	5|

The samples referred to above are the following lists:
1,4,5 lists
Each element represents the # days that must pass from the last practiced attempt before the word is next practiced at the given streak.

To make all this data usable and useful during analysis, I performed the following actions:
* Concatenated the tables to get column for latest streak of the word
* Added columns for total attempts, total successful attempts and total unsuccessful attempts
* Created age column for more useful interpretation in time-series analysis later

**Missing Data:**
* Japanese Learning Proficiency Test (JLPT) grade
* Generalised level (personal grade boundaries)

I would need to do some scraping to get the JLPT grades for each word / expression, as this was something not included in my data. I also wanted some qualitative description of the streak values, which demonstrates my mastery of the vocabulary.

### Web Scraping
The ever useful Japanese online dictionary site [Jisho](https://jisho.org/) contained the JLPT grades I needed for this analysis. Looping through each word in my personal dictionary and scraping the relevant JLPT grade from the site was then added to my Pandas DataFrame.

-- show final result --

## Exploratory Data Analysis
Not sure any of above is useful for this...
The analysis phase began gathering insights on the data in the following fields:
* Words per JLPT grades
* Words per sample
* Words per day(?)
* 

I consider a streak of 5 to be when I have mastered a word and as such want to evaluate the time taken to get here and the recollection ability at this point. 
Before digging into the data and drawing comparisons, I made a note that the data in sample 1 has gone through several iterations as the algorithm has been improved during the creation of the app. As can be seen in the below graph, the month-on-month average number of days for a word to reach streak 5 for the sample has decreased over time as the model has improved. Due to this, I am drawing comparisions for words from 09/2020 onwards.

![alt text](https://github.com/MattPCollins/Analysis/blob/master/Screenshots/rolling_avg_sample1_all.png "Streak Degradation: Sample 1")

Given that I want to evaluate the performance of each sample, understanding their weak points is important. The below visual shows the number of occurrences a word decreased from streak n to n-1.

This shows that across the samples, streak 5 is generally the weakest (we ignore streak 0 as the word is just being learned for the first time and we do expect failures!), hence is a good target to improve upon.


The following results show 


I investigated the data distributions and statistics across the dataset. My most informative findings are below:
![alt text](https://github.com/MattPCollins/Analysis/blob/master/Screen%20Shot%202021-01-04%20at%2012.47.54.png "Poor retention")
![alt text](https://github.com/MattPCollins/Analysis/blob/master/Screen%20Shot%202021-01-04%20at%2012.44.52.png "Distribution of vocabulary grades")

The algorithm determines when a word next needs to be practiced based on a list, where the elements represent the number of days before the next attempt needs to be taken. The data contains 'samples', which use different variations of this list, as seen below:
Notes: include 1,4,5
When the model was first created, only sample 1 existed, whcih was refined and improved over time as can be seen in the following graph - for words added to the dicitionary on a month-by-month basis we can see that the average number of days to reach streak N decreased, through a combination of improving the model and refining the sample values.
However, the values in this list were arbtitrarily chosen, and efficiency could not be guaranteed. As a result, further samples were introduced for newly added words to compare the efficiencies and ensure a more optimal model was being used based on my practice rates and short comings.

Note: from above graph, we have seen a min point in Nov and Dec 2020. Limit data from sample 1 to avoid any misleading statistics.

What was I interested in seeing:
Streak regression for each sample
Min days to streak N and streak M
Avg days to streak N and streak M
Variation in above.
Avg success for samples

## Model Tuning



## Project Outcome / Things I learned
