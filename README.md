GitHub Actions
===

Paycare
---

180 min.

You’ve been hired as a DevOps Engineer at PayCare, a mid-sized payroll processing company that handles salary and tax calculations for multiple clients. PayCare processes monthly payroll data submitted by clients in CSV format. The company uses an ETL (Extract, Transform, Load) pipeline to clean the raw data, calculate tax and net salaries, and output a clean payroll report.

To ensure reliable and automated payroll processing, PayCare is transitioning to a more automated system using Docker for containerization and GitHub Actions for continuous integration (CI). Your task is to automate this process and ensure the system is tested and deployable in an automated CI pipeline.

# Your Tasks

PayCare’s payroll data pipeline currently consists of 3 stages:
1. **Extract**: Read raw payroll data from a CSV file.
2. **Transform**: Clean the data by removing invalid entries and adding tax and net salary columns.
3. **Load**: Save the cleaned and processed data into a new CSV file.

The provided script automates these steps, but the system needs to be further developed into a **containerized application** with automated testing 
and a **GitHub Actions CI workflow. You will need to:

1. **Write a Dockerfile** to containerize the ETL pipeline and run it locally.
2. **Write unit tests** for each step of the ETL pipeline (e.g., data extraction, transformation, loading).
3. **Create a GitHub Actions** workflow that automates testing, building, and running the application in Docker.

# Scenario

You are provided with an initial Python script that handles the ETL process for payroll data. The company requires you to extend this by:

1. **Writing a Dockerfile** to containerize the application.
2. **Writing tests** to ensure the code works as expected.
3. **Building a GitHub Actions workflow** to automate testing, building the Docker image, and running the containerized application.

# Phase 1: Write the Dockerfile

You need to containerize the Python ETL application using Docker. The Dockerfile will allow anyone in the company to run the ETL pipeline locally or in a production environment with the necessary dependencies packaged in a container.

The Docker container will:
- Install necessary dependencies (e.g., Pandas).
- Run the ETL script (etl.py) that reads input data from a CSV file, processes it, and saves the output.

## Dockerfile Requirements
1. Base the Docker image on an official Python image (e.g., `python:3.9`).
2. Install dependencies (e.g., `pandas`, plus anything listed in `requirements.txt`).
3. Copy the ETL code into the image and set an appropriate working directory.
4. Ensure that the Docker container can be run with mounted volumes for both the input and output CSV files (so that the pipeline can read and write files on the host).

# Phase 2: Write Tests

You will write unit tests to ensure that the extraction, transformation, and loading steps work as expected. The tests should check for:

1. Data Extraction: Test that the input CSV file is read correctly.
2. Data Transformation: Test that the cleaning and tax/net salary calculation steps are performed correctly.
3. Data Loading: Test that the processed data is saved correctly to an output file.

## Testing Requirements
- Use `pytest` to write unit tests for the ETL functions (`extract_data`, `transform_data`, and `load_data` or the equivalent functions in `etl.py`).
- Mock the CSV file input and output where necessary (e.g., using temporary files or in-memory DataFrames).
- Ensure tests cover potential edge cases (e.g., missing values in the input file, negative salaries, invalid tax rates).

# Phase 3: Automate with GitHub Actions (CI Workflow)

Now that you’ve containerized the application and written tests, your final task is to create a GitHub Actions workflow that automates the following steps:
1. Clone the Repository: The workflow will pull the latest code from your PayCare repository.
2. Run Tests: The workflow will run the tests you’ve written to validate the ETL pipeline’s functionality.
3. Build the Docker Image: The workflow will build the Docker image using the Dockerfile you wrote.
4. Run the Container: The workflow will run the Docker container, passing an input CSV file and generating the output file.
5. (Optional) Publish Artifacts / Logs: The workflow can upload the processed CSV and test reports as artifacts for inspection.

## GitHub Actions Workflow Requirements
- Create a workflow file at: `.github/workflows/ci.yml`
- The workflow should:
    1. Check out the repository (using actions/checkout).
    2. Set up Python (using actions/setup-python).
    3. Install dependencies (e.g., pip install -r requirements.txt and pytest).
    4. Run the pytest tests to validate the ETL pipeline.
    5. Build the Docker image using your Dockerfile.
    6. Run the Docker container, ensuring that:
        - An input CSV is available (for example, by using the data/ folder from the repo or a test CSV).
        - Volumes are mounted correctly so the output CSV file is written to a known location.
    7. Fail the workflow if tests fail or if the container exits with a non-zero status code.
    8. (Optional) Upload artifacts such as the processed CSV or test reports using actions/upload-artifact.

## Workflow Structure (High-Level)
- **Job: test-and-build**
    - **Step 1: Checkout Repository**
        - Use `actions/checkout@v4` to pull the latest code.
    - **Step 2: Set Up Python & Install Dependencies**
        - Install requirements and `pytest`.
    - **Step 3: Run Tests**
        - Run `pytest` to validate the ETL logic.
    - **Step 4: Build Docker Image**
        - Run `docker build -t me/paycare .`
    - **Step 5: Run Container**
        - Run the Docker container with appropriate volume mounts
            - e.g.:
       `docker run -v $(pwd)/app/data:/app/data me/paycare`
    - Step 6: (Optional) Upload Artifacts
        - Use `actions/upload-artifact` to store the output CSV or logs.

## Application Code (Starting Point)

The application code that you will be working with can be found here:
- https://github.com/JedhaBootcamp/paycare

> **IMPORTANT** | Don't forget to fork 🍴
> 
> Don't forget to fork the repo if you want to be able to make edits! 😉

## Deliverables
1. A **Dockerfile** that containerizes the ETL process.
2. **Unit tests** using `pytest` to validate each step of the ETL pipeline.
3. A **GitHub Actions workflow file** (`.github/workflows/ci.yml`) that automates the CI process:
    - Running tests.
    - Building the Docker image.
    - Running the Docker container to process payroll data.
    - (Optionally) Uploading the output CSV and/or test reports as artifacts.


# Worksace
````
cd [...]/paycare
docker built -t me/paycare .
docker run -v $(pwd)/app/data:/app/data me/paycare
```