import os
import nbformat
from nbconvert.preprocessors import ExecutePreprocessor
from nbconvert.preprocessors import CellExecutionError

def run_notebook(notebook_path): # Execute a Jupyter Notebook and return its status (Success or Error).
    
    try:
        with open(notebook_path) as f:
            nb = nbformat.read(f, as_version=4)
            ep = ExecutePreprocessor(timeout=600, kernel_name='python3')
            ep.preprocess(nb, {'metadata': {'path': './'}})
        return True, None  # Success
    
    except CellExecutionError as e:
        return False, str(e)  # Failed with error message
    
    except Exception as e:
        return False, str(e)  # Other error

def run_all_notebooks(directory): # Run all Jupyter Notebooks in a given directory and collect those that fail.
    
    error_notebooks = []

    for filename in os.listdir(directory):
        
        if filename.endswith(".ipynb"):
            notebook_path = os.path.join(directory, filename)
            print(f"Running: {filename}")
            success, error = run_notebook(notebook_path)
            
            if not success:
                error_notebooks.append((filename, error))
                print(f"Error in {filename}: {error}")

    return error_notebooks

if __name__ == "__main__": # Makes script executable from command line
    
    notebook_dir = '../default-notebooks/Python_Tutorials' # Directory where notebooks are stored
    
    failed_notebooks = run_all_notebooks(notebook_dir) # Run all notebooks in the directory

    # Report results
    if failed_notebooks:
        print("\nFailed Notebooks:")
        for notebook, error in failed_notebooks:
            print(f"{notebook}: {error}")

    else:
        print("\nAll notebooks ran successfully!")