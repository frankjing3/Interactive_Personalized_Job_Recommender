import pandas as pd
import numpy as np
import sqlalchemy
import re


def split_location(location):
    parts = location.split(',')
    if len(parts) >= 2:
        return parts[0], parts[1]
    elif len(parts) == 1:
        return parts[0], None
    else:
        return None, None



engine_linkin_job = sqlalchemy.create_engine('sqlite:///linkin_job.db')

df_linkedin_job_summary = pd.read_csv('job_summary.csv')
df_linkedin_job_skills = pd.read_csv('job_skills.csv')
df_linkedin_job_postings = pd.read_csv('linkedin_job_postings.csv')
df_linkedin_job_skills = df_linkedin_job_skills.dropna()
df_linkedin_job_summary = df_linkedin_job_summary.dropna()
df_linkedin_job_postings = df_linkedin_job_postings.dropna()

df_linkedin_job_postings = df_linkedin_job_postings[df_linkedin_job_postings['got_summary'] != 'f']

df_linkedin_job_postings = df_linkedin_job_postings[df_linkedin_job_postings['got_ner'] != 'f']

df_linkedin_job_postings = df_linkedin_job_postings[df_linkedin_job_postings['is_being_worked'] != 't']

df_linkedin_job_postings[['city', 'state']] = df_linkedin_job_postings['job_location'].apply(split_location).apply(pd.Series).copy()

df_linkedin_job_skills['job_skills'] = df_linkedin_job_skills['job_skills'].str.lower()

df_linkedin_job_all = pd.merge(df_linkedin_job_skills, df_linkedin_job_summary, on='job_link', how='inner')
df_linkedin_job_all = pd.merge(df_linkedin_job_all, df_linkedin_job_postings[['job_link', 'job_title', 'company', 'city', 'state','job_level','job_type','first_seen']], on='job_link', how='inner')

df_linkedin_job_all = df_linkedin_job_all[['job_link', 'job_skills', 'job_summary', 'job_title', 'company', 'city', 'state','job_level','job_type','first_seen']]


rows = []

for index, row in df_linkedin_job_all.iterrows():
    job_link = row['job_link']
    job_skills = row['job_skills']
    if isinstance(job_skills, str):
        job_skills = job_skills.split(',')  # Splitting skills by comma
        for skill in job_skills:
            skill_cleaned = re.sub(r'[^\w\s]', '', skill.strip())
            rows.append({'job_link': job_link, 'job_skills_new': skill_cleaned})
df_job_skills_detail = pd.DataFrame(rows)

df_job_skills_detail['id'] = range(1, len(df_job_skills_detail) + 1)

df_job_skills_detail = df_job_skills_detail[['id', 'job_link', 'job_skills_new']]

from nltk.stem.snowball import EnglishStemmer
def skills_stem(text):
    if isinstance(text, str):
        stemmer = EnglishStemmer()
        words = text.split()
        stem_words = [stemmer.stem(word) for word in words]
        return " ".join(stem_words)
    else:
        return text
from collections import Counter

df_job_skills_detail['job_skills_stem'] = df_job_skills_detail['job_skills_new'].apply(skills_stem)
counts = Counter(df_job_skills_detail['job_skills_new'])
top2000_skills = counts.most_common(2000)
df_job_skills_2000 = pd.read_csv('job_skills_2000.csv')
df_job_skills_cat = pd.read_csv('job_skills_cat.csv')
skill2000_id_mapping = df_job_skills_2000.set_index('job_skills_new')['skills_cat_id'].to_dict()
def setskillid(skill_new):
    return skill2000_id_mapping.get(skill_new, 0)
df_job_skills_detail['skills_cat_id'] = df_job_skills_detail['job_skills_new'].apply(setskillid)

df_job_skills_detail.to_sql('job_skills_detail', con=engine_linkin_job, if_exists='replace', index=False)
df_linkedin_job_all.to_sql('linkedin_job_all', con=engine_linkin_job, if_exists='replace', index=False)
df_job_skills_2000.to_sql('job_skills_2000', con=engine_linkin_job, if_exists='replace', index=False)
df_job_skills_cat.to_sql('job_skills_cat', con=engine_linkin_job, if_exists='replace', index=False)
