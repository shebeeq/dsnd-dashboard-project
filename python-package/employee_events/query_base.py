# Import any dependencies needed to execute sql queries
import sqlite3
from pathlib import Path
import pandas as pd

# Dynamically calculate the absolute path to the database file in this package
DB_PATH = Path(__file__).resolve().parent / "employee_events.db"

# Define a class called QueryBase
# Use inheritance to add methods
# for querying the employee_events database.
class QueryBase:

    # Create a class attribute called `name`
    # set the attribute to an empty string
    name = ""

    # Define a `names` method that receives
    # no passed arguments
    def names(self):
        # Return an empty list
        return []

    # Define an `event_counts` method
    # that receives an `id` argument
    # This method should return a pandas dataframe
    def event_counts(self, id: int) -> pd.DataFrame:

        # QUERY 1
        # Write an SQL query that groups by `event_date`
        # and sums the number of positive and negative events
        # Use f-string formatting to set the FROM {table}
        # to the `name` class attribute
        # Use f-string formatting to set the name
        # of id columns used for joining
        # order by the event_date column
        query = f"""
        SELECT 
            ev.event_date,
            SUM(ev.positive_events) AS positive_count,
            SUM(ev.negative_events) AS negative_count
        FROM employee_events ev
        JOIN {self.name} t ON ev.{self.name}_id = t.{self.name}_id
        WHERE t.{self.name}_id = ?
        GROUP BY ev.event_date
        ORDER BY ev.event_date;
        """
        
        # Connect to the database and return the data as a dataframe
        with sqlite3.connect(DB_PATH) as conn:
            df = pd.read_sql_query(query, conn, params=(id,))
        return df

    # Define a `notes` method that receives an id argument
    # This function should return a pandas dataframe
    def notes(self, id: int) -> pd.DataFrame:

        # QUERY 2
        # Write an SQL query that returns `note_date`, and `note`
        # from the `notes` table
        # Set the joined table names and id columns
        # with f-string formatting
        # so the query returns the notes
        # for the table name in the `name` class attribute
        query = f"""
        SELECT 
            n.note_date, 
            n.note
        FROM notes n
        JOIN {self.name} t ON n.{self.name}_id = t.{self.name}_id
        WHERE t.{self.name}_id = ?
        ORDER BY n.note_date;
        """
        
        # Connect to the database and return the data as a dataframe
        with sqlite3.connect(DB_PATH) as conn:
            df = pd.read_sql_query(query, conn, params=(id,))
        return df