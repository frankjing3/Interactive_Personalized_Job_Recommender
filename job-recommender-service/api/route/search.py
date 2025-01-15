from http import HTTPStatus
from flask import Blueprint
from api.model.recommended_job import RecommendedJobModel
from api.schema.recommended_job import RecommendedJobSchema
from pyspark import *
import pandas as pd
from flask import request
from api.data.search import search as search_data

search_api = Blueprint('api', __name__)

@search_api.route('/search', methods = ['POST'])
def search():
    request_body = request.json
    try:
        search_result = search_data(request_body["skills"], request_body["state"], request_body["position"])
    except:
        search_result = pd.read_csv('static/query_results.csv')
    results = []
    for index, row in search_result.iterrows():
        model = RecommendedJobModel()
        model.jobLink = row['job_link']
        model.jobSkills = row['job_skills']
        model.jobTitle = row['job_title']
        model.jobLevel = row["job_level"]
        model.company = row['company']
        model.city = row['city']
        model.state = row['state']
        model.jobType = row['job_type']
        model.jobSummary = row['job_summary']
        model.firstSeen = row['first_seen']
        results.append(RecommendedJobSchema().dump(model))
    return results, 200


if __name__ == '__main__':
    search()