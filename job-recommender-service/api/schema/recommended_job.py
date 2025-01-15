from flask_marshmallow import Schema
from marshmallow.fields import Str


class RecommendedJobSchema(Schema):
    class Meta:
        # Fields to expose
        fields = ["jobLink", "jobSkills", "jobSummary", "jobTitle", "company", "city", "state", "jobLevel", "jobType", "firstSeen"]

    jobLink = Str()
    jobSkills = Str()
    jobSummary = Str()
    jobTitle = Str()
    company = Str()
    city = Str()
    state = Str()
    jobLevel = Str()
    jobType = Str()
    firstSeen = Str()