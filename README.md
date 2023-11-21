# Candidates CRUD API
This API is used to Create, Read, Update and Delete the Candidate details.

## Prerequisites
 You should have installed [python3](https://www.python.org/downloads/), [Django](https://docs.djangoproject.com/en/4.2/topics/install/#installing-an-official-release-with-pip) and [Git](https://www.git-scm.com/downloads)

## Installation
1. Clone the project from GitHub
    ```git
    git clone https://github.com/koushikromel/candidate_app.git
    ```
2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3. Run the application:
    ```py
    python3 manage.py makemigrations
    python3 manage.py migrate
    python3 manage.py createsuperuser (and create superuser with your desired username and password)
    python3 manage.py runserver 127.0.0.1:8000
    ```

## Initialization
   Project need to setup by pre entered values in the admin panel. visit ```http://127.0.0.1:8000/admin``` after logged in enter all the values other than CandidateDirectory to support the development process when performing CRUD operations on CandidateDirectory.

## Endpoints
1. Read All Candidate Detail
    - Method: GET
    - Endpoint: http://127.0.0.1:8000/
    - Description: Displays the list of all created candidates.

2. Read Candidate Detail
    - Method: GET
    - Endpoint: http://127.0.0.1:8000/{candidate_id}/
    - Parameters:
        - candidate_id: int
    - Description: Display the detail of the candidate with {candidate_id}.

3. Create Candidate Detail
    - Method: POST
    - Endpoint: http://127.0.0.1:8000/new/
    - Description: Create a new candidate.

4. Edit Candidate Detail
    - Method: POST
    - Endpoint: http://127.0.0.1:8000/{candidate_id}/edit/
    - Parameters:
        - candidate_id: int
    - Description: Displays the list of all created candidates.

5. Delete Candidate Detail
    - Method: POST
    - Endpoint: http://127.0.0.1:8000/{candidate_id}/delete/
    - Parameters:
        - candidate_id: int
    - Description: Displays the list of all created candidates.

## License
This Project is licensed under the MIT License - see the [License](https://choosealicense.com/licenses/mit/) file for details.
