import sys,os
path=os.path.dirname(os.path.abspath(__file__))    
def get_dir_explorer(path:os.path.dirname=None):
    """
    Returns a directory paths, files and others for the given path.
    Parameters:
    path (str): The path to the directory. If None, uses the current working directory.
    Returns:
    dict: A dictionary containing the directory structure.
    """
    if path is None:
        path = os.getcwd()
    if not os.path.isdir(path):
        raise ValueError(f"The path {path} is not a valid directory.")
    result=os.walk(path)
    for root, dirs, files in result:
        print(f"Root: {root}")
        print("Directories:")
        for dir_name in dirs:
            print(f"  - {dir_name}")
        print("Files:")
        for file_name in files:
            print(f"  - {file_name}")
        print("\n")


get_dir_explorer(path)