import pandas
import logging
import pathlib

# Créer le répertoire logs s'il n'existe pas
log_dir = pathlib.Path("logs")
log_dir.mkdir(exist_ok=True)

# Configurer le logger
logging.basicConfig(level=logging.INFO,
                    format="[%(asctime)s][%(levelname)s][Paycare:ETL] %(message)s",
                    handlers=[
                        logging.FileHandler(log_dir / "etl.log", mode="w", encoding="utf-8"), 
                        logging.StreamHandler()
                    ])

_logger = logging.getLogger(__name__)

def _log_info(msg, *args, **kwargs):
    _logger.info(msg, *args, **kwargs)

def _log_error(msg, *args, **kwargs):
    _logger.error(msg, *args, **kwargs)

# Step 1: Extract
def extract_data(file_path):
    """
    Extracts data from a CSV file.
    """
    try:
        data = pandas.read_csv(file_path)
        _log_info("Data extraction successful.")
        return data
    except Exception as e:
        _log_error(f"Error in data extraction: {e}")
        return None

# Step 2: Transform
def transform_data(data):
    """
    Transforms the data by cleaning and adding new features.
    """
    try:
        # Drop rows with missing values
        data_cleaned = data.dropna().copy()
        
        # Add a new column for Tax (assuming a flat 10% tax rate on salary)
        data_cleaned['tax'] = data_cleaned['salary'] * 0.1
        
        # Calculate net salary after tax
        data_cleaned['net_salary'] = data_cleaned['salary'] - data_cleaned['tax']
        
        _log_info("Data transformation successful.")
        return data_cleaned
    except Exception as e:
        _log_error(f"Error in data transformation: {e}")
        return None

# Step 3: Load
def load_data(data, output_file_path):
    """
    Loads the transformed data into a new CSV file.
    """
    try:
        data.to_csv(output_file_path, index=False)
        _log_info(f"Data loaded successfully to \"{output_file_path}\".")
    except Exception as e:
        _log_error(f"Error in data loading: {e}")

# Main ETL function
def etl_process(input_filepath, output_filepath):
    data = extract_data(input_filepath)
    if data is not None:
        transformed_data = transform_data(data)
        if transformed_data is not None:
            load_data(transformed_data, output_filepath)

if __name__ == "__main__":
    import os

    LOCAL_OUTPUTS_DIRECTORY = "outputs"
    LOCAL_INPUTS_DIRECTORY = "inputs"

    OUTPUT_DATA_FILENAME = "output_data.csv"
    INPUT_DATA_FILENAME = "input_data.csv"

    if not os.path.exists(LOCAL_OUTPUTS_DIRECTORY):
        os.mkdir(LOCAL_OUTPUTS_DIRECTORY)
    
    assert os.path.exists(LOCAL_OUTPUTS_DIRECTORY)
    assert os.path.exists(LOCAL_INPUTS_DIRECTORY)

    output_filepath = os.path.join(LOCAL_OUTPUTS_DIRECTORY, OUTPUT_DATA_FILENAME)
    input_filepath = os.path.join(LOCAL_INPUTS_DIRECTORY, INPUT_DATA_FILENAME)
    assert os.path.exists(input_filepath)

    etl_process(input_filepath, output_filepath)