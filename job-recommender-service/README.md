# job-recommender-service

Backend services that host scripts to intilize database, notebooks for data cleaning and processing, and APIs.

## Dependencies

- [flask](https://palletsprojects.com/p/flask/): Python server of choise
- [flasgger](https://github.com/flasgger/flasgger): Used to generate the swagger documentation
- [flask-marshmallow](https://flask-marshmallow.readthedocs.io/en/latest/): My favourite serializer
- [apispec](https://apispec.readthedocs.io/en/latest/): Required for the integration between marshmallow and flasgger

## Set Up

1. Check out the code
2. Install requirements
    ```
    sudo pip install pipenv  ==> if pipenv is not installed
    pipenv install
    ```
3. Start the server with:
    ```
   pipenv run python -m flask run
    ```

4. Visit http://127.0.0.1:5000/api for the home api