import pandas as pd

class Database:
    """
    Act as a wrapper for the Database connection.
    """

    def add_document(self, collection_name, document):
        """
        Write data to a CSV file.
        """
        document.to_csv(
            f"assets/db/{collection_name}.csv", 
            mode="a", 
            sep=";", 
            header=False,
            index=False,
        )

    def get_documents(self, collection_name, label_filter):
        """
        Extract data from a CSV file.
        """
        data = pd.read_csv(f"assets/db/{collection_name}.csv", sep=";", index_col=0)
        id_equal_to_label_filter = data["COD_DISCIP_ORIG"] == label_filter
        filtered_data = data[id_equal_to_label_filter]
        return filtered_data
