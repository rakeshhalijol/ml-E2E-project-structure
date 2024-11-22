from dataclasses import dataclass
from sklearn.model_selection import train_test_split
import os


@dataclass
class DataIngestionConfig:
    train_data_path: str = os.path.join("atrifacts", "train.csv")
    test_data_path: str = os.path.join("atrifacts", "test.csv")
    raw_data_path: str = os.path.join("atrifacts", "data.csv")


class DataIngestion:
    def __init__(self) -> None:
        self.ingestion_config = DataIngestionConfig()

    def intiate_data_ingestion(self):
        pass
