class Database:
    """
    Act as a wrapper for the Database connection.
    """

    def add_document(self, collection_name, document):
        """
        Write data to a CSV file.
        """
        document.to_csv("assets/db/{collection_name}.csv", ";")

    def get_documents(self, collection_name, label_filter):
        """
        Extract data from a CSV file.
        """
        data = pd.read_csv("assets/db/{collection_name}.csv")
        return data[data["COD_DISCIP_ORIG"] == label_filter]
