# Japanese Vocabulary Revision Analysis: Overview

Over the work-from-home period of Covid-19 lockdown, I have been taking my Japanese studies more seriously, in particular around finally focus on writing Kanji. For anyone familiar with Kanji, they can appreciate the vast range of characters required to be mastered, and this was something I have previously struggled with.

While there are great revision apps already on the market, I wanted to kill two birds with one stone and create my own revision program in Python, as another avenue of self-development.

I created my own space repetition algorithm and populated my own dictionary of vocabulary to study. I created fact and dimensional tables to model my results and track my progress.

This Data Science project was aimed to help improve my understanding of my learning efforts since May, and guide my findings.

**_Tl;dr:_**
* Context: Created a revision algorithm using spaced repetition for studying Japanese vocabulary.
* Built Analysis tool to verify effectiveness on spaced repetition boundaries used.
* Scraped additional detail on vocabulary to provide further insights.
* Analysed data to confirm algorithm was appropriately tuned to enhance my efficiency at learning.
* X% faster at learning (to master level, to expert level), %Y percent higher efficiency rate

##  Code and resources
* Python version: 3.7
* Packages: pandas, numpy, matplotlib, seaborn, json, BeautifulSoup, datetime, webbrowser, re, requests

## Data Cleaning
A lot of the data is separated into different fact and dimension files for reporting purposes and so is not in the correct format to perform analysis on in the raw state. As this was my own dataset, I had created it with this kind of project work in mind so there was not much cleaning which was necessary.

**Existing data:**
* Dimensional Dictionary csv file
    * example table
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

## Model Tuning



### Project Outcome / Things I learned
