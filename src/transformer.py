import logging
import pandas as pd

logger = logging.getLogger(__name__)

def transform_data(api_data):
    if not api_data:
        logger.warning("No data to transform")
        return None

    # Structure JSON into a table
    df = pd.json_normalize(api_data)

    #Cleaning logic
    if "gender" in df.columns:
        df["gender"] = df["gender"].apply(
            lambda x: "male" if x == "m"
            else "female" if x == "f"
            else None
        )

    logger.info(f"Data transformed successfully | rows={len(df)}")

    return df