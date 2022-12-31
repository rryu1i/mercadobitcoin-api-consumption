import os
from abc import ABC
import datetime
from typing import List, Dict, Union
import json


class DataTypeNotSupportedForIngestionException(Exception):
    def __init__(self, *args: object) -> None:
        self.data = data
        self.message = f"Data type {type(data)} is not supported for ingestion"
        super().__init__(self.message)


class DataWriter:
    def __init__(self, coin: str, api: str) -> None:
        self.api = api
        self.coin = coin
        self.filename = f"{self.api}/{self.coin}/{datetime.datetime.now()}.json"

    def _write_row(self, row: str) -> None:
        os.makedirs(os.path.dirname(self.filename), exist_ok=True)
        with open(self.filename, "a") as f:
            f.write(row)

    def _write_to_file(self, data: Union[List, dict]):
        if isinstance(data, dict):
            self._write_row(json.dumps(data) + "\n")
        elif isinstance(data, List):
            for element in data:
                self.write(element)
        else:
            raise DataTypeNotSupportedForIngestionException(data)

    def write(self, data: Union[List, dict]):
        self._write_to_file(data=data)
