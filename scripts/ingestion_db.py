import pandas as pd
import os
import logging
import time
import gc
from sqlalchemy import create_engine

# Configure logging
logging.basicConfig(
    filename="logs/ingestion_db.log",
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
    filemode="a"
)

engine = create_engine(
    "sqlite:///inventory.db",
    connect_args={"timeout": 30}
)

def ingest_db(file_path, table_name, engine):
    first_chunk = True
    total_rows = 0

    for chunk in pd.read_csv(
        file_path,
        chunksize=50000,
        low_memory=False
    ):

        chunk.to_sql(
            name=table_name,
            con=engine,
            if_exists="replace" if first_chunk else "append",
            index=False
        )

        first_chunk = False

        total_rows += len(chunk)
        print(f"{table_name}: {total_rows:,} rows inserted...")

        del chunk
        gc.collect()

    print(f"{table_name} loaded successfully!")
    logging.info(f"{table_name} loaded successfully.")

    
def load_raw_data():

    start = time.time()

    data_folder = "data"

    if not os.path.exists(data_folder):
        print("Data folder not found.")
        return

    csv_files = [f for f in os.listdir(data_folder) if f.endswith(".csv")]

    print(f"Found {len(csv_files)} CSV files.\n")

    for file in csv_files:

        file_path = os.path.join(data_folder, file)
        table_name = os.path.splitext(file)[0]

        print(f"\nProcessing {file}...")
        logging.info(f"Processing {file}")

        try:
            ingest_db(file_path, table_name, engine)
        except Exception as e:
            print(f"Error: {e}")
            logging.error(str(e))

    end = time.time()

    print("\n===================================")
    print("Data Ingestion Completed Successfully!")
    print(f"Total Time: {(end-start)/60:.2f} minutes")
    print("===================================")

    logging.info(f"Completed in {(end-start)/60:.2f} minutes")


if __name__ == "__main__":
    load_raw_data()

