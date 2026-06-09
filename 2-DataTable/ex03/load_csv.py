import pandas as pd


def load(path: str) -> pd.DataFrame | None:
    '''
    Takes a path as argument, writes the dimensions of the data set
    and returns it.
    Returns None in case of error (bad path, bad format, etc.).
    '''
    try:
        dataset = pd.read_csv(path)
        print(f"Loading dataset of dimensions: {dataset.shape}")
        return dataset
    except FileNotFoundError:
        print(f"Error: file not found: {path}")
        return None
    except pd.errors.EmptyDataError:
        print(f"Error: empty file: {path}")
        return None
    except pd.errors.ParserError:
        print(f"Error: bad CSV format: {path}")
        return None
    except Exception as e:
        print(f"Error loading dataset: {e}")
        return None
