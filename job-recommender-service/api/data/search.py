import openai
import pandas as pd
import numpy as np
import sqlalchemy
import os
from openai import OpenAI

os.environ["OPENAI_API_KEY"] = ""
client = OpenAI()
df_job_skills_cat = pd.read_csv('static/job_skills_cat.csv')
all_job_cat = ",".join("\'" + df_job_skills_cat['job_skills_new'] + "\'")
skill_cat_mapping = df_job_skills_cat.set_index('job_skills_new')['id'].to_dict()
engine_linkin_job = sqlalchemy.create_engine('sqlite:///linkin_job.db')
def setskillid(skill_new):
    return skill2000_id_mapping.get(skill_new, 0)

def search(skill, state, position):
    sql_query = """
    SELECT linkedin_job_all.job_link,job_skills, job_summary, job_title, company, city, state,job_level,job_type,first_seen
    FROM linkedin_job_all
    INNER JOIN job_skills_detail
    ON linkedin_job_all.job_link = job_skills_detail.job_link
    """
    if(skill!=""):
        llmstring=callllm(skill)
        llmret = skill_cat_mapping.get(llmstring, 0)
    liststring=[]
    wherestr=" "
    if (skill!=""):
        liststring.append("job_skills_detail.skills_cat_id =" + str(llmret))
    if (state!=""):
        liststring.append("TRIM(linkedin_job_all.state) ='" + state + "'")
    if (position!=""):
        liststring.append("TRIM(linkedin_job_all.job_title) ='" + position + "'")
    if len(liststring)>0:
        wherestr=" where " + " and ".join(liststring)
    sql_query=sql_query+wherestr
    with engine_linkin_job.connect() as connection:
        df_search = pd.read_sql_query(sql_query, connection)
        df_search.to_csv('query_results.csv', index=False)
        return df_search

def callllm(job_skills):
    promptvar='select the following skill which is closest to ' +   job_skills + ': '+ all_job_cat
    completion = client.completions.create(
      model="gpt-3.5-turbo-instruct",
      prompt=promptvar
    )
    llmstring=completion.choices[0].text.strip().lower()
    return llmstring

if __name__ == '__main__':
    search("Python Collaboration Coding", "CA",  "Senior Software Engineer")