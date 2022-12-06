

from django.db import connections
from CommonServices.Constants import


class DbConnector:

    def get_data_from_db(self, query, DB=DEFAULT_DB):
        """
        """
        cursor = connections[DB].cursor()
        cursor.execute(query)
        row = cursor.fetchall()
        print("data" + str(row))
        return row

    def get_data_from_db_with_columns(self, query, DB=DEFAULT_DB):
        """
        """
        cursor = connections[DB].cursor()
        cursor.execute(query)
        col_names = [desc for desc in cursor.description]
        row = cursor.fetchall()
        return col_names, row


    def get_cursor(self, DB=DEFAULT_DB):
        """
        """
        return connections[DB].cursor()


