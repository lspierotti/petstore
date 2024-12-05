
## Objetive

The objective of this project is to test The PetStore API.


## Information

The Testsuite was designed so that the requests or endpoints used are stored in a single directory (folder: `services`). Thats mean if a request needs to be modified, it can be done in that single file without affecting the test (low coupling). This design pattern is called **Single Source of Truth (SSOT)** or aligns with the **DRY (Don't Repeat Yourself)** principle: it centralizes endpoint definitions in one location, so updates are made in a single place rather than throughout the project.

Additionally, various fixtures are implemented to assist in writing tests. One of them is **parametrize**, which aims to evaluate a test with *n* input data, resulting in *n* test cases. In other words, for *n* inputs, we obtain *n* tests while writing only a single test case.




## Environment Variables

The exercise is designed to evaluate the API in different environments:

    `dv`: develop

    `qa`: qa or "preproduction

    `pr`: production 

Since testing this API involves starting a local server (as mentioned in the exercise description "Quality_Engineer_-_Take_Home_Test"), the URL will point to: `https://localhost:8080`. 

In other words, **dv**, **qa**, and **pr** are fictional environment variables.



## About the project

- There are two test folders: `test_functional` and `test_bdd`. In the first folder we can see some functionals tests about some endpoints. The second folder `test_bdd` contains flow tests where the goal is to do a CRUD: create a pet, get it, uptdate it and  them remove it from the favorites.

- The `data.py` file contains variables that will be used in the test files (many of them are used in the test parameterizations).
  
- **IMPORTANT**: The token is provided through my personal account. It is stored in a variable called `TOKEN` in the data.py file. However, when committing the code, we will not include it. This means the tests will not run unless the corresponding key is provided.

- **IMPORTANT**: In the `conftest.py` file, the logic for the project is defined. It was designed to be run either locally or from a Jenkins environment. However, what is commonly done is making a request with certain credentials to authenticate. Since we don't have access to that request, the tokens are hardcoded.
 
- The `Logger.py` file and log.log simply log the events occurring in the tests.



- The files `config_local.ini` and `config_jenkins.ini` are identical. However, it may happen that to access an API from different machines, the URLs could be different. That's why this is left as an example.


## Running Tests

Read the following steps, to run the testsuite.
- The `pytest.ini` file sets the execution mode: either local or from jenkins.
- To run it in local way:

    - In the `pytest.ini` file, uncomment line 4 and edit the variable named:
        env_local
    - In the `pytest.ini` file, comment out line 3, as this is for executing via Jenkins. Note: remember to restore the file to its original state, meaning it should be ready for Jenkins execution. 

- The test suite is prepared to run both locally and from Jenkins. For the latter case, you need to create the Docker image and then run it with the following commands:
    ```bash
    docker build -t cat_api .
    docker-compose up
    ```

    To achieve this, some lines of the `docker-compose.yml` file need to be edited:

    - Line 8: This variable should be "pr". In this case, we are only executing requests to the "pr" environment of The Cat API.
    - Line 12: This is the Jenkins path. It should not be commented out.
    - To show how to create and run the image, we leave Line 13 uncommented with our local directory.



## Tech Stack

**Python:** Pytest, BDD

**Docker:** Dockerfile, Docker-compose

**Logger**



