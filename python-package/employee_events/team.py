# Import the QueryBase class
from .query_base import QueryBase
import pandas as pd

# Create a subclass of QueryBase
# called  `Team`
class Team(QueryBase):

    # Set the class attribute `name`
    # to the string "team"
    name = "team"

    # Define a `names` method
    # that receives no arguments
    # This method should return
    # a list of tuples from an sql execution
    def names(self) -> list:
        
        # Query 5
        # Write an SQL query that selects
        # the team_name and team_id columns
        # from the team table for all teams
        # in the database
        query = """
        SELECT 
            team_name,
            team_id
        FROM team
        ORDER BY team_name;
        """
        
        # Call the inherited self.query() method from QueryMixin
        rows = self.query(query)
        return [(str(row[0]), str(row[1])) for row in rows]

    # Define a `username` method
    # that receives an ID argument
    # This method should return
    # a list of tuples from an sql execution
    def username(self, id: int) -> list:

        # Query 6
        # Write an SQL query
        # that selects the team_name column
        # Use f-string formatting and a WHERE filter
        # to only return the team name related to
        # the ID argument
        query = f"""
        SELECT team_name
        FROM {self.name}
        WHERE {self.name}_id = {id};
        """
        
        # Call the inherited self.query() method from QueryMixin
        return self.query(query)

    # Below is method with an SQL query
    # This SQL query generates the data needed for
    # the machine learning model.
    # Without editing the query, alter this method
    # so when it is called, a pandas dataframe
    # is returns containing the execution of
    # the sql query
    def model_data(self, id):

        query = f"""
            SELECT positive_events, negative_events FROM (
                    SELECT employee_id
                         , SUM(positive_events) positive_events
                         , SUM(negative_events) negative_events
                    FROM {self.name}
                    JOIN employee_events
                        USING({self.name}_id)
                    WHERE {self.name}s.{self.name}_id = {id}
                    GROUP BY employee_id
                   )
                """
        
        # Call the inherited self.pandas_query() method from QueryMixin
        return self.pandas_query(query)
