<---------- DESCRIPTION ------------>
# Project InteractivePersonalizedJobRecommender

Under the root directory, there are 
1. `job-recommender-service` is the root directory for Python flask service and scripts/notebooks for data process and API
2. `job-recommender-ux` is the root directory for React frontend project

You need to following the instruction below to start both projects locally

<---------- INSTALLATION ------------>
# job-recommender-service

Backend services that host scripts to intilize database, notebooks for data cleaning and processing, and APIs.

## Dependencies

- [flask](https://palletsprojects.com/p/flask/): Python server of choise
- [flasgger](https://github.com/flasgger/flasgger): Used to generate the swagger documentation
- [flask-marshmallow](https://flask-marshmallow.readthedocs.io/en/latest/): My favourite serializer
- [apispec](https://apispec.readthedocs.io/en/latest/): Required for the integration between marshmallow and flasgger
- pandas
- openai
- sqlalchemy
- nltk
- All dependencies are located in Pipfile

## Set Up

1. Initialize the database.
- place the extracted data file into the `job-recommender-service/api/data`. The data set could be found at [Kaggle's website](https://www.kaggle.com/datasets/asaniczka/1-3m-linkedin-jobs-and-skills-2024)
- There should be three files - jpb_skills.csv, job_summary.csv, linkedin_job_postings.csv
- run script`job-recommender-service/api/data/MigratetoDB.py`. This will initialize the database with data in the csv file
2. In `job-recommender-service/api/data/search.py` file. Set the OPENAPi Api key `os.environ["OPENAI_API_KEY"] = ""`. To acquaire a API key, visit https://platform.openai.com/api-keys
3. Check out the code
4. Install requirements
    ```
    sudo pip install pipenv  ==> if pipenv is not installed
    pipenv install
    ```
5. Start the server with:
    ```
   pipenv run python -m flask run
    ```
6. Visit http://127.0.0.1:5000/api for the home api


# job-recommender-ux
React frontend for interactive job recommender app.

## Dependencies
Make sure you install Node v16.x.x

## Start Project
Under the directory of `jon-recommender-ux`
1. run `npm install`
2. run `npm start` to start
3. Go to browser `localhost:3000`


# Tableau Template
For each query triggered from UI, it will generate `query_results.csv`, in the reail world, our Tableau server will take it as input for visualization.
We provide a `job-recommender-service/api/data/Template.twb` which we used to visualize the data and display the visualizations on our webapp.

An example of the dashboard is https://public.tableau.com/app/profile/bohan.ye/viz/Template_17132059522630/Dashboard?publish=yes

Both projects should be started without any exception. Now, you can have fun with job searching easily!


<---------- EXECUTION ------------>
1. Open the web app at localhost:3000
2. Fill the forms with State = "All State", Position = "Senior Software Engineer", Skills = "Python Collboration Data Visualization"
3. Click "Search" Button
4. Wait for a while and you will see the visualization and recommended jobs