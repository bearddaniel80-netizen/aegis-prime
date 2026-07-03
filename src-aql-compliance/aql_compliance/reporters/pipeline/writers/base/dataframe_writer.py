from abc import (
    ABC,
    abstractmethod,
)

import pandas as pd


class DataFrameWriter(
    ABC
):

    def write(
        self,
        artifact,
    ) -> None:
        
        self.destination = artifact.output_file

        for (
            table_name,
            rows,
        ) in artifact.tables.items():

            if not rows:
                continue

            if isinstance(rows, dict):
                rows = [rows]

            if hasattr(rows, "to_dict") and not isinstance(rows, list):
                rows = [rows.to_dict()]

            dataframe = (
                pd.DataFrame(
                    rows
                )
            )

            self.write_dataframe(
                table_name=table_name,
                dataframe=dataframe,
            )

    @abstractmethod
    def write_dataframe(
        self,
        table_name: str,
        dataframe: pd.DataFrame,
    ) -> None:
        pass