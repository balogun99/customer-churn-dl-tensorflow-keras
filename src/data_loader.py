import pandas as pd

# df = pd.read_csv("/Users/macbookpro/Desktop/ML & DL & GENAI Projects/Deep Learning/projects/customer_churn_dl/data/raw/customer_churn_data.csv")

def load_dataset(path: str) -> pd.DataFrame:
    """
    Load dataset from CSV.

    Parameters
    ----------
    path : str
        Path to dataset.

    Returns
    -------
    pd.DataFrame
    """
    # df = pd.read_csv('/Users/macbookpro/Desktop/ML & DL & GENAI Projects/Deep Learning/projects/customer_churn_dl/data/raw/customer_churn_data.csv')

    df = pd.read_csv(path)

    return df