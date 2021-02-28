# Japanese Vocabulary Revision Analysis: Overview

Over the work-from-home period of Covid-19 lockdown, I have been taking my Japanese studies more seriously, in particular around finally focus on writing Kanji. For anyone familiar with Kanji, they can appreciate the vast range of characters required to be mastered, and this was something I have previously struggled with.

While there are great revision apps already on the market, I wanted to kill two birds with one stone and create my own revision program in Python, as another avenue of self-development.

I created my own space repetition algorithm and populated my own dictionary of vocabulary to study. I created fact and dimensional tables to model my results and track my progress.

This Data Science project was aimed to help improve my understanding of my learning efforts since May, and guide my findings.

**_Tl;dr:_**
* Context: Created a revision algorithm using spaced repetition for studying Japanese vocabulary.
* Built Analysis tool to verify effectiveness on spaced repetition boundaries (streak thresholds) used.
* Scraped additional detail on vocabulary to provide further insights.
* Analysed data to confirm algorithm was appropriately tuned to enhance my efficiency at learning.
* X% faster at learning while retaining long term recollection.

##  Code and resources
* Python version: 3.7
* Packages: pandas, numpy, matplotlib, seaborn, json, BeautifulSoup, datetime, webbrowser, re, requests

## Data Cleaning
A lot of the data is separated into different fact and dimension files for reporting purposes and so is not in the correct format to perform analysis on in the raw state. As this was my own dataset, I had created it with this kind of project work in mind so there was not much cleaning which was necessary.

**Existing data:**
* Dimensional Dictionary csv file (example rows below in screenshot)

|   Word Index  |    English    |    Hiragana   |      Kanji    |    Date Added | Rank         |    Sample    |
| ------------- | ------------- | ------------- | ------------- | ------------- |------------- |------------- |
| 0             | house         | いえ　         |  家           | 09/05/2020    |      1       |      1       |
| 1             | in the end    |　ひこうき     　| 飛行機         |  04/06/2020   |      5       |      2       |

* Dimensional Streak csv file
* Fact Results csv file
* Fact Streak csv file

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

## EDA
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
