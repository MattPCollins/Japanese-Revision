from dropoff import webInfo, jlptGrade
import pandas as pd

# get csv to df for preparation
path = '/Users/mattcollins/Projects/MyProject/KanjiProgram/csvs/word_dictionary.csv'
df = pd.read_csv(path)
kanjis = df['kanji']

# scrape grades
grades = []
for kanji in kanjis:
    print(kanji)
    webstring = webInfo(kanji)
    grade = jlptGrade(webstring)
    grades.append(grade)

print(grades)

