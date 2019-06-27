class Database:
    """
    Act as a wrapper for the Database connection.
    """

    def add_document(self, collection_name, document):
        """
        Write data to a CSV file.
        """
        document.to_csv("assets/db/{collection_name}.csv", ";")
